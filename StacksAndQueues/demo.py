#!/bin/usr/env python3

from edenStack import EdenStack

if __name__ == '__main__':
    print("I got here")
    myStack = EdenStack()
    numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
    print(myStack.isEmpty())
    for number in numbers:
        myStack.push(number)