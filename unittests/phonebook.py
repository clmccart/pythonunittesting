import os

class Phonebook():

    def __init__(self):
        self.entries = {}
    
    """Add a new entry to the phonebook.

    Args:
        name: a string representing the name of the contact
        number: a string representing the phone number associated with the contact
    Returns:
        None
    
    >>> add("Bob", "1234567")
    >>> add("Carl", "18002345")
    >>> add("Farley", "143")
    """
    def add(self, name, number):
        self.entries[name] = number
    
    def lookup(self, name):
        return self.entries[name]
    
    def get_names(self):
        return self.entries.keys()
    
    def get_numbers(self):
        return self.entries.values()
    
    def is_consistent(self):
        return True
