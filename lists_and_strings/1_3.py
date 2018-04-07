#!/usr/bin/env python3
import unittest

# Task description
# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.

class TestStringMethods(unittest.TestCase):

    def test_checker(self):
        self.assertEqual(remove_duplicates("Pool"), "Pol")
        self.assertEqual(remove_duplicates("Inferior"), "Inferio")
        self.assertEqual(remove_duplicates("Woolloomoolloo"), "Wolm")

def remove_duplicates(word):
    buffer = ""
    for letter in range(len(word)):
        if word[letter] not in buffer:
            buffer = buffer + word[letter]

    return buffer


if __name__ == "__main__":
    unittest.main()