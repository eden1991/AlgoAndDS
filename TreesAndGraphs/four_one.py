from AlgoAndDS.TreesAndGraphs.BinaryTree.node import Node

'''
4.1 Implement a function to check if a binary tree is balanced. For the purposes of this
    question, a balanced tree is defined to be a tree such that the heights of the two
    subtrees of any node never differ by more than one.
'''

def traverse_left(root):
    left_depth = [0]

    if root:
        left_depth = left_depth + traverse_left(root.left)
        left_depth[0] += 1

    return left_depth

def traverse_right(root):
    right_depth = [0]

    if root:
        right_depth = right_depth + traverse_right(root.right)
        right_depth[0] += 1

    return right_depth

def is_balanced(root):
    left_side = len(traverse_left(root))
    right_side = len(traverse_right(root))

    if left_side > right_side:
        difference = left_side - right_side
    else:
        difference = right_side - left_side

    return difference <= 1
