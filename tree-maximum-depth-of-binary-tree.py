import unittest
from collections import deque

class Test(unittest.TestCase):

    def recursive(self, root):
        if not root:
            return 0
        return 1 + max(self.recursive(root.left), self.recursive(root.right))

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

    def iterative_bfs(self, root):
        q = deque()
        if root:
            q.append(root)

        level = 0
        
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    # def test_first(self):
    #     self.assertEqual(self.iterative_bfs([3,9,20,None,None,15,7]), 3)

    # def test_second(self):
    #     self.assertEqual(self.iterative_bfs([1,None,2]), 2)


if __name__ == '__main__':
    unittest.main()