#!/usr/bin/env python3

import unittest
from AlgoAndDS.TreesAndGraphs.BinaryTree.node import Node
from AlgoAndDS.TreesAndGraphs.four_one import is_balanced

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
        self.assertFalse(is_balanced(root))

        # Add one more node to the left side to balance out the left subtree
        root.insert(1)

        # We should see True now as the hights of the two subtrees don't differ by more than one (the tree is balanced)
        self.assertTrue(is_balanced(root))

        # Add one more node to the left side
        root.insert(6)

        # The tree should still be balanced, so we expect True (the difference is 0 now
        self.assertTrue(is_balanced(root))

        # Remove the entire right subtree
        root.right = None

        # The tree should be completely unbalanced now, so we expect False
        self.assertFalse(is_balanced(root))

        # Remove the left subtree too
        root.left = None

        # The tree should be balanced now as there are no subtrees
        self.assertTrue(is_balanced(root))


if __name__ == '__main__':
    unittest.main()