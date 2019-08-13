# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 4:51 PM
# @Author  : zhang_jia_luo@foxmail.com
# @File    : deleteNode.py
# @Software: PyCharm


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
