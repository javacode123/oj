# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        queue = [(root, [], expectNumber)]

        while len(queue):
            node, path, exp = queue.pop()
            path.append(node.val)
            exp = exp - node.val
            if exp == 0 and node.left is None and node.right is None:
                res.insert(0, list(path))
            p1 = list(path)
            p2 = list(path)
            if node.left:
                queue.append((node.left, p1, exp))
            if node.right:
                queue.append((node.right, p2, exp))
        return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    print(Solution().FindPath(root, 22))
