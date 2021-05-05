"""

pet.py

"""

from .. import meta

class PetName:
    def __init__(self):
        pass

    def lookup(self, ctx={}):
        return self.get_name()

    def get_name(self):
        table = meta.WeightedTable([
            { "w":1, "v":"Bagel"},
            { "w":1, "v":"Bailey"},
            { "w":1, "v":"Bandit"},
            { "w":1, "v":"Bear"},
            { "w":1, "v":"Bella"},
            { "w":1, "v":"Benson"},
            { "w":1, "v":"Bentley"},
            { "w":1, "v":"Biscuit"},
            { "w":1, "v":"Bobby"},
            { "w":1, "v":"Brandy"},
            { "w":1, "v":"Bubbles"},
            { "w":1, "v":"Buddy"},
            { "w":1, "v":"Button"},
            { "w":1, "v":"Calvin"},
            { "w":1, "v":"Caleb"},
            { "w":1, "v":"Charlie"},
            { "w":1, "v":"Coco"},
            { "w":1, "v":"Cooper"},
            { "w":1, "v":"Cupcake"},
            { "w":1, "v":"Daisy"},
            { "w":1, "v":"Diablo"},
            { "w":1, "v":"Dino"},
            { "w":1, "v":"Ernest"},
            { "w":1, "v":"Ernie"},
            { "w":1, "v":"Ford"},
            { "w":1, "v":"Fuzzy"},
            { "w":1, "v":"George"},
            { "w":1, "v":"Girl"},
            { "w":1, "v":"Gizmo"},
            { "w":1, "v":"Goofy"},
            { "w":1, "v":"Jack"},
            { "w":1, "v":"Jacky"},
            { "w":1, "v":"Jester"},
            { "w":1, "v":"John"},
            { "w":1, "v":"Kitty"},
            { "w":1, "v":"Lady"},
            { "w":1, "v":"Lily"},
            { "w":1, "v":"Lucy"},
            { "w":1, "v":"Luna"},
            { "w":1, "v":"Maggie"},
            { "w":1, "v":"Marshmallow"},
            { "w":1, "v":"Max"},
            { "w":1, "v":"Mister Big"},
            { "w":1, "v":"Mister Man"},
            { "w":1, "v":"Molly"},
            { "w":1, "v":"Monkey"},
            { "w":1, "v":"Mooshie"},
            { "w":1, "v":"Nellie"},
            { "w":1, "v":"Ninja"},
            { "w":1, "v":"Noodle"},
            { "w":1, "v":"Nugget"},
            { "w":1, "v":"Paddington"},
            { "w":1, "v":"Paul"},
            { "w":1, "v":"Peanut"},
            { "w":1, "v":"Pixie"},
            { "w":1, "v":"Princess"},
            { "w":1, "v":"Puddles"},
            { "w":1, "v":"Puddley"},
            { "w":1, "v":"Rexy"},
            { "w":1, "v":"Ringo"},
            { "w":1, "v":"Rocky"},
            { "w":1, "v":"Rory"},
            { "w":1, "v":"Roxie"},
            { "w":1, "v":"Rufus"},
            { "w":1, "v":"Screech"},
            { "w":1, "v":"Smokey"},
            { "w":1, "v":"Snickers"},
            { "w":1, "v":"Spark"},
            { "w":1, "v":"Stella"},
            { "w":1, "v":"Stitch"},
            { "w":1, "v":"Sunny"},
            { "w":1, "v":"Teddy"},
            { "w":1, "v":"Tiger"},
            { "w":1, "v":"Trinket"},
            { "w":1, "v":"Trixie"},
            { "w":1, "v":"Willow"}
        ])
        return table.choice()
