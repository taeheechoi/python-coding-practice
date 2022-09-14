# https://leetcode.com/problems/invert-binary-tree/

import unittest

class Test(unittest.TestCase):

    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def test_first(self):
        self.assertEqual(self.lowestCommonAncestor([2,1,3]), [2,3,1])
    
    def test_second(self):
        self.assertEqual(self.lowestCommonAncestor([]), [])


if __name__ == '__main__':
    unittest.main()
