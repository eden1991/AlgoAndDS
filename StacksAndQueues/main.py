#!/usr/bin/env python3
from stack import Stack
import unittest


class TestStackMethods(unittest.TestCase):

    '''
    Test general stack functionality
    '''
    def test_stack(self):
        myStack = Stack()
        numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
        # Push all the numbers in the numbers list in to myStack
        for number in numbers:
            myStack.push(number)

        # The stack shouldn't be empty
        self.assertFalse(myStack.isEmpty())

        # The element at the head of the stack should be 8
        self.assertEqual(myStack.peek(), 8)

        # Pop 5 elements out
        for number in range(0, 5):
            myStack.pop()

        # The element at the head of the stack should be 3
        self.assertEqual(myStack.peek(), 3)

        # Empty the stack
        for number in range(0, myStack.size()):
            myStack.pop()

        # The stack should now be empty
        self.assertTrue(myStack.isEmpty())

    ''' 
    3.1 Describe how you could use a single array to implement three stacks.

    Approach: Have an array of size 3 and nest another array at each indice.
    You can then operate these nested arrays 
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
        poppedShoe = wardrobe[0].pop()

        # The item that we just popped should be Adidas
        self.assertEqual(poppedShoe, "Adidas")
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
        numbersStack = Stack()
        numbers = [ 4, 2, 3, 1, 5, 6, 7, 8 ]
        # push all the numbers in the numbers list in to numbersStack
        for number in numbers:
            numbersStack.push(number)

        self.assertEqual(numbersStack.findMin(), 1)



if __name__ == '__main__':
    unittest.main()