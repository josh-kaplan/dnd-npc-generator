"""

pet.py

"""
import random
import json
from .. import meta

class RandomStats(meta.Table):

    def lookup(self):
        return json.dumps(self.get_stats(), indent=4)

    def get_stats(self):
        return{
            'str': self.roll_stat(),
            'dex': self.roll_stat(),
            'con': self.roll_stat(),
            'int': self.roll_stat(),
            'wis': self.roll_stat(),
            'cha': self.roll_stat()
        }
    
    def roll_stat(self):
        d6 = [ random.randint(1,6) for i in range(4) ]
        lowest = min(d6)
        d6.remove(lowest)
        return sum(d6)


if __name__ == '__main__':
    print(RandomStats().lookup())