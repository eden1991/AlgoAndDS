#!/usr/bin/env python3
import unittest

# Task description
# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
# five characters, including the null character.)


class TestStringMethods(unittest.TestCase):

    def test_checker(self):
        self.assertEqual(reverse('Pool\0'), 'looP\0')
        self.assertEqual(reverse('Police\0'), 'eciloP\0')
        self.assertEqual(reverse('Monitor\0'), 'rotinoM\0')


def reverse(word):
    reversed = ""
    # Loop through each letter of the string passed in to the function from back-to-front
    # and append each letter in to the above variable, excluding the null string at the end.
    for letter in range(len(word)-2, -1, -1):
        reversed = reversed + word[letter]
    # Now append the null string
    reversed = reversed + word[len(word)-1]

    return reversed


if __name__ == '__main__':
    unittest.main()
