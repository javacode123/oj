# -*- coding: utf-8 -*-
# @Time    : 2019-08-23 11:44
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : connect.py
# @Software: PyCharm


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        queue = [root]

        while queue:
            size = len(queue)
            next = None
            while size != 0:
                cur = queue.pop(0)
                if cur.right:
                    queue.append(cur.right)
                    queue.append(cur.left)
                cur.next = next
                next = cur
                size -= 1

        return root


if __name__ == '__main__':
    root = Node(5, Node(4, None, None, None), Node(3, None, None, None), None)
    print(Solution().connect(root))
    print(root.left.next.val)
