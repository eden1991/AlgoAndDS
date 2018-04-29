#!/usr/bin/env python3
from unorderedList import UnorderedList
import unittest

# Implement an algorithm to find the nth to last element of a singly linked list

class TestFindFromNth(unittest.TestCase):

    def test_checker(self):
        mylist = UnorderedList()
        numbers = [31, 77, 17, 93, 26, 54]
        for number in numbers:
            mylist.add(number)

        # The linked list should contain 11 items overall
        self.assertEqual(mylist.size(), 6)

        # Let n equal 3 as we want the nodes from indice 3 through
        # to the last node in the list.
        '''
        Keep in mind that the node item added in first will end up 
        as the last node item due to individually pushing each node
        in to the linkedlist. So, when mentally figuring out what 
        elements should end up in the new linkedlist, count in from
        the last element in the numbers list above.
        '''
        newlist = mylist.findFromNth(3)
        self.assertEqual(newlist.size(), 3)

        # The 3 nodes inside the list should be 31, 77, and 17
        self.assertTrue(newlist.search(31))
        self.assertTrue(newlist.search(77))
        self.assertTrue(newlist.search(17))

        # Output to console for visual confirmation
        newlist.print_list()
        print("---")

        # Test that we grab node items from n-1 to n
        newlist = mylist.findFromNth(mylist.size()-2)
        self.assertEqual(newlist.size(), 2)

        # The 2 nodes inside the list should be 31 and 77
        self.assertTrue(newlist.search(31))
        self.assertTrue(newlist.search(77))

        # Output to console for visual confirmation
        newlist.print_list()
        print("---")

        # Test that we can grab only the head node
        newlist = mylist.findFromNth(mylist.size()-1)
        self.assertEqual(newlist.size(), 1)

        # The only node inside the list should be 31
        self.assertTrue(newlist.search(31))

        # Output to console for visual confirmation
        newlist.print_list()


if __name__ == '__main__':
    unittest.main()

