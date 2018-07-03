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
        new_animal = Animal(type, breed)

        if not self.head:
            self.head = new_animal
        elif not self.tail:
            self.head.set_next(new_animal)
            self.tail = new_animal
            self.tail.set_previous(self.head)
        else:
            self.tail.set_next(new_animal)
            new_animal.set_previous(self.tail)
            self.tail = new_animal

        self.size += 1

    def get_tail(self):
        return self.tail

    def inspect_tail(self):
        if self.tail:
            return self.tail.get_data()
        else:
            return self.tail

    def enqueue_from_end(self, type, breed):
        new_animal = Animal(type, breed)

        if self.tail:
            new_animal.set_previous(self.tail)
            self.tail.set_next(new_animal)
            self.tail = new_animal
        elif not self.head:
            self.head = new_animal
        else:
            self.tail = new_animal
        self.size += 1

    def dequeue_any(self):
        dequeued = None

        if self.tail:
            dequeued = self.tail
            self.tail = self.tail.get_previous()
            self.size -= 1

        return dequeued

    def dequeue_specific(self, type):
        temp = Stack()

        while self.inspect_tail()[0] != type:
            temp.push(self.dequeue_any())

        dequeued = self.dequeue_any()

        while temp.size() > 0:
            new_animal = temp.pop().getData()
            self.enqueue_from_end(new_animal.get_data()[0], new_animal.get_data()[1])

        self.size -= 1
        return dequeued

