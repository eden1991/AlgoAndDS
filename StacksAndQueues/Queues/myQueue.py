from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack

'''
3.5 Implement a MyQueue class which implements a queue using two stacks.
'''

class MyQueue:

    def __init__(self):
        self.main = Stack()
        self.temp = Stack()

    def put(self, data):
        while not self.main.is_empty():
            self.temp.push(self.main.pop().getData())

        self.main.push(data)

        while not self.temp.is_empty():
            self.main.push(self.temp.pop().getData())

    def get(self):
        return self.main.pop()

    def size(self):
        return self.main.size()

    def is_empty(self):
        return self.main.is_empty()