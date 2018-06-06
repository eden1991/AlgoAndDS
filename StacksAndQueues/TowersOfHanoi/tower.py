from AlgoAndDS.StacksAndQueues.TowersOfHanoi.disk import Disk
# from disk import Disk


class Tower:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):

        # Create a new Disk out of the item passed in
        temp = Disk(item)

        # Point the new Disk to the top item in the stack
        temp.setNext(self.top)

        # Assign the new temp item as the top item of the stack (the previous top item
        # is already pointing to the next item in the stack)
        self.top = temp

    def pop(self):
        item = None

        # If the stack isn't empty
        if self.top is not None:
            # Store the top item
            item = self.top
            # and use it to retrieve and assign the next item in the stack to the head of the stack
            self.top = self.top.getNext()

        return item

    def peek(self):
        # Just return the data of the top item
        return self.top

    def size(self):
        current = self.top
        count = 0

        # Keep iterating through the stack and increment the count per iteration
        while current is not None:
            count += 1
            current = current.getNext()

        return count


    # Very useful for visually confirming the positioning of Disks as a sanity check
    def print_disks(self):
        current = self.top
        disks = []

        while current is not None:
            # print(current.getData(), end="")
            disks.append(current.getData())
            current = current.getNext()

        return str(disks)
