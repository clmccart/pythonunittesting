from pytests.phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook():
    return Phonebook()


def test_and_lookup_entry(phonebook):
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")


def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Alice", "12345")
    assert "Alice" in phonebook.names()
    assert "12345" in phonebook.numbers()


def test_missing_entry_raises_keyerror(phonebook):
    pytest.skip("Uninteresting")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
