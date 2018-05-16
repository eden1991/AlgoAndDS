#!/usr/bin/env python3
from AlgoAndDS.LinkedLists.node import Node


class EdenStack:

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


