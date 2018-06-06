#!/usr/bin/env python3
import unittest
from AlgoAndDS.StacksAndQueues.Queues.myQueue import MyQueue

'''
3.5 Implement a MyQueue class which implements a queue using two stacks.
'''
class TestQueueMethods(unittest.TestCase):

    def test_queue(self):
        myQueue = MyQueue()
        items = [1, 2, 'car', 10, 45, 'Chevy']

        for item in items:
            myQueue.put(item)

        # We should have 6 items in myQueue
        self.assertEquals(6, myQueue.size())

        # Calling 'get' should return (and remove) the item at the front of myQueue which should be 1
        self.assertEquals(1, myQueue.get().getData())

        # The size of myQueue should now be 5
        self.assertEquals(5, myQueue.size())

        # Putting an item in should send it to the end.
        myQueue.put("box")
        # Let's check that the last item in myQueue is 'box'
        for count in range(0, myQueue.size()-1):
            myQueue.get()
        # We should now only have the one item remaining in myQueue
        self.assertEquals(1, myQueue.size())
        # And that item should be 'box'
        self.assertEquals('box', myQueue.get().getData())

        # myQueue should now be empty
        self.assertEquals(True, myQueue.is_empty())


if __name__ == '__main__':
    unittest.main()