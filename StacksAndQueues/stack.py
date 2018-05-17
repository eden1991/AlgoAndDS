#!/usr/bin/env python3
from node import Node


class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, item):
        temp = Node(item)
        temp.setNext(self.top)
        self.top = temp

    def pop(self):
        if self.top is not None:
            item = self.top.getData()
            self.top = self.top.getNext()
            return item

        return None

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
    def findMin(self):
        min = self.top.getData()
        current = self.top.getNext()

        while current is not None:
            if current.getData() < min:
                min = current.getData()

            current = current.getNext()

        return min
