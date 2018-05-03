#!/usr/bin/env python3
from unorderedList import UnorderedList
import unittest

# Given a circular linked list, implement an algorithm which returns node at the beginning
# of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an
# earlier node, so as to make a loop in the linked list.
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

class TestFindFromNth(unittest.TestCase):

    def test_checker(self):
        mylist = UnorderedList()
        # Purposely add in additional
        letters = [ 'a', 'b', 'c', 'd', 'e', 'c', 'c', 'c' ]
        for letter in letters:
            mylist.add(letter)

        # Purposely create an endless loop by changing the next node after 'e' to be 'c'
        mylist.change_next('e', 'c')

        # Test that c is in fact at the head of the loop
        self.assertEqual(mylist.find_loop_head(), 'c')


if __name__ == '__main__':
    unittest.main()

