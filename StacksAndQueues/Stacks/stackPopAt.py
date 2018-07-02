from AlgoAndDS.StacksAndQueues.Stacks.setOfStacks import SetOfStacks
from AlgoAndDS.StacksAndQueues.Stacks.stack import Stack

'''
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific
sub-stack.
'''
class StackPopAt(SetOfStacks):
    def __init__(self, max_size):
        # Bring in the super class's variables
        super().__init__(max_size)
        self.max_size = max_size

    def pop_at(self, index):
        current_stack = self.stack_set.head
        temp = Stack()

        # Determine which stack the node resides in
        sub_stack = index // self.max_size
        # print("Sub-stack:", sub_stack)

        # If the index doesn't reside in the first stack (and hence there are more than one stack in
        # the set), then move to the specific stack. Also, remove the number of positions that must
        # be iterated through by deducting the positions from earlier stacks.
        if sub_stack > 0:
            counter = 0
            for stack in range(0, sub_stack):
                current_stack = current_stack.getNext()
                counter += 1
                # print("Shuffled to next stack")

            # current_node = current_stack.getData().top
            # while current_node is not None:
            #     print(current_node.getData())
            #     current_node = current_node.getNext()

            # Now that we are operating on a specific stack only, get the index of the node item
            # with respect to where it sits in this stack.
            # particular_stack_index = index - self.max_size - current_stack.getData().stack_size
            particular_stack_index = index - self.max_size * counter
            # print(particular_stack_index)
        else:
            particular_stack_index = index

        # Also calculate and capture the number of nodes ahead of the particular index.
        # Note that we deduct a further 1 due to indexes starting at 0.
        num_nodes_ahead = current_stack.getData().size() - particular_stack_index - 1 # <- This doesn't make sense

        # Pop all the items ahead of the index and push them in to a temporary stack
        for indice in range(0, num_nodes_ahead):
            temp.push(current_stack.getData().pop().getData())

        # Pop the top node out of the current stack which is the node item at 'index'
        popped_node = current_stack.getData().pop()
        self.items_count -= 1
        # popped_node = super().pop()

        # Store a reference to the current_stack as we will need to come back to it to push the nodes back in from temp.
        placeholder = current_stack
        # Shuffle all node items up the set by one to fill the gap left by popping earlier.
        # The point of doing this is to maintaian the order of all node items in the Set
        while current_stack.getNext() is not None:
            current_stack.getData().push(current_stack.getNext().getData().pop().getData())
            current_stack = current_stack.getNext()

        current_stack = placeholder
        # Push everything back in to the current stack from temp
        while temp.is_empty() is False:
            current_stack.getData().push(temp.pop().getData())

        while current_stack.getNext() is not None:
            current_stack = current_stack.getNext()

        if self.tail_stack.is_empty():
            self.stack_set.remove(self.tail_stack)

            current = self.stack_set.head
            while current.getNext() is not None:
                current = current.getNext()
            self.tail_stack = current
            self.stack_count -= 1

        return popped_node

    def print_nodes(self):
        current_stack = self.stack_set.head

        while current_stack is not None:
            current_node = current_stack.getData().top
            while current_node is not None:
                print(current_node.getData())
                current_node = current_node.getNext()
            current_stack = current_stack.getNext()


if __name__ == '__main__':
    da_stack = StackPopAt(4)
    numbers = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    for num in numbers:
        da_stack.push(num)

    # da_stack.print_nodes()
    # 4 8
    # 3 7
    # 2 6
    # 1 5
    # da_stack.print_nodes()
    # print("Popped:", da_stack.pop_at(0).getData())
    # print("Popped:", da_stack.pop_at(7).getData())
    # print("Popped:", da_stack.pop_at(1).getData())
    # print("Popped:", da_stack.pop_at(0).getData())
    # da_stack.print_nodes()
    # # print("Popped:", da_stack.pop_at(6).getData())
    # print("Popped:", da_stack.pop_at(9).getData())