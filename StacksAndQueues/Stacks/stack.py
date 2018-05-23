#!/usr/bin/env python3
from AlgoAndDS.StacksAndQueues.Stacks.node import Node


class Stack:

    def __init__(self):
        self.top = None

        # Added for setOfStacks solution - 3.3
        self.next = None
        self.previous = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        temp = Node(item)
        temp.setNext(self.top)
        self.top = temp

    def pop(self):
        item = None

        if self.top is not None:
            item = self.top
            self.top = self.top.getNext()
            return item

        return item

    def peek(self):
        return self.top.getData()

    def size(self):
        current = self.top
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    '''
    3.2
    '''
    def find_min(self):
        min_element = self.top.getData()
        current = self.top.getNext()

        while current is not None:
            if current.getData() < min_element:
                min_element = current.getData()

            current = current.getNext()

        return min_element

    '''
    3.3
    '''
    def set_next(self, next_stack):
        self.next = next_stack

    def set_previous(self, previous_stack):
        self.previous = previous_stack

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

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

