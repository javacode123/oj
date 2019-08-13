# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 12:54
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : convert.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None

        def helper(node):
            if not node:
                return
            helper(node.left)
            node.left = self.pre
            if self.pre:
                self.pre.right = node
            else:
                self.head = node
            self.pre = node
            helper(node.right)

        helper(pRootOfTree)
        return self.head


if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    head = Solution().Convert(root)
    s = 'abcd'
    print(s.split('b'))