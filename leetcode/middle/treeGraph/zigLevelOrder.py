# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 15:21
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : zigLevelOrder.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue, res, reverse = [root], [], False

        while queue:
            next_queue = []
            res_line = []
            while queue:
                node = queue.pop(0)
                if node:
                    res_line.append(node.val)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            if res_line:
                if reverse:
                    res_line.reverse()
                    res.append(res_line)
                else:
                    res.append(res_line)
                reverse = not reverse
            queue = next_queue

        return res


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(Solution().zigzagLevelOrder(root))
