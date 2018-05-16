#!/usr/bin/env python
from stack import Stack
import unittest


class TestStackMethods(unittest.TestCase):

    def stack_tests(self):
        myStack = Stack()
        numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
        for number in numbers:
            myStack.push(number)

        self.assertEqual(myStack.peek(), 8)


if __name__ == '__main__':
    # unittest.main()
    print("I got here")