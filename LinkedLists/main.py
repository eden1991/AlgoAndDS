#!/usr/bin/env python3
from unorderedList import UnorderedList
import unittest


class TestLinkedListMethods(unittest.TestCase):

    def test_2_1(self):
        mylist = UnorderedList()
        numbers = [ 31, 77, 17, 93, 93, 26, 26, 26, 54, 54, 54 ]
        for number in numbers:
            mylist.add(number)

        # The linked list should contain 11 items overall
        self.assertEqual(mylist.size(), 11)

        duplicate_results = mylist.find_duplicates()

        # The duplicates should be:
        # 93 occurs a second time
        # 26 occurs a third time
        # 54 occurs a third time
        self.assertEqual(duplicate_results[93], 2)
        self.assertEqual(duplicate_results[26], 3)
        self.assertEqual(duplicate_results[54], 3)

        mylist.remove_duplicates()

        # The size of the Unordered Linked list should be 6
        self.assertEqual(mylist.size(), 6)
        # There should still be an occurrence of every digit:
        # 31, 77, 17, 93, 26, 54
        self.assertTrue(mylist.search(31))
        self.assertTrue(mylist.search(77))
        self.assertTrue(mylist.search(17))
        self.assertTrue(mylist.search(93))
        self.assertTrue(mylist.search(26))
        self.assertTrue(mylist.search(54))

        # There should be no duplicates remaining, running the find_duplicates function
        # should still leave the linkedlist untouched
        mylist.remove_duplicates()
        self.assertEqual(mylist.size(), 6)


    def test_2_2(self):
        mylist = UnorderedList()
        numbers = [ 31, 77, 17, 93, 26, 54 ]
        for number in numbers:
            mylist.add(number)

        # The linked list should contain 6 items overall
        self.assertEqual(mylist.size(), 6)

        # Let n equal 3 as we want the node at indice 3 which
        # will enable us to reach through to the last node in the list.
        newNode = mylist.findFromNth(3)
        self.assertEqual(newNode.getData(), 93)

        # Test that we can request the first item in the list
        newNode = mylist.findFromNth(0)
        self.assertEqual(newNode.getData(), 31)

        # Test that we can request the last item in the list
        newNode = mylist.findFromNth(mylist.size()-1)
        self.assertEqual(newNode.getData(), 54)

        # Test that we can't request something by passing in a non-existent indice
        newNode = mylist.findFromNth(7)
        self.assertEqual(newNode.getData(), None)

    def test_2_6(self):
        mylist = UnorderedList()
        # Purposely add in additional letters
        letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
        for letter in letters:
            mylist.add(letter)

        # Purposely create an endless loop by changing the next node after 'e' to be 'c'
        mylist.change_next('e', 'c')

        # Test that c is in fact at the head of the loop
        self.assertEqual(mylist.find_loop_head(), 'c')



if __name__ == '__main__':
    unittest.main()