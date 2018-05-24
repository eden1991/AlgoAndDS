#!/usr/bin/env python3
from StacksAndQueues.Stacks.node import Node


class Stack:

    def __init__(self):
        self.top = None

        # Added for setOfStacks solution - 3.3
        self.next = None
        self.previous = None

    def is_empty(self):
        return self.top is None

    def push(self, item):

        # Create a new node out of the item passed in
        temp = Node(item)

        # Point the new node to the top item in the stack
        temp.setNext(self.top)

        # Assign the new temp item as the top item of the stack (the previous top item
        # is already pointing to the next item in the stack)
        self.top = temp

    def pop(self):
        item = None

        # If the stack isn't empty
        if self.top is not None:
            # Store the top item
            item = self.top
            # and use it to retrieve and assign the next item in the stack to the head of the stack
            self.top = self.top.getNext()

        return item

    def peek(self):
        # Just return the data of the top item
        return self.top.getData()

    def size(self):
        current = self.top
        count = 0

        # Keep iterating through the stack and increment the count per iteration
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    '''
    3.2
    '''
    def find_min(self):
        # Store the top node data initially
        min_element = self.top.getData()
        # We've already accounted for the data in the top node, so set current as the next node
        current = self.top.getNext()

        # Iterate through and compare the node data with min_element each time, and store the current node
        # data in to min_element if it is less than min_element.
        while current is not None:
            if current.getData() < min_element:
                min_element = current.getData()

            current = current.getNext()

        return min_element

    '''
    3.3
    
    # Some getters and setters for connecting and enabling backward and forward navigation among stacks for solution 3.3
    '''
    def set_next(self, next_stack):
        self.next = next_stack

    def set_previous(self, previous_stack):
        self.previous = previous_stack

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    # Very useful for visually confirming the positioning of nodes as a sanity check
    def print_nodes(self):
        current = self.top

        while current is not None:
            print(current.getData())
            current = current.getNext()

    def search_for_node(self, target):
        current = self.top
        found = 0

        while current is not None:
            if current.getData() == target:
                found += 1
                break

        return found

