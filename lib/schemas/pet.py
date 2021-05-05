from . import Schema
from ..tables.pet.petname import PetName
from ..tables.pet.petanimal import PetAnimal

class Pet(Schema):
    # Context initialization
    _ctx = {

    }

    # Fields / Attributes
    animal = PetAnimal()
    name = PetName()

    def __str__(self):
        return '{animal} named {name}'

if __name__ == '__main__':
    for i in range(10):
        Pet._build()