#!/usr/bin/env python3
from AlgoAndDS.LinkedLists.node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        # The code below will cause this method to add
        # nodes in from the head of the list
        # temp = Node(item)
        # temp.setNext(self.head)
        # self.head = temp

        current = self.head
        previous = None
        newNode = Node(item)

        if self.head is None:
            self.head = newNode
        else:
            while current is not None:
                previous = current
                current = current.getNext()
            previous.setNext(newNode)


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

    # This method has been implemented to enable test cases
    def find_duplicates(self):
        current = self.head
        duplicates = {}

        # Build up a dictionary of the node data from the
        # linked list and store the count of their occurrences
        # as their values
        while current is not None:
            if current.getData() in duplicates:
                duplicates[current.getData()] += 1
            else:
                duplicates[current.getData()] = 1

            current = current.getNext()

        return duplicates

    '''
    2.1 | Write code to remove duplicates from an unsorted linked list.
    '''
    # FOLLOW UP
    # How would you solve this problem if a temporary buffer is not allowed?
    def remove_duplicates(self):
        # We set the holder variable to start at the head, and current to be the next node
        # so that we are never comparing the same node but rather the holder is compared to
        # every other node in the linkedlist as they are passed in to the current variable
        holder = self.head

        while holder is not None:
            current = holder.getNext()
            while current is not None:
                # If another occurrence of holder is found in the linked list, then remove it
                if holder.getData() == current.getData():
                    self.remove(current.getData())
                current = current.getNext()
            '''
            Currently, the remove method will remove the first occurrence of
            a node that it finds, which will cause it to remove all occurrences
            of a node if they are all in succession. So here we check if this has
            happened, and add the node back in if all occurrences have been removed.

            The ideal situation here would be to re-write the remove method to take in
            a node object rather than just the data and creating a new node inside the
            remove method.
            '''
            if self.search(holder.getData()) is False:
                self.add(holder.getData())
            holder = holder.getNext()

    '''
    2.2 | Implement an algorithm to find the nth to last element of a singly linked list
    '''
    def findFromNth(self, n):
        current = self.head

        # If the value passed in is greater than the size of the linkedlist, assign None
        if n > self.size():
            current = Node(None)

        # If the value passed in is between index 0 and the .size-1, then we can proceed
        # to find and return the node at the starting index which will hence allow to iterate
        # through to the last node
        if n >= 0 and n < self.size():
            for counter in range(0, n):
                current = current.getNext()

        return current

    '''
    2.6 | Given a circular linked list, implement an algorithm which returns node at the beginning
    of the loop.
    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an
    earlier node, so as to make a loop in the linked list.
    EXAMPLE
    input: A -> B -> C -> D -> E -> C [the same C as earlier]
    output: C
    '''
    # Assume that all elements in the list are unique
    def find_loop_head(self):
        current = self.head
        nodeCounter = {}

        # Iterate through the linkedlist and append a count for every node that has
        # a pointer to it
        while current is not None:
            if current.getNext().getData() in nodeCounter:
                nodeCounter[current.getNext().getData()] += 1
            else:
                nodeCounter[current.getNext().getData()] = 1

            # Break out once we establish that there is an endless loop.
            # This is indicating by surfacing that a single node has 2 counters pointing to it
            if nodeCounter[current.getNext().getData()] >= 2:
                break

            current = current.getNext()

        # After breaking out of the above while loop, return the node at the head of the endless loop
        return current.getNext().getData()

    def change_next(self, origin, dest):
        current = self.head
        end = self.head

        # Iterate through the list until we get to the origin node that
        # we want to be the culprit that initiates the loop
        while current.getData() != origin:
            current = current.getNext()

        # Iterate through the list until we get to the dest node that will be
        # the node that is situated at the head of the loop
        while end.getData() != dest:
            end = end.getNext()

        # Set the current (origin) node to point to some node which will invoke
        # an endless loop
        current.set_next(end)