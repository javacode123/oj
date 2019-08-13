# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 11:28
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : addTwoNumbers.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        p1, p2, cur, carry = l1, l2, head, 0

        while p1 or p2:
            x1 = p1.val if p1 else 0
            x2 = p2.val if p2 else 0
            val = x1 + x2 + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            cur = cur.next

        if carry:
            cur.next = ListNode(1)

        return head.next


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(5)
    head = Solution().addTwoNumbers(l1, l2)

    while head:
        print(head.val)
        head = head.next



