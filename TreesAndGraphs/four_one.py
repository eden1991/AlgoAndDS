'''
4.1 Implement a function to check if a binary tree is balanced. For the purposes of this
    question, a balanced tree is defined to be a tree such that the heights of the two
    subtrees of any node never differ by more than one.
'''

def traverse_left(root):
    # A list to act as a physical counter to store a  series of 1's that represent each level of traversal through
    # a subtree
    left_depth = [0]

    if root:
        # If the root variable contains a node, then recurse on the left side
        left_depth = left_depth + traverse_left(root.left)
        # And add to the left_depth counter
        left_depth[0] += 1

    return left_depth

def traverse_right(root):
    right_depth = [0]

    if root:
        right_depth = right_depth + traverse_right(root.right)
        right_depth[0] += 1

    return right_depth

def is_balanced(root):
    # Store the length of the lists passed in from the traverse_ functions above
    left_side = len(traverse_left(root))
    right_side = len(traverse_right(root))

    # Work out which length is larger and deduct from the smaller length
    if left_side > right_side:
        difference = left_side - right_side
    else:
        difference = right_side - left_side

    # Return True if the difference is no more than 1, which means the tree is balanced.
    # Else, return False for an unbalanced tree.
    return difference <= 1
