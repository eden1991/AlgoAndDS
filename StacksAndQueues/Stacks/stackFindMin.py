from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack

'''
3.2 How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.
'''

# We pass in an object of the parent class to the child
class StackFindMin(Stack):
    def __init__(self):
        # Bring in the super class's variables
        super(StackFindMin, self).__init__()
        # Use a regular stack to keep track of the history of minimal elements
        self._min_value = Stack()
        self._temp_stack = Stack()

    def push(self, item):
        # Call the parent class's push method
        super().push(item)

        # Continually compare item to the value at the top of min_value and append item
        # once the new element to the min_value stack if it is found to be smaller than what
        # is current at the top.
        self.set_min(item)

    def pop(self):
        # Call the parent class's pop method
        popped = super().pop()

        # Remove the node item value from the min_value stack if it happens to match
        # the minimum value currently residing at the top of the min_value stack.
        if popped.getData() == self._min_value.peek():
            self._min_value.pop()

        return popped

    # Getter for the current minimum value
    def get_min(self):
        return self._min_value.peek()

    # Setter for the current minimum value
    def set_min(self, data):
        if not self.get_min():
            self._min_value.push(data)
        else:
            while self.get_min() is not None and data > self.get_min():
                self._temp_stack.push(self._min_value.pop().getData())

            self._min_value.push(data)

            while self._temp_stack.peek() is not None:
                self._min_value.push(self._temp_stack.pop().getData())
