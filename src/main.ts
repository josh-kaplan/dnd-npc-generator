import { notDeepStrictEqual } from 'assert';
import {generate} from './generate';

let options = {
    race:           null,
    subrace:        null,
    classorprof:    null,
    occupation1:    null,
    occupation2:    null,
    alignment:      null,
    plothook:       null,
    gender:         null,
}

console.time('Generate')  
let npcs = []
for (let i = 0; i < 1; i++) {
    let npc = generate(options)
    npcs.push(npc.npc)
}
console.timeEnd('Generate')
//console.log(npcs)
npcs.forEach(npc => printNPC(npc))

function abilityWithMod(ability: number) {
    let nModifier = (ability-10)%2;
    let modifier = (nModifier >= 0) ? `+${nModifier}` : `${nModifier}`;
    let spaces = (ability < 10) ? ' ' : '';
    return `    ${spaces}${ability} (${modifier})`;
}


function cm2ft(cm: any) {
    let _inches = 0.393701 * Number(cm);
    let ft = Math.floor(_inches/12) 
    let inch = Math.round(_inches % 12);
    return `${ft}'${inch}"`;
}

function printNPC(npc: any) {
    let pronoun = npc.description.pronounCapit;
    let ft = cm2ft(npc.physical.height);

    console.log(`
[General Description]
${npc.description.name} is a ${npc.description.age} year old ${npc.description.gender} ${npc.description.race} ${npc.description.occupation}.

[Appearance]
${pronoun}has ${npc.physical.hair}${npc.physical.eyes}. 
${pronoun}has ${npc.physical.skin} and ${npc.physical.face}.
${pronoun}has ${npc.physical.build} and stands ${npc.physical.height}cm (${ft}) tall.
${npc.physical.special1}
${npc.physical.special2}

[Personality and Background]
${npc.ptraits.traits1}
${npc.ptraits.traits2}
${npc.pquirks.description}
${npc.hook.description}
${npc.religion.description}

[Alignment Tendencies]
Good:       ${npc.alignment.good}
Neutral:    ${npc.alignment.moralneutral}
Evil:       ${npc.alignment.evil}

Lawful:     ${npc.alignment.lawful}
Neutral:    ${npc.alignment.ethicalneutral}
Chaotic:    ${npc.alignment.chaotic}

[Stats]
STR ${abilityWithMod(npc.abilities.str)}
DEX ${abilityWithMod(npc.abilities.dex)}
CON ${abilityWithMod(npc.abilities.con)}
INT ${abilityWithMod(npc.abilities.int)}
WIS ${abilityWithMod(npc.abilities.wis)}
CHA ${abilityWithMod(npc.abilities.cha)}
`);
}