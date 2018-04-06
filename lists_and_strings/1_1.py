#!/usr/bin/env python3
import unittest

# Task description
# Implement an algorithm to determine if a string has all unique characters. What if you
# can not use additional data structures?


class TestStringMethods(unittest.TestCase):

    def test_checker(self):
        self.assertFalse(check_unique("Pool"))
        self.assertTrue(check_unique("Police"))
        self.assertTrue(check_unique("Endeavor"))
        self.assertTrue(check_unique("AWS"))
        self.assertFalse(check_unique("Google"))
        self.assertFalse(check_unique("ghwuaighiaewhgjkwea"))


def check_unique(word):
    buffer = ""
    unique = True
    # Iterate through the string passed in to the function
    for letter in word:
        # Check if the letter exists in the buffer string.
        # If it exists, then break out from the loop as the string is not unique.
        if letter in buffer:
            unique = False
            break
        else:
            # We've encountered the first occurrence of letter, so append it in to
            # the buffer for comparison in the next iteration of the loop
            buffer = buffer + letter

    return unique


if __name__ == "__main__":
    unittest.main()
