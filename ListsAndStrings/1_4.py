#!/usr/bin/env python3
import unittest

# Task description
# Write a method to decide if two strings are anagrams or not.

class TestStringMethods(unittest.TestCase):

    def test_checker(self):
        self.assertTrue(are_anagrams("Add", "Dad"))
        self.assertTrue(are_anagrams("Cafe", "Face"))
        self.assertFalse(are_anagrams("Daisy", "Dayze"))
        self.assertFalse(are_anagrams("Weather", "Wether"))


def are_anagrams(stringOne, stringTwo):
    return sorted(stringOne.lower()) == sorted(stringTwo.lower())


if __name__ == "__main__":
    unittest.main()