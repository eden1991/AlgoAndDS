#!/usr/bin/env python3
from algo_and_ds.LinkedLists.node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def print_list(self):
        current = self.head

        while current != None:
            print(current.getData())
            current = current.getNext()

    # Returns a list of duplicate node items
    def find_duplicates(self):
        current = self.head
        duplicates = {}
        nonduplicates = []
        # Build up a dictionary of the node data from the
        # linked list and store the count of their occurrences
        # as their values
        while current is not None:
            if current.getData() in duplicates:
                duplicates[current.getData()] += 1
            else:
                duplicates[current.getData()] = 1

            current = current.getNext()

        # Filter out the node data which are not duplicates and store
        # in a list to be returned
        for item in duplicates:

            if duplicates[item] == 1:
                nonduplicates.append(item)

        for dup in nonduplicates:
            del duplicates[dup]

        return duplicates
