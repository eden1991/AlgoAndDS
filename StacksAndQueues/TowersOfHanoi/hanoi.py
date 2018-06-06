#!/usr/bin/env python3
from AlgoAndDS.StacksAndQueues.TowersOfHanoi.tower import Tower

'''
3.4 In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different
sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
order of size from top to bottom (e.g., each disk sits on top of an even larger one). You
have the following constraints:
(A) Only one disk can be moved at a time.
(B) A disk is slid off the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first rod to the last using Stacks.
'''

# We pass in a variable for keeping count of illegal moves purely for testing purposes.
# This variable cannot be declared inside the function as it will get overwritten
# every time that the function recurses.
def towers_of_hanoi(disk, source, auxiliary, destination, illegal_counter):
    '''
    Keep track of any illegal moves made. Disks on the source tower should always be
    smaller than any disks on the auxiliary tower when pushing on to it.
    '''
    # When the disk size is down to 1, simply pop it from the source tower and push it
    # on to the auxiliary tower.
    if disk == 1:
        if source.size() > 0 and auxiliary.size() > 0:
            if source.peek().getData() > auxiliary.peek().getData():
                illegal_counter += 1
        auxiliary.push(source.pop().getData())
        # print("Exited, S>A | Disk == 1 | S: %s | A: %s | D: %s"
        #       % (source.print_disks(), auxiliary.print_disks(), destination.print_disks()))
        # print("")
    else:
        # print("Calling r1  | Disk == %d | S: %s | D: %s | A: %s"
        #       % (disk - 1, source.print_disks(), destination.print_disks(), auxiliary.print_disks()))

        # The aim here is to move disks from the source tower to the auxiliary tower
        towers_of_hanoi(disk - 1, source, destination, auxiliary, illegal_counter)  # r1

        # print("Returned from r1 | Disk == %d | S: %s | A: %s | D: %s"
        #       % (disk, source.print_disks(), auxiliary.print_disks(), destination.print_disks()))

        # print("Continuing towards r2. Push Source -> Aux")
        '''
        Continue to keep track of any illegal moves made. Disks on the source tower should always be
        smaller than any disks on the auxiliary tower when pushing on to it.
        '''
        if source.size() > 0 and auxiliary.size() > 0:
            if source.peek().getData() > auxiliary.peek().getData():
                illegal_counter += 1

        # The aim here is to move disks from the source tower to the destination tower
        auxiliary.push(source.pop().getData())
        # print("Pushed S > A | Disk == %d | S: %s | A: %s | D: %s"
        #       % (disk, source.print_disks(), auxiliary.print_disks(), destination.print_disks()))

        # print("Calling r2  | Disk == %d | D: %s | A: %s | S: %s"
        #       % (disk - 1, destination.print_disks(), auxiliary.print_disks(), source.print_disks()))

        # The aim here is to move disks from the auxiliary tower to the destination tower
        towers_of_hanoi(disk - 1, destination, auxiliary, source, illegal_counter)  # r2
        # print("Returned from r2  | Disk == %d | S: %s | A: %s | D: %s"
        #       % (disk, source.print_disks(), auxiliary.print_disks(), destination.print_disks()))
        return illegal_counter


if __name__ == '__main__':
    One = Tower()
    Two = Tower()
    Three = Tower()

    # Variable for keeping count of the number of illegal moves made
    # i.e. the program places a larger disk over a smaller disk
    illegal_moves = 0

    One.push(5)
    One.push(4)
    One.push(3)
    One.push(2)
    One.push(1)

    print("Pre-state   | Disk == %d | One: %s | Two: %s | Three: %s"
          % (One.size(), One.print_disks(), Two.print_disks(), Three.print_disks()))
    print("- - -")
    illegal_moves_made = towers_of_hanoi(One.size(), One, Two, Three, illegal_moves)
    print("- - -")
    print("Post-state  | Disk == %d | One: %s | Two: %s | Three: %s"
          % (Three.size(), One.print_disks(), Two.print_disks(), Three.print_disks()))
    print(illegal_moves_made)
