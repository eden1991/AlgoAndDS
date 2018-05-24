#!/usr/bin/env python3
from StacksAndQueues.Stacks.stack import Stack

'''
3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
should be composed of several stacks, and should create a new stack once
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
behave identically to a single stack (that is, pop() should return the same values as it
would if there were just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific
sub-stack.
'''


class SetOfStacks:

    def __init__(self, max_size):
        # Initial the new set with a stack by default
        self.head_stack = Stack()
        # Store the passed in max_size parameter in order to be bale to check and maintain that
        # stacks do not grow excessively and topple over.
        self.max_size = max_size

    def push(self, item):
        current = self.head_stack

        # Get down to the end stack
        while current.get_next() is not None:
            current = current.get_next()

        # Add a new stack to the set if the end one is full
        if current.size() == self.max_size:
            new_stack = Stack()
            current.set_next(new_stack)
            new_stack.set_previous(current)
            current = current.get_next()

        # Push the new node in to the last stack of the set
        current.push(item)

    def peek(self):
        current = self.head_stack

        # Get down to the end stack
        while current.get_next() is not None:
            current = current.get_next()

        return current.peek()

    def pop(self):
        current = self.head_stack

        while current.get_next() is not None:
            current = current.get_next()

        popped = current.pop()

        # Remove the last stack if it is empty
        if current.size() == 0:
            if current.get_previous() is not None:
                previous = current.get_previous()
                previous.set_next(None)
            current.set_previous(None)

        return popped

    def set_size(self):
        current = self.head_stack
        # A variable to keep count of the number of stacks in the set
        stack_count = 0
        # A list to store a count of the number of node items within each stack
        items_per_stack_count = []
        # A variable to keep a sum of the overall number of node items in the set
        total_items_count = 0

        while current is not None:
            stack_count += 1
            items_per_stack_count.append(current.size())
            total_items_count += current.size()
            current = current.get_next()

        return stack_count, items_per_stack_count, total_items_count

    def is_set_empty(self):
        # The set is empty if the head stack size is 0 and there is no following stack
        return self.head_stack.size() == 0 and self.head_stack.get_next() is None

    # Iterates through the set and uses the stack method print_nodes() to print all nodes in the set
    def list_set_node_items(self):
        current_stack = self.head_stack
        stack_number = 0

        while current_stack is not None:
            current_stack.print_nodes()
            print("--- end stack " + str(stack_number) + " ---")
            stack_number += 1
            current_stack = current_stack.get_next()

    '''
    FOLLOW UP
    Implement a function popAt(int index) which performs a pop operation on a specific
    sub-stack.
    '''
    def pop_at(self, index):
        current_stack = self.head_stack
        num_nodes_ahead = 0
        temp = Stack()

        # Determine which stack the node resides in
        sub_stack = index // self.max_size

        # If the index doesn't reside in the first stack, then move to the specific stack.
        # Also, remove the number of positions that must be iterated through by deducting
        # the positions from earlier stacks
        if sub_stack > 0:
            for stack in range(0, sub_stack):
                current_stack = current_stack.get_next()

            # Now that we are operating on a specific stack only, get the index of the node item
            # with respect to where it sits in this stack
            particular_stack_index = index - self.max_size

            # Also calculate and capture the number of nodes ahead of the particular index
            # Note that we deduct a further 1 due to indexes starting at 0
            num_nodes_ahead = current_stack.size() - particular_stack_index - 1

        # Pop all the items ahead of the index and push them in to a temporary stack
        for indice in range(0, num_nodes_ahead):
            temp.push(current_stack.pop().getData())

        # Pop the top node out of the current stack which is the node item at 'index'
        popped_node = current_stack.pop()

        # Push everything back in to the current stack from temp
        while temp.is_empty() is False:
            current_stack.push(temp.pop().getData())

        # Shuffle all node items up the set by one to fill the gap left by popping earlier
        while current_stack.get_next() is not None:
            current_stack.push(current_stack.get_next().pop().getData())
            current_stack = current_stack.get_next()

        return popped_node
