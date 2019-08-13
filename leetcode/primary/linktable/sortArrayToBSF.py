# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 2:44 PM
# @Author  : zhang_jia_luo@foxmail.com
# @File    : sortArrayToBSF.py
# @Software: PyCharm

# Definition for a binary tree node.
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None

        def helper(nums, low, high):
            if low == high:
                return None
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = helper(nums, low, mid)
            node.right = helper(nums, mid+1, high)

            return node

        return helper(nums, 0, len(nums))

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None

        low, high = 0, len(nums)
        root = TreeNode(-1)
        stack = [(root, low, high)]

        while len(stack) > 0:
            node, low, high = stack.pop(0)
            mid = (low + high) // 2
            node.val = nums[mid]

            if low < mid:
                node.left = TreeNode(-1)
                stack.append((node.left, low, mid))
            if mid+1 < high:
                node.right = TreeNode(-1)
                stack.append((node.right, mid+1, high))

        return root


if __name__ == '__main__':
    print(Solution().sortedArrayToBST([1,2,3]))



