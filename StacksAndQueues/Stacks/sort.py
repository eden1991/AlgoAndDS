#!/usr/bin/env python3

from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack

'''
3.6 Write a program to sort a stack in ascending order. You should not make any assumptions
about how the stack is implemented. The following are the only functions that
should be used to write this program: push | pop | peek | isEmpty.

See sort.py for solution code.
'''

def sort_stack(origin_stack):
    auxiliary = Stack()
    end_stack = Stack()
    end_stack.push(origin_stack.pop().getData())

    while origin_stack.is_empty() is False:
        # Store the data from the top node in origin_stack.
        temp_node_data = origin_stack.peek()
        # When temp_node_data no longer matches the data of the top node in origin_stack, then exit
        # and begin to evaluate the next node
        while origin_stack.peek() == temp_node_data:
            # If end_stack is empty, simply push in to it the top node from origin_stack
            if end_stack.is_empty():
                end_stack.push(origin_stack.pop().getData())
                break
            # If the top node in origin_stack is greater than the top_node in end_stack, push it over.
            # We are storing the data in descending order so that later we can easily transfer the nodes
            # back over to origin_stack in ascending order.
            elif origin_stack.peek() >= end_stack.peek():
                end_stack.push(origin_stack.pop().getData())
                break
            else:
                # Move the top node from end_stack out of the way by pushing it in to auxiliary so that
                # we can loop again and compare with the next node in auxiliary
                auxiliary.push(end_stack.pop().getData())

        # Now push all nodes from auxiliary back in to end_stack
        while auxiliary.is_empty() is False:
            end_stack.push(auxiliary.pop().getData())
        # print(end_stack.print_nodes())

    # Finally, push all nodes from end_stack in to origin_stack in ascending order
    while end_stack.is_empty() is False:
        origin_stack.push(end_stack.pop().getData())
    # print(origin_stack.print_nodes())



if __name__ == '__main__':
    myStack = Stack()
    myStack.push(5)
    myStack.push(5)
    myStack.push(1)
    myStack.push(3)
    myStack.push(3)
    myStack.push(2)
    myStack.push(4)
    sort_stack(myStack)
    print(myStack.print_nodes())