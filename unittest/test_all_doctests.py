import unittest
import doctest
import phonebook

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(phonebook))
    return tests