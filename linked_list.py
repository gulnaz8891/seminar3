from mylistiterator import MyListIterator
class Set:
    def __init__(self, data=None):
        self.data = {}
        if data != None: 
            if len(data) != len(set(data)):
                data = set(data)
            for d in data:
                self.data[d] = d
    def add(self, i):
        if i in self.data.keys():
            return 'Already in set'
        self.data[i] = i
    def remove(self, i):
        if i not in self.data.keys():
            return 'Not in set'
        self.data.pop(i)
    def __len__(self):
        return len(self.data.keys())
    def contains(self, i):
        if i in self.data.keys():
            return True
        return False
    def union(self, otherSet):
        setData = list(set(self.data.keys()) | set(otherSet.data.keys()))
        unionSet = Set(setData)
        return unionSet
    def intersection(self, otherSet):
        setData = list(set(self.data.keys()) & set(otherSet.data.keys()))
        intersectionSet = Set(setData)
        return intersectionSet
    def difference(self, otherSet):
        setData = list(set(self.data.keys()) ^ set(otherSet.data.keys()))
        differenceSet = Set(setData)
        return differenceSet
    def subset(self, otherSet):
        if set(self.data.keys()) < set(otherSet.data.keys()):
            return True
        return False
    def __repr__(self):
      return '['+', '.join(str(x) for x in self.data.keys())+']'
    def __iter__( self ):
      return MyListIterator(self.data)
    
