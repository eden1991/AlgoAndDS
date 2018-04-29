#!/usr/bin/env python3
from unorderedList import UnorderedList
import unittest

# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

class TestRmoveduplicates(unittest.TestCase):

    def test_checker(self):
        mylist = UnorderedList()
        numbers = [31, 77, 17, 93, 93, 26, 26, 26, 54, 54, 54]
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

        remove_duplicates(duplicate_results, mylist)

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

        # There should be no duplicates remaining, the find_duplicates function
        # should return an empty dictionary
        self.assertEqual(mylist.find_duplicates(), {})


# Function to leverage the remove method to remove duplicates from the unsorted linked list
def remove_duplicates(duplicates, UnorderedLinkedList):
    # Iterates through each data item in the provided list and remove them
    # from the UnorderedList linked list
    for key in duplicates:
        # We add -1 to the end range as we want to leave 1 single occurrence of the node item
        for count in range(0, duplicates[key]-1):
            UnorderedLinkedList.remove(key)


if __name__ == '__main__':
    unittest.main()

