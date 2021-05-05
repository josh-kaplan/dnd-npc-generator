import random


class Table(object):
    """
    """
    def __init__(self, ctx={}):
        self._ctx = ctx


class WeightedTable(object):
    """
    """    
    def __init__(self, _data):
        self._table = _data

    def lookup(self):
        raise Error('Classes that inherit from WeightedTable must define a lookup method.')

    def choice(self):
        # NOTE: This will be a O(n) operation
        tmp = []
        for row in self._table:
            for i in range(row['w']):
                tmp.append(row['v'])
            
        return random.choice(tmp)
