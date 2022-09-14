# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# T: O(n) S: O(n) - height

import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


class Test(unittest.TestCase):

    def recursive(self, root):
        if not root:
            return 0
        return 1 + max(self.recursive(root.left), self.recursive(root.right))

    def iterative_bfs(self, root):
        if not root:
            return 0
        level = 0

        q = deque([root])

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def iterative_dfs(self, root):
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result

    # def setUp(self):
    #     self.root = TreeNode()

    # def test_first(self):
    #     items = [3,9,20,None,None,15,7]
    #     for item in items:
    #         self.root.insert(item)
    #     print(self.root)
        # self.assertEqual(self.iterative_bfs([3,9,20,None,None,15,7]), 3)

    # def test_second(self):
    #     self.assertEqual(self.iterative_bfs([1,None,2]), 2)


if __name__ == '__main__':
    unittest.main()
