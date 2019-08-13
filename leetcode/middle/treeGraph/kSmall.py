# -*- coding: utf-8 -*-
# @Time    : 2019-08-23 12:48
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : kSmall.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        queue, node, i = [], root, 1

        while queue or node:
            while node:
                queue.append(node)
                node = node.left
            node = queue.pop()
            if i == k:
                return node.val
            node = node.right
            i += 1
        return None


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    print(Solution().kthSmallest(root, 2))