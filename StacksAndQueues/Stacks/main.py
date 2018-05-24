#!/usr/bin/env python3
from StacksAndQueues.Stacks.stack import Stack
from StacksAndQueues.Stacks.setOfStacks import SetOfStacks
import unittest
import gc


class TestStackMethods(unittest.TestCase):

    '''
    Test general stack functionality
    '''
    def test_stack(self):
        my_stack = Stack()
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        # Push all the numbers in the numbers list in to my_stack
        for number in numbers:
            my_stack.push(number)

        # The stack shouldn't be empty
        self.assertFalse(my_stack.is_empty())

        # The element at the head of the stack should be 8
        self.assertEqual(my_stack.peek(), 8)

        # Pop 6 elements out
        last_element = None
        for number in range(0, 6):
            last_element = my_stack.pop()

        # The last element popped out should be 3
        self.assertEqual(last_element.getData(), 3)

        # The element at the head of the stack should be 2
        self.assertEqual(my_stack.peek(), 2)

        # Empty the stack
        for number in range(0, my_stack.size()):
            my_stack.pop()

        # The stack should now be empty
        self.assertTrue(my_stack.is_empty())

    ''' 
    3.1 Describe how you could use a single array to implement three stacks.

    Approach: Have an array of size 3 and nest another array at each indice.
    You can then operate on these nested arrays.
    '''
    def test_singleArray_three_stacks(self):
        wardrobe = list()
        shoes = list()
        shirts = list()
        bags = list()

        wardrobe.append(shoes)
        wardrobe.append(shirts)
        wardrobe.append(bags)

        # There should be 3 empty lists nested inside of the wardrobe list
        self.assertEqual(wardrobe, [[], [], []])

        # Add some items in for verifying
        wardrobe[0].append("Nike")
        wardrobe[0].append("Adidas")
        wardrobe[1].append("Ralph Polo")
        wardrobe[1].append("Lacoste")
        wardrobe[1].append("Tom Ford")
        wardrobe[2].append("Country Road")

        # Now check that those items exist
        self.assertEqual(wardrobe[0][0], "Nike")
        self.assertEqual(wardrobe[1][0], "Ralph Polo")
        self.assertEqual(wardrobe[2][0], "Country Road")

        # Let's see that we can remove items from the head of each stack
        popped_shoe = wardrobe[0].pop()

        # The item that we just popped should be Adidas
        self.assertEqual(popped_shoe, "Adidas")
        # The item at the head of the stack should be Nike
        self.assertEqual(wardrobe[0][0], "Nike")
        # Check that the shoes stack is empty after popping the last item
        wardrobe[0].pop()
        self.assertEqual(len(wardrobe[0]), 0)

    '''
    3.2 How would you design a stack which, in addition to push and pop, also has a function
    min which returns the minimum element? Push, pop and min should all operate in
    O(1) time.
    '''
    def test_min(self):
        numbers_stack = Stack()
        numbers = [4, 2, 3, 1, 5, 6, 7, 8]
        # push all the numbers in the numbers list in to numbersStack
        for number in numbers:
            numbers_stack.push(number)

        self.assertEqual(numbers_stack.find_min(), 1)

    '''
    3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
    in real life, we would likely start a new stack when the previous stack exceeds
    some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
    should be composed of several stacks, and should create a new stack once
    the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
    behave identically to a single stack (that is, pop() should return the same values as it
    would if there were just a single stack).

    FOLLOW UP - Scroll down and see below.
    '''
    def test_set_of_stacks(self):
        new_set = SetOfStacks(10)
        # Let's make sure that we have initialised with a maximum stack limit of 10
        self.assertEqual(new_set.max_size, 10)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        bank_of_numbers = [15, 16, 17, 18, 19, 20, 21, 22, 23]

        # Only push the numbers list in for now which is a total of 14 numbers
        for number in numbers:
            new_set.push(number)

        # Test that the item at the head of the set is 14
        self.assertEqual(new_set.peek(), 14)

        # new_set.list_set_node_items()
        # Test that the set is composed of 2 stacks, with 10 numbers in the head stack, and 4 in the next stack
        self.assertEqual(new_set.set_size()[0], 2)
        self.assertEqual(new_set.set_size()[1][0], 10)
        self.assertEqual(new_set.set_size()[1][1], 4)

        # Test that popping a node from the set will pop the item at the head of the set of stacks which is 14
        self.assertEqual(new_set.pop().getData(), 14)

        # Now test that the set is still composed of 2 stacks, with 10 numbers in the head stack, and 3 in the next
        # stack (13 nodes all-up)
        self.assertEqual(new_set.set_size()[0], 2)
        self.assertEqual(new_set.set_size()[1][0], 10)
        self.assertEqual(new_set.set_size()[1][1], 3)

        # Now let's test that we keep adding additional stacks to the set as we continually hit the maximum stack
        # limit of 10 per stack
        for number in bank_of_numbers:
            new_set.push(number)

        # Check that the size of the set has grown to 3 stacks, with 10 numbers in the first two stacks, and 2 in
        # the third (22 nodes all-up)
        self.assertEqual(new_set.set_size()[0], 3)
        self.assertEqual(new_set.set_size()[1][0], 10)
        self.assertEqual(new_set.set_size()[1][1], 10)
        self.assertEqual(new_set.set_size()[1][2], 2)

        # Now let's test that we can pop all values from the last stack in the set, and that we dispose of the empty
        # stack from the set.
        for count in range(0, 2):
            new_set.pop()

        # Check that the size of the set has reduced to 2 stacks, with 10 numbers in both stacks (20 nodes all-up)
        self.assertEqual(new_set.set_size()[0], 2)
        self.assertEqual(new_set.set_size()[1][0], 10)
        self.assertEqual(new_set.set_size()[1][1], 10)
        # And test that the third stack has been disposed of programmatically
        self.assertEqual(new_set.head_stack.get_next().get_next(), None)

        # Let's also test that we can completely clear out the set
        while new_set.is_set_empty() is False:
            new_set.pop()

        # Test that the set is empty
        self.assertTrue(new_set.is_set_empty())

        '''
        FOLLOW UP
        Implement a function popAt(int index) which performs a pop operation on a specific
        sub-stack.
        '''
        # Initialise a new set of stacks
        some_set = SetOfStacks(5)
        bunch_of_nums = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

        # Make sure that we have initialised with a maximum stack limit of 5
        self.assertEqual(some_set.max_size, 5)
        #
        for num in bunch_of_nums:
            some_set.push(num)

        # Test that some_set contains 10 values
        self.assertEqual(some_set.set_size()[2], 10)

        # Visually confirm the sequence of nodes in the Set
        # print("Initial stack contents:")
        # some_set.list_set_node_items()

        # Pop the node at index 6, we expect the popped node to be 2
        self.assertEqual(some_set.pop_at(6).getData(), 2)

        # print("Stack contents after popping node at index 6:")
        # some_set.list_set_node_items()
        # Now pop the node at index 1, we expect the popped node to be 7
        self.assertEqual(some_set.pop_at(7).getData(), 4)

        # Visually confirm the sequence of nodes in the Set again
        # some_set.list_set_node_items()

        # Pop the node at index 0, we expect the popped node to be 10
        self.assertEqual(some_set.pop_at(0).getData(), 10)

        # print(some_set.set_size()[2])
        # some_set.list_set_node_items()
        # Pop the last node in the set, we expect the popped node to be 3
        self.assertEqual(some_set.pop_at(8).getData(), 3)

        '''
        The remaining nodes should be in the below sequence:
        index |node_item| index |node_item|
         4       |5|                | |
         3       |9|                | |
         2       |8|                | |
         1       |7|                | |
         0       |6|              5 |1|
        '''

        # Check that the top node in the first stack is 5 bi directly peeking at the stack
        self.assertEqual(some_set.head_stack.peek(), 5)
        # some_set.list_set_node_items()
        # Check that the top node in the second stack (and hence, the top of the set of stacks)
        # is 1.
        self.assertEqual(some_set.peek(), 1)


if __name__ == '__main__':
    unittest.main()
