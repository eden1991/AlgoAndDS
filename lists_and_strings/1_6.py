#!/usr/bin/env python3
import unittest

# Task description
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

class TestStringMethods(unittest.TestCase):

    def test_checker(self):
        matrix = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]
        rotated_matrix = [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]
        rotate(matrix, len(matrix))
        self.assertEqual(matrix, rotated_matrix)
        matrix = [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]
        rotated_matrix = [4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]
        rotate(matrix, len(matrix))
        self.assertEqual(matrix, rotated_matrix)


def rotate(matrix, n):
    for layer in range(0, n//2):
        first = layer
        last = n - 1 - layer
        for pixel in range(first, last):
            offset = pixel - first
            top = matrix[first][pixel]  # Save top

            # left -> top
            matrix[first][pixel] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[pixel][last]

            # top -> right
            matrix[pixel][last] = top # right <- top


if __name__ == '__main__':
    unittest.main()
