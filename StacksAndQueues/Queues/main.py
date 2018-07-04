#!/usr/bin/env python3
import unittest
from AlgoAndDS.StacksAndQueues.Queues.myQueue import MyQueue
from AlgoAndDS.StacksAndQueues.Queues.shelter import Shelter
from AlgoAndDS.StacksAndQueues.Queues.animal import Animal

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

    '''
    3.7 An animal shelter holds only dogs and cats, and oeprates on a strictly "first in, first out" basis.
        People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
        can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
        They cannot select which specific animal they would like. Create the data structures to maintain this 
        system and implement oeprations such as enqueue, dequeueAny, dequeueDog and dequeueCat. You may use
        the built-in LinkedList data structure.  
    '''
    def test_shelter_enqueue(self):
        my_sheler = Shelter()
        my_sheler.enqueue("Cat", "Sphynx Cat")
        my_sheler.enqueue("Dog", "Chihuahua")

        # Test that we can access both the head and the detail
        self.assertEqual(my_sheler.head.get_data()[0], "Cat")
        self.assertEqual(my_sheler.tail.get_data()[0], "Dog")

        my_sheler.enqueue("Cat", "Tabby")
        my_sheler.enqueue("Dog", "Schitsu")

        # Test that the tail has been updated
        self.assertEqual(my_sheler.tail.get_data()[1], "Schitsu")

        # Test that we can traverse through by accessing the animal that is previous to the tail animal
        self.assertEqual(my_sheler.tail.get_previous().get_data()[1], "Tabby")

        # Traverse right back to the beginning and test that we can access the animal at the head
        current_animal = my_sheler.tail
        while current_animal.get_previous():
            current_animal = current_animal.get_previous()

        self.assertEqual(current_animal.get_data()[0], "Cat")

        # Test that the shelter size is 4
        self.assertEqual(my_sheler.size, 4)

    def test_shelter_inspect_tail(self):
        my_sheler = Shelter()
        my_sheler.enqueue("Cat", "Persian Cat")
        my_sheler.enqueue("Dog", "Bulldog")

        # Test that the inspect_tail method returns Bulldog
        self.assertEqual(my_sheler.inspect_tail()[1], "Bulldog")

    def test_shelter_dequeue_any(self):
        my_sheler = Shelter()

        my_sheler.enqueue("Cat", "Maine Coon")
        my_sheler.enqueue("Dog", "Poodle")

        # Test that the dequeue_any method returns Poodle
        self.assertEqual(my_sheler.dequeue_any().get_data()[1], "Poodle")

        # Test that the dequeue_any method now returns Maine Coon
        self.assertEqual(my_sheler.dequeue_any().get_data()[1], "Maine Coon")

        # Test that the shelter size is now 0
        self.assertEqual(my_sheler.size, 0)

        # Now that the Shelter is empty, test that the dequeue_any method now returns None
        self.assertEqual(my_sheler.dequeue_any(), None)

    def test_shelter_dequeue_specific_dog(self):
        my_sheler = Shelter()
        my_sheler.enqueue("Dog", "Yorkshrie Terrir")
        my_sheler.enqueue("Cat", "Maine Coon")
        my_sheler.enqueue("Cat", "Persian Cat")
        my_sheler.enqueue("Cat", "Burmese")

        # Test that we dequeue a Dog given a person has opted for one over a cat
        self.assertEqual(my_sheler.dequeue_specific("Dog").get_data()[0], "Dog")

    def test_shelter_dequeue_specific_cat(self):
        my_sheler = Shelter()
        my_sheler.enqueue("Cat", "Bengal Cat")
        my_sheler.enqueue("Dog", "French Bulldog")
        my_sheler.enqueue("Dog", "Great Dane")
        my_sheler.enqueue("Dog", "Pit Bull")

        # Test that we dequeue a Cat given a person has opted for one over a dog
        self.assertEqual(my_sheler.dequeue_specific("Cat").get_data()[0], "Cat")


if __name__ == '__main__':
    unittest.main()