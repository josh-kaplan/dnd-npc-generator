"""

pet.py

"""

from .. import meta

class WildMagic(meta.Table):

    def lookup(self):
        event = self.get_event()
        event = ' '.join(event.strip().split())
        return '{}'.format(event)

    def get_event(self):
        data = [{
            'w':3,
            'v': '''
            A spectral shield hovers near you for the next minute, 
            granting you a +2 bonus to AC and immunity to Magic Missile.
            '''
        }, {'w': 2,
            'v': '''
            For the next minute, you can see any invisible creature if you have line 
            of sight to it.
            '''
        }, {'w': 3,
            'v': '''
            You are immune to being intoxicated by alcohol for the next 5d6 days.
            '''
        }, {'w': 2,
            'v': '''
            Your hair falls out but grows back within 24 hours.
            '''
        }, {'w': 2,
            'v': '''
            You cast Fireball as a 3rd-level spell centered on yourself.
            '''
        }, {'w': 3,
            'v': '''
            For the next minute, any flammable object you touch that isn't being worn 
            or carried by another creature bursts into flame.
        '''
        }, {'w': 2,
            'v': '''
            You cast Magic Missile as a 5th-level spell.
            '''
        }, {'w': 3,
            'v': '''
            You regain your lowest-level expended spell slot.
            '''
        }, {'w': 1,
            'v': '''
            Roll a d10. Your height changes by a number of inches equal to the roll. 
            Roll another die. If the roll is odd, you shrink. If the roll is even, 
            you grow. This effect lasts until your next long rest.
        '''
        }, {'w': 2,
            'v': '''
            For the next minute, you must shout when you speak.
            '''
        }, {'w': 2,
            'v': '''
            You cast Confusion centered on yourself.
        '''
        }, {'w': 2,
            'v': '''
            You cast Fog Cloud centered on yourself.
        '''
        }, {'w': 2,
            'v': '''
            For the next minute, you regain 5 hit points at the start of each of 
            your turns.
        '''
        }, {'w': 1,
            'v': '''
            Up to three creatures you choose within 30 feet of you take 4d10 
            lightning damage.
        '''
        }, {'w': 3,
            'v': '''
            You grow a long beard made of feathers that remains until you sneeze, 
            at which point the feathers explode out from your face.'''
        }, {'w': 2,
            'v': '''
            You are frightened by the nearest creature until the end of your next 
            turn.'''
        }, {'w': 2,
            'v': '''
            You cast Grease centered on yourself.'''
        }, {'w': 1,
            'v': '''
            Each creature within 30 feet of you becomes invisible for the next
            minute. The invisibility ends on a creature when it attacks or casts a 
            spell.'''
        }, {'w': 2,
            'v': '''
            Creatures have disadvantage on saving throws against the next spell you 
            cast in the next minute that involves a saving throw.'''
        }, {'w': 3,
            'v': '''
            You gain resistance to all damage for the next minute.'''
        }, {'w': 1,
            'v': '''
            Your skin turns a vibrant shade of blue. A Remove Curse spell can end 
            this effect.'''
        }, {'w': 2,
            'v': '''
            A random creature within 60 feet of you becomes poisoned for 1d4 hours.'''
        }, {'w': 2,
            'v': '''
            You glow with bright light in a 30-foot radius for the next minute. 
            Any creature that ends its turn within 5 feet of you is blinded until 
            the end of its next turn. Ranged attacks have advantage against you.'''
        }, {'w': 3,
            'v': '''
            For the next minute, all your spells with a casting time of 1 action 
            have a casting time of 1 bonus action.'''
        }, {'w': 2,
            'v': '''
            You cast Polymorph on yourself. If you fail the saving throw, you turn
            into a sheep for the spell's duration.'''
        }, {'w': 2,
            'v': '''
            You teleport up to 60 feet to an unoccupied space of your choice that 
            you can see.'''
        }, {'w': 3,
            'v': '''
            Illusory butterflies and flower petals flutter in the air within 10 feet
            of you for the next minute.'''
        }, {'w': 1,
            'v': '''
            You are transported to the Astral Plane until the end of your next turn, 
            after which time you return to the space you previously occupied or the 
            nearest unoccupied space if that space is occupied.'''
        }, {'w': 3,
            'v': '''
            You can take one additional action immediately.'''
        }, {'w': 2, 
            'v': '''
            Maximize the damage of the next damaging spell you cast within the next 
            minute.'''
        }, {'w': 2,
            'v': '''
            Each creature within 30 feet of you takes 1d10 necrotic damage. You 
            regain hit points equal to the sum of the necrotic damage dealt.'''
        }, {'w': 1,
            'v': '''
            Roll a d10. Your age changes by a number of years equal to the roll. If 
            the roll is odd, you get younger (minimum 1 year old). If the roll is 
            even, you get older. The effect lasts until the end of yout next 
            long rest.'''
        }, {'w': 2,
            'v': '''
            You cast Mirror Image.'''
        }, {'w': 2,
            'v': '''
            You cast Fly on a random creature within 60 feet of you.'''
        }, {'w': 2,
            'v': '''
            You regain 2d10 hit points.'''
        }, {'w': 1,
            'v': '''
            You become invisible for the next minute. During that time, other 
            creatures can't hear you. The invisibility ends if you attack or cast a 
            spell.'''
        }, {'w': 3,
            'v': '''
            You turn into a potted plant until the start of your next turn. While a 
            plant, you are incapacitated and have vulnerability to all damage. If 
            you drop to 0 hit points, your pot breaks, and your form reverts.'''
        }, {'w': 3,
            'v': '''
            If you die within the next minute, you immediately come back to life as 
            if by the Reincarnate spell.'''
        }, {'w': 3,
            'v': '''
            For the next minute, you can teleport up to 20 feet as a bonus action on 
            each of your turns.'''
        }, {'w': 1,
            'v': '''
            Your size increases by one size category for the next minute.'''
        }, {'w': 2,
            'v': '''
            You cast Levitate on yourself.'''
        }, {'w': 3,
            'v': '''
            You and all creatures within 30 
            feet of you gain vulnerability to piercing damage for the next minute.'''
        }, {'w': 1,
            'v': '''
            A unicorn controlled by the DM appears in a space within 5 feet of you, 
            then disappears 1 minute later.'''
        }, {'w': 2,
            'v': '''
            You are surrounded by faint, ethereal music for the next minute.'''
        }, {'w': 3,
            'v': '''
            You can't speak for the next minute. Whenever you try, pink bubbles 
            float out of your mouth.'''
        }]
        table = meta.WeightedTable(data)
        return table.choice()


if __name__ == '__main__':
    print(WildMagic().lookup())

