from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack
from AlgoAndDS.StacksAndQueues.Queues.animal import Animal

'''
3.7 An animal shelter holds only dogs and cats, and oeprates on a strictly "first in, first out" basis.
    People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
    can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
    They cannot select which specific animal they would like. Create the data structures to maintain this 
    system and implement oeprations such as enqueue, dequeueAny, dequeueDog and dequeueCat. You may use
    the built-in LinkedList data structure.  
'''

class Shelter():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, type, breed):
        # Initialise new animal
        new_animal = Animal(type, breed)

        # If there is no head, store the new animal in to the head
        if not self.head:
            self.head = new_animal
        # Else, if there is no tail, then store the new animal in to the tail
        elif self.head and not self.tail:
            # Point the head to the new animal
            self.head.set_next(new_animal)
            # Store the new animal in to the tail
            self.tail = new_animal
            # Point the tail to the head for backward traversal
            self.tail.set_previous(self.head)
        else:
            # Point the current tail (soon to be previous tail) to the new animal
            self.tail.set_next(new_animal)
            # Point the new animal to the current tail
            new_animal.set_previous(self.tail)
            # Set the new animal as the new tail
            self.tail = new_animal

        self.size += 1

    def inspect_tail(self):
        # Call the .get_data method on the tail only if there is something in the tail
        if self.tail:
            return self.tail.get_data()
        elif self.head:
            return self.head.get_data()
        else:
            # Otherwise, essentially just return None
            return self.tail

    def dequeue_any(self):
        # Initialise dequeued with None in case the function is called on an empty Shelter
        dequeued = None

        # If the tail contains a node
        if self.tail:
            # Store the tail in dequeued
            dequeued = self.tail
            # Set the tail to the animal previous to the tail
            if self.size > 2:
                self.tail = dequeued.get_previous()
            else:
                self.tail = None
            # if self.tail:
            #     self.tail.set_next(None)
            # Decrement the shelter size
            self.size -= 1
        elif self.head:
            dequeued = self.head
            dequeued.set_next(None)
            self.head = None
            self.size -= 1

        return dequeued

    def dequeue_specific(self, type):
        # Initialise a temporary stack to hold the animals that are dequeued whilst searching for the specific animal
        # type
        temp = Stack()

        # Continually dequeue animals and push them in to the aforementioned Stack until the intended type of animal
        # is encountered
        while self.inspect_tail()[0] != type:
            temp.push(self.dequeue_any())

        dequeued = self.dequeue_any()

        # Now pop all the animals from temp and enqueue back in to the Shelter
        while temp.size() > 0:
            new_animal = temp.pop().getData()
            self.enqueue(new_animal.get_data()[0], new_animal.get_data()[1])

        self.size -= 1
        return dequeued

