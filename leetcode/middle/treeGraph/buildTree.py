# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 16:03
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : buildTree.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left=0, in_right=len(inorder)):
            if in_left == in_right:
                return None

            nonlocal pre_index
            root_val = preorder[pre_index]
            root = TreeNode(root_val)
            pre_index += 1
            index = in_dict[root_val]

            root.left = helper(in_left, index)
            root.right = helper(index+1, in_right)

            return root

        pre_index = 0
        in_dict = {value: index for index, value in enumerate(inorder)}

        return helper()


if __name__ == '__main__':
    print(Solution().buildTree([1], [1]))