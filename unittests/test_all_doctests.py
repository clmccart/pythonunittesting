import unittest
import doctest
import unittests.phonebook as phonebook

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(phonebook))
    return tests