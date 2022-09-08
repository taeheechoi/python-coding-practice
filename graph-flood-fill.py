import unittest

class Test(unittest.TestCase):

    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])

        init_color = image[sr][sc]

        directions = ((0,1), (0,-1), (1,0), (-1,0))

        if init_color == color: # when it is 0
            return image
        
        def traverse(i,j):
            if image[i][j] != init_color:
                return
            
            image[i][j] = color

            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    traverse(next_i, next_j)
        traverse(sr, sc)

        return image

    def test_first(self):
        self.assertEqual(self.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),  [[2,2,2],[2,2,0],[2,0,1]])
    
    def test_second(self):
        self.assertEqual(self.floodFill([[0,0,0],[0,0,0]], 0, 0, 0),   [[0,0,0],[0,0,0]])



if __name__ == '__main__':
    unittest.main()