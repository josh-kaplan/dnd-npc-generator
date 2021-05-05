"""

pet.py

"""

from .. import meta
from . import petname

class PetAnimal(meta.Table):

    def lookup(self):
        return 'a {} named {}'.format(self.get_animal(), petname.PetName().lookup())

    def get_animal(self):
        table = meta.WeightedTable([
            # Common (15-20)
            { "w":24, "v":"dog"},
            { "w":20, "v":"cat"},
            { "w":20, "v":"horse"},
            { "w":15, "v":"pidgeon"},
            { "w":18, "v":"songbird"},
            { "w":16, "v":"mouse"},
            { "w":16, "v":"rat"},
            { "w":18, "v":"snake"},
            # Uncommon (10-15)
            { "w":15, "v":"owl"},
            { "w":14, "v":"fox"},
            { "w":15, "v":"turtle"},
            { "w":15, "v":"falcon"},
            { "w":15, "v":"hawk"},
            { "w":10, "v":"rock"},
            { "w":10, "v":"guinea pig"},
            { "w":10, "v":"hamster"},
            { "w":13, "v":"gecko"},
            { "w":15, "v":"rabbit"},
            { "w":15, "v":"parrot"},
            { "w":13, "v":"ferret"},
            # Rare (5-10)
            { "w":10, "v":"eagle"},
            { "w":8, "v":"tiger"},
            { "w":5, "v":"lion"},
            { "w":7, "v":"bear"},
            # Very Rare (1-5)
            { "w":1, "v":"tiny golem"},
            { "w":1, "v":"tiny ooze"},
            { "w":1, "v":"zombie"},
            { "w":1, "v":"dragon hatchling"},
            { "w":1, "v":"kobold"},
            { "w":2, "v":"pseudodragon"}
        ])
        return table.choice()


if __name__ == '__main__':
    print(PetAnimal().lookup())