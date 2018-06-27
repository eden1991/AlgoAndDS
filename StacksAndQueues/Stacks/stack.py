from AlgoAndDS.StacksAndQueues.Stacks.node import Node


class Stack:

    def __init__(self):
        self.top = None
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def push(self, item):

        # Create a new node out of the item passed in
        temp = Node(item)

        # Point the new node to the top item in the stack
        temp.setNext(self.top)

        # Assign the new temp item as the top item of the stack (the previous top item
        # is already pointing to the next item in the stack)
        self.top = temp
        self.stack_size += 1

    def pop(self):
        item = None

        # If the stack isn't empty
        if self.top is not None:
            # Store the top item
            item = self.top
            # and use it to retrieve and assign the next item in the stack to the head of the stack
            self.top = self.top.getNext()

        self.stack_size -= 1
        return item

    def peek(self):
        # Just return the data of the top item
        if self.top:
            return self.top.getData()
        else:
            return None

    def size(self):
        return self.stack_size

    # Very useful for visually confirming the positioning of nodes as a sanity check
    def print_nodes(self):
        current = self.top

        while current is not None:
            print(current.getData(), end=' ')
            current = current.getNext()

    def search_for_node(self, target):
        current = self.top
        found = 0

        while current is not None:
            if current.getData() == target:
                found += 1
                break

        return found

