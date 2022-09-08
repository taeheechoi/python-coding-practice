import unittest

class Test(unittest.TestCase):

    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val > cur.val and p.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

    def test_first(self):
        self.assertEqual(self.lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5], 2, 4), 2)
    
    def test_second(self):
        self.assertEqual(self.lowestCommonAncestor([2,1], 2, 1), 2)


if __name__ = '__main__':
    unittest.main()
