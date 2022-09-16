# https://leetcode.com/problems/invert-binary-tree/
# O(n)-number of nodes, O(n)
import unittest
from collections import deque

class Test(unittest.TestCase):

    def invertTree(self, root):
        if not root:
            return []
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


    def bfs(self, root):
        if not root:
            return []
        q = deque([root])
        while q:
            current = root.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                q.append(current.left)
            
            if current.right:
                q.append(current.right)
        return root

    def test_first(self):
        self.assertEqual(self.invertTree([2,1,3]), [2,3,1])
    
    def test_second(self):
        self.assertEqual(self.invertTree([4,2,7,1,3,6,9]), [4,7,2,9,6,3,1])


if __name__ == '__main__':
    unittest.main()
