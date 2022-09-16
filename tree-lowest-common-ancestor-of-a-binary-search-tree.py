# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Time: O(logn) Space: O(1)
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def lowestCommonAncestor(self, root, p, q):
        curr = root
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
    
    def test_first(self):
        self.assertEqual(self.lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5], 2, 8), 6)

    def test_second(self):
        self.assertEqual(self.lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5], 2, 4), 2)


if __name__ == '__main__':
    unittest.main()