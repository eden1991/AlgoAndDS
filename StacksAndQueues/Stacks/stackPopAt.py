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

        # If the index doesn't reside in the first stack (and hence there are more than one stack in
        # the set), then move to the specific stack. Also, remove the number of positions that must
        # be iterated through by deducting the positions from earlier stacks.
        if sub_stack > 0:
            for stack in range(0, sub_stack):
                current_stack = current_stack.getNext()

            # Now that we are operating on a specific stack only, get the index of the node item
            # with respect to where it sits in this stack.
            particular_stack_index = index - self.max_size
        else:
            particular_stack_index = index

        # Also calculate and capture the number of nodes ahead of the particular index.
        # Note that we deduct a further 1 due to indexes starting at 0.
        num_nodes_ahead = current_stack.getData().size() - particular_stack_index - 1

        # Pop all the items ahead of the index and push them in to a temporary stack
        for indice in range(0, num_nodes_ahead):
            temp.push(current_stack.getData().pop().getData())

        # Pop the top node out of the current stack which is the node item at 'index'
        popped_node = super().pop()

        # Push everything back in to the current stack from temp
        while temp.is_empty() is False:
            current_stack.getData().push(temp.pop().getData())

        # Shuffle all node items up the set by one to fill the gap left by popping earlier
        while current_stack.getNext() is not None:
            current_stack.getData().push(current_stack.getNext().getData().pop().getData())
            current_stack = current_stack.getNext()

        return popped_node

    def print_nodes(self):
        # self > UnorderedList() > Node() > Stack() > Node()
        current_stack = self.stack_set.head
        # current_stack = UnorderedList() > Node()
        current_node = current_stack.getData().top
        # current_stack = Node() > Stack() > Node()

        while current_stack is not None:
            while current_node is not None:
                print(current_node.getData())
                current_node = current_node.getNext()
            current_stack = current_stack.getNext()
            # print(current_stack.getData())
            # SetOfStacks() > UnorderedList() > Node() > Stack() > Node()

if __name__ == '__main__':
    da_stack = StackPopAt(4)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in numbers:
        da_stack.push(num)

    da_stack.print_nodes()