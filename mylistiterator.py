class MyListIterator:
    def __init__(self, d=0):
        self.data = d

    def __iter__(self):
        return self

    def __next__(self):
        data = self.data
        self.data = 1
        return data
