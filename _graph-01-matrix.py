import unittest
from collections import deque


class Test(unittest.TestCase):
    def updateMatrix(self, mat):
        if not mat:
            return []
        rows, cols = len(mat), len(mat[0])

        visited = set()

        result = [[float('inf')]*cols for _ in range(rows)]
        # result = [[0 if mat[row][col] == 0 else float('inf') for col in range(cols)] for row in range(rows)]
        
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        q = deque()

        def traverse(i, j):
            visited.add((i, j))
            q.append((i, j))
            
            while q: 
                curr_i, curr_j = q.popleft()
            
                    
                for direction in directions:
                    next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                    
                    if 0 <= next_i < rows and 0 <= next_j < cols and (next_i, next_j) not in visited:
                        result[next_i][next_j] = mat[i][j] + 1
                        visited.add((next_i, next_j))
                        q.append((next_i, next_j +1))
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    traverse(i, j)
      


        return result

    # def test_first(self):
    #     self.assertEqual(self.updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]), [
    #                      [1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 2, 1, 1, 0, 1], [2, 1, 1, 1, 1, 2, 1, 0, 1, 0], [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]])

    def test_second(self):
        self.assertEqual(self.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]),[[0, 0, 0], [0, 1, 0], [0, 0, 0]])


if __name__ == '__main__':
    unittest.main()