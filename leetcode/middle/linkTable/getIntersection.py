# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 14:23
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : getIntersection.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_dict = {}
        p1, p2 = headA, headB

        while p1:
            node_dict[p1] = 1
            p1 = p1.next

        while p2:
            if node_dict.get(p2, 0) == 1:
                return p2
            p2 = p2.next

        return None


if __name__ == '__main__':
    h1 = ListNode(1)
    node = ListNode(2)
    h1.next = node
    h2 = ListNode(1)
    h2.next = node
    print(Solution().getIntersectionNode(h1, h2).val)
