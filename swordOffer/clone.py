# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 20:04
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : clone.py
# @Software: PyCharm


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        p = pHead

        while p:  # 插入复制
            clone = RandomListNode(p.label)
            clone.next = p.next
            p.next = clone
            p = clone.next

        p = pHead

        while p:  # 复杂指针复制
            clone = p.next
            if p.random:
                clone.random = p.random.next
            p = clone.next
        p = pHead
        res = p.next
        copy_cur = res
        while p:  # 分离
            p.next = copy_cur.next
            p = p.next
            copy_cur.next = p.next
            copy_cur = copy_cur.next
        return res


if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    print(Solution().Clone(head))