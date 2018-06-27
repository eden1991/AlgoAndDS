from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack
from AlgoAndDS.LinkedLists.unorderedList import UnorderedList

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

See stackFindMin.py
'''


class SetOfStacks:

    def __init__(self, max_size):
        # Store the passed in max_size parameter in order to be able to check and maintain that
        # stacks do not grow excessively and topple over.
        self.max_size = max_size
        self.stack_set = UnorderedList()
        # Keep track of the total number of stacks in the set
        self.stack_count = 0
        # Keep track of the total number of node items in the set
        self.items_count = 0
        # Append a stack to the set for initialisation
        self.append_stack()

    def push(self, item):
        # Add a new stack to the set if the end one is full
        if self.tail_stack.size() == self.max_size:
            self.append_stack()

        # Push the new node in to the last stack of the set and increment the items count
        self.items_count += 1
        self.tail_stack.push(item)

    def peek(self):
        return self.tail_stack.peek()

    def pop(self):
        popped = self.tail_stack.pop()

        # Remove the last stack if it is empty
        if self.tail_stack.is_empty():
            self.stack_set.remove(self.tail_stack)

            current = self.stack_set.head
            while current.getNext() is not None:
                current = current.getNext()
            self.tail_stack = current
            self.stack_count -= 1

        self.items_count -= 1
        return popped

    def set_size(self):
         # return stack_count, total_items_count
        return self.stack_count, self.items_count

    def is_set_empty(self):
        # The set is empty if the head stack size is 0 and there is no following stack
        return self.stack_count == 0

    def append_stack(self):
        self.tail_stack = Stack()
        self.stack_set.add(self.tail_stack)
        self.stack_count += 1

    # Iterates through the set and uses the stack method print_nodes() to print all nodes in the set
    def list_set_node_items(self):
        current_stack = self.head_stack
        stack_number = 0

        while current_stack is not None:
            current_stack.print_nodes()
            print("--- end stack " + str(stack_number) + " ---")
            stack_number += 1
            current_stack = current_stack.get_next()

