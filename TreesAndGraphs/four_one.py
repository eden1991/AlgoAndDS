'''
4.1 Implement a function to check if a binary tree is balanced. For the purposes of this
    question, a balanced tree is defined to be a tree such that the heights of the two
    subtrees of any node never differ by more than one.
'''


from AlgoAndDS.TreesAndGraphs.BinaryTree.node import Node


def check_balance(root):
    # Base case: if the root is empty, then it is height balanced, so return 0 (height of a null tree)
    if root == None:
        return 0

    # Check if the left subtree is height balanced. If it is, then return its height to the node 'root', else
    # return -1
    left_height = check_balance(root.left)
    if left_height == -1:
        return -1

    # Check if the right subtree is height balanced. If it is, then return its height to the node 'root', else
    # return -1
    right_height = check_balance(root.right)
    if right_height == -1:
        return -1

    # Finally, check if the tree is balanced at the starting root node itself by checking the absolute difference between heights
    # of left and right sub-trees.
    if abs(left_height - right_height) > 1:
        return -1

    # If it is, then return 1 + the greater of the two heights (we're only interested in the side that we traversed down,
    # hence we determine which side has a greater value which infers that that is the side that we traversed down).
    return(1 + max(left_height, right_height))
