#!/usr/bin/env python
import argparse
import json
import math
import random
import sys
from pprint import pprint
from pymongo import MongoClient

client = MongoClient()
db = client['dnd']

def main():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('--race', nargs='+')
    parser.add_argument('--class', nargs='+')
    parser.add_argument('--profession-type', type=str)
    args = parser.parse_args()
    print(args)

    print('-'*74)

    # Build the query
    query = {
        'screened': {'$ne': False},
        '$and': []
    }

    # Add race filters to the query
    if args.race is not None:
        expr = {'$or': []}
        for race in args.race:
            expr['$or'].append({'description.race': str(race)})
        query['$and'].append(expr)

    # Add class filters to the query
    if getattr(args, 'class') is not None:
        expr = {'$or': []}
        for cls in getattr(args, 'class'):
            expr['$or'].append({'description.class': str(cls)})
        query['$and'].append(expr)
    
    # Add profession type to the query
    if args.profession_type is not None:
        expr = {'tags.professionType': str(args.profession_type)}
        query['$and'].append(expr)

    # Cleanup query
    if len(query['$and']) == 0:
        del query['$and']

    print('Query: ', json.dumps(query, indent=4))
    count = db.npc.count_documents(query)
    print('Found {} matching results.'.format(count))

    while 1:    
        N = random.randint(0, count)
        results = db.npc.find(query).limit(1).skip(N)
        docs = [ doc for doc in results ] 
        if len(docs) == 0:
            break

        doc = docs[0]
        print_npc(doc)

        use = input('Mark NPC as used? (y/n) ')
        if use == 'y':
            newvals = {}
            newvals['screened'] = True

            notes = input('Usage Notes: ')
            newvals['notes'] = notes

            db.npc.update_one({'_id': doc['_id']}, {'$set': newvals})


def cm2ft(cm):
    _inches = 0.393701 * cm
    ft = math.floor(_inches/12) 
    inch = round(_inches % 12)
    return '{ft}\'{inch}"'.format(ft=ft, inch=inch)


def abilityWithMod(ability):
    modifier = int((ability-10)/2)
    if modifier >= 0:
        modifier = '+{modifier}'.format(modifier=modifier)
    spaces = ' ' if (ability < 10) else ''
    return '{0}{1} ({2})'.format(spaces, ability, modifier)


def print_npc(npc):
    fmt = {
        'color': '\u001b[36m',
        'esc': '\u001b[0m',
        'name': npc['description']['name'],
        'age': npc['description']['age'],
        'gender': npc['description']['gender'],
        'race': npc['description']['race'],
        'occupation': npc['description']['occupation'],
        'Pronoun': npc['description']['pronounCapit'],
        'pronoun': npc['description']['pronounMinus'],
        'ft': cm2ft(npc['physical']['height']),
        'hair': npc['physical']['hair'],
        'eyes': npc['physical']['eyes'],
        'skin': npc['physical']['skin'],
        'face': npc['physical']['face'],
        'build': npc['physical']['build'],
        'phys_special1': npc['physical']['special1'],
        'phys_special2': npc['physical']['special2'],
        'ptraits1': npc['ptraits']['traits1'],
        'ptraits2': npc['ptraits']['traits2'],
        'pquirks': npc['pquirks']['description'],
        'hook': npc['hook']['description'],
        'religion': npc['religion']['description'],
        'alignment_good': npc['alignment']['good'],
        'alignment_moralneutral': npc['alignment']['moralneutral'],
        'alignment_evil': npc['alignment']['evil'],
        'alignment_lawful': npc['alignment']['lawful'],
        'alignment_ethicalneutral': npc['alignment']['ethicalneutral'],
        'alignment_chaotic': npc['alignment']['chaotic'],
        'str': abilityWithMod(npc['abilities']['str']),
        'dex': abilityWithMod(npc['abilities']['dex']),
        'con': abilityWithMod(npc['abilities']['con']),
        'int': abilityWithMod(npc['abilities']['int']),
        'wis': abilityWithMod(npc['abilities']['wis']),
        'cha': abilityWithMod(npc['abilities']['cha'])
    }
    
    s = '''
{color}Description{esc}
{name} is a {age} year old {gender} {race} {occupation}. 
{Pronoun}has {hair}{eyes}. 
Standing {ft} tall with {build}, {pronoun}has {skin} and {face}. 
{phys_special1} {phys_special2}

{color}Personality and Background{esc}
{ptraits1}
{ptraits2}
{pquirks}
{hook}
{religion}

{color}Alignment Tendencies{esc}
Good, Neutral, Evil:      {alignment_good}, {alignment_moralneutral}, {alignment_evil}
Lawful, Neutral, Chaotic: {alignment_lawful}, {alignment_ethicalneutral}, {alignment_chaotic}

{color}Stats{esc}
STR    {str}        INT    {int}
DEX    {dex}        WIS    {wis}
CON    {con}        CHA    {cha}
'''.format(**fmt)
    print('-'*74)
    print(s)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('')
        print('Goodbye.')
