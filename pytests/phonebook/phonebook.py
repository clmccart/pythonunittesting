class Phonebook:
    """
    A doctest to prove to myself that I can 

    >>> pb=Phonebook()
    >>> pb.add("Farley", "1234")
    >>> pb.lookup("Farley")
    '1234'
    """
    def __init__(self, *args, **kwargs):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def names(self):
        return self.entries.keys()

    def numbers(self):
        return self.entries.values()

if __name__ == "__main__":
    import doctest
    doctest.testmod()        
