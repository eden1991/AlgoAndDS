#!/usr/bin/env python3

import unittest
from AlgoAndDS.TreesAndGraphs.BinaryTree.node import Node
from AlgoAndDS.TreesAndGraphs.four_one import check_balance

class TestStackMethods(unittest.TestCase):
    '''
    4.1 Implement a function to check if a binary tree is balanced. For the purposes of this
        question, a balanced tree is defined to be a tree such that the heights of the two
        subtrees of any node never differ by more than one.
    '''
    def test_4_1(self):
        root = Node(12)
        # Add four nodes with values greater than the root and 2 that are less than the root
        root.insert(8)
        root.insert(4)
        root.insert(15)
        root.insert(22)
        root.insert(30)
        root.insert(31)

        # The tree should currently be unbalanced, so we expect False
        self.assertEqual(check_balance(root), -1)

        # Add one more node to the left subtree
        root.insert(1)

        # We should see False still as the two subtrees are still unbalanced
        self.assertEqual(check_balance(root), -1)

        # Add one more node to the left side
        root.insert(6)

        # The tree should still be unbalanced, so we expect False
        self.assertEqual(check_balance(root), -1)

        # Remove the entire right subtree
        root.right = None

        # The tree should be completely unbalanced now, so we still expect False
        self.assertEqual(check_balance(root), -1)

        # Remove the left subtree too
        root.left = None

        # The tree should be balanced now as there are no subtrees
        self.assertEqual(check_balance(root), 1)

        # Now add all the previous nodes back in
        root.insert(8)
        root.insert(4)
        root.insert(15)
        root.insert(22)
        root.insert(30)
        root.insert(31)
        root.insert(1)
        root.insert(6)
        # And add the below nodes to balance the tree
        root.insert(20)
        root.insert(21)
        root.insert(14)
        root.insert(13)
        root.insert(9)

        # The tree should be balanced now as there are no height differences greater than 1 amongst the subtrees
        self.assertEqual(check_balance(root), 5)



if __name__ == '__main__':
    unittest.main()