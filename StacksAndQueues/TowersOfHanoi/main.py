#!/usr/bin/env python3
from AlgoAndDS.StacksAndQueues.TowersOfHanoi.tower import Tower
from AlgoAndDS.StacksAndQueues.TowersOfHanoi.hanoi import towers_of_hanoi
import unittest

class TestHanoi(unittest.TestCase):

    def test_hanoi_3_disks(self):
        one = Tower()
        two = Tower()
        three = Tower()
        # A variable for keeping count of the number of illegal moves made
        # i.e. if the program places a larger disk over a smaller disk
        illegal_moves = 0

        # We'll try with just 3 disks to start off with
        one.push(3)
        one.push(2)
        one.push(1)

        illegal_moves_made = towers_of_hanoi(one.size(), one, two, three, illegal_moves)
        # Test that we get all disks on to the destination tower
        self.assertEquals(3, two.size())
        # There should be no disks on either of the other towers
        self.assertEquals(0, one.size())
        self.assertEquals(0, three.size())
        # Test that the program made no illegal moves i.e. it did not place any larger disks on
        # top of smaller disks
        self.assertEquals(0, illegal_moves_made)

    # Now let's try with 5 disks
    def test_hanoi_5_disks(self):
        # Setup new towers
        one = Tower()
        two = Tower()
        three = Tower()
        illegal_moves = 0

        one.push(5)
        one.push(4)
        one.push(3)
        one.push(2)
        one.push(1)

        illegal_moves_made = towers_of_hanoi(one.size(), one, two, three, illegal_moves)
        # Test that we get all disks on to the destination tower
        self.assertEquals(5, two.size())
        # There should be no disks on either of the other towers
        self.assertEquals(0, one.size())
        self.assertEquals(0, three.size())
        # Test that the program made no illegal moves i.e. it did not place any larger disks on
        # top of smaller disks
        self.assertEquals(0, illegal_moves_made)


if __name__ == '__main__':
    unittest.main()