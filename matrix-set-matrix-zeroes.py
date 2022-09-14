# https://leetcode.com/problems/set-matrix-zeroes/
# Time complexity : O(m*n)
# Space complexity : O(m+n)

import unittest

class Test(unittest.TestCase):

    def setZeros(self, matrix):
        rows = [1]*len(matrix)
        cols = [1]*len(matrix[0])

        for i in range(len(rows)):
            for j in range(len(cols)):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
        return matrix
    def test_first(self):
        self.assertEqual(self.setZeros([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])

    def test_second(self):
        self.assertEqual(self.setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]),  [[0,0,0,0],[0,4,5,0],[0,3,1,0]])


if __name__ == '__main__':
    unittest.main()
