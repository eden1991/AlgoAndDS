from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack

# class Stack():
#     def __init__(self):
#         pass

class StackFindMin(Stack):
    # def __init__(self, top, stack_size):
    def __init__(self):
        # Stack.__init__(self, top, stack_size)
        self.top = None
        self.stack_size = 0


    def find_min(self):
        # Store the top node data initially
        min_element = self.top.getData()
        # We've already accounted for the data in the top node, so set current as the next node
        current = self.top.getNext()

        # Iterate through and compare the node data with min_element each time, and store the current node
        # data in to min_element if it is less than min_element.
        while current is not None:
            if current.getData() < min_element:
                min_element = current.getData()

            current = current.getNext()

        return min_element

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

    my_stack = StackFindMin()

    for number in numbers:
        my_stack.push(number)

    print(my_stack.find_min() == 1)