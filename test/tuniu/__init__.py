# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 19:58
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return None
        l = []
        l.append(root)

        while len(l):
            node = l.pop(0)
            print(node.val)
            if node.left:
                l.append(node.left)
            if node.right:
                l.append(node.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().PrintFromTopToBottom(root))