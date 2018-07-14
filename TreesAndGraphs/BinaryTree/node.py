#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print method
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    # Binary search tree method
    def search(self, lookup_value):
        if lookup_value < self.data:
            if not self.left:
                return(False)
            else:
                return self.left.search(lookup_value)
        elif lookup_value > self.data:
            if not self.right:
                return(False)
            else:
                return self.right.search(lookup_value)
        else:
            return(True)

    # In-order Traversal method
    # Left -> Root -> Right
    def in_order_traversal(self, root):
        traversed_result = []
        if root:
            traversed_result = traversed_result + self.in_order_traversal(root.left)
            print("Left:", traversed_result)
            traversed_result.append(root.data)
            traversed_result = traversed_result + self.in_order_traversal(root.right)
            print("Right:", traversed_result)
        return traversed_result

    # Pre-order Traversal method
    # Root -> Left -> Right
    def pre_order_traversal(self, root):
        traversed_result = []
        if root:
            traversed_result.append(root.data)
            traversed_result = traversed_result + self.pre_order_traversal(root.left)
            traversed_result = traversed_result + self.pre_order_traversal(root.right)

        return traversed_result

    # Post-order Traversal method
    # Left -> Right -> Root
    def post_order_traversal(self, root):
        traversed_result = []
        if root:
            traversed_result = traversed_result + self.post_order_traversal(root.left)
            traversed_result = traversed_result + self.post_order_traversal(root.right)
            traversed_result.append(root.data)

        return traversed_result

if __name__ == '__main__':
    # root = Node(12)
    # root.insert(6)
    # root.insert(14)
    # root.insert(3)
    # print(root.search(7))
    # print(root.search(12))
    # root.print_tree()
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.in_order_traversal(root))
    # print(root.pre_order_traversal(root))
    # print(root.post_order_traversal(root))