# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 14:02
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : oddEvenList.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even, cur = ListNode(-1), ListNode(-1), head
        cur_even, cur_odd = even, odd

        while cur:
            cur_odd.next = cur
            cur_odd = cur_odd.next
            cur = cur.next
            if cur:
                cur_even.next = cur
                cur_even = cur_even.next
                cur = cur.next

        cur_even.next = None
        cur_odd.next = even.next

        return odd.next


if __name__ == '__main__':
    head = ListNode(2)
    root = Solution().oddEvenList(head)

    while root:
        print(root.val)
        root = root.next
