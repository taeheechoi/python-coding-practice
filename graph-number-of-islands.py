# https://leetcode.com/problems/number-of-islands/
# Time O(m*n) Space O(1)

import unittest
from collections import deque

class Test(unittest.TestCase):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        is_island = 0
        visited = set()

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                curr_i, curr_j = queue.popleft()
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))
                    for direction in directions:
                        next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                        if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == '1':
                            queue.append((next_i, next_j))

                                    

        def dfs(i, j):
            if (i, j) in visited or grid[i][j] == '0':
                return

            visited.add((i, j))

            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    dfs(next_i, next_j)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == '1':
                    is_island += 1
                    bfs(i, j)
                    

        return is_island

    def test_first(self):
        self.assertEqual(self.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]), 1)

    def test_second(self):
        self.assertEqual(self.numIslands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]), 3)


if __name__ == '__main__':
    unittest.main()
