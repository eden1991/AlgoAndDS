#!/usr/bin/env python3
import unittest

# Task description
# Write a method to replace all spaces in a string with ‘%20’.

class TestStringMethods(unittest.TestCase):

    def test_checker(self):
        self.assertEqual(substitute_spaces("Hello there"), "Hello%20there")
        self.assertEqual(substitute_spaces("Nospaces"), "Nospaces")
        self.assertEqual(substitute_spaces("In the end, it doesn't even matter"), "In%20the%20end,%20it%20doesn't%20even%20matter")
        self.assertEqual(substitute_spaces("No%20spaces"), "No%20spaces")
        self.assertEqual(substitute_spaces(" Justtwospaces "), "%20Justtwospaces%20")

def substitute_spaces(sentence):
    return sentence.replace(" ", '%20')


if __name__ == '__main__':
    unittest.main()