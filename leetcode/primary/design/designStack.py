# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 17:09
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : designStack.py
# @Software: PyCharm


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.queue != []:
            if x <= self.queue[-1]:
                self.queue.append(x)
        else:
            self.queue.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            node = self.stack.pop()
            if node == self.queue[-1]:
                self.queue.pop()
            return node
        return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.queue) == 0:
            return None
        return self.queue[-1]


if __name__ == '__main__':
    import heapq
    l = []
    heapq.heappush(l, -4)
    heapq.heappush(l, -5)
    heapq.heappush(l, -0)
    heapq.heappush(l, -0)
    l = [-i for i in l]
    print(l)