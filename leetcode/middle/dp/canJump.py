# -*- coding: utf-8 -*-
# @Time    : 2019-08-31 15:47
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : canJump.py
# @Software: PyCharm


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        left_index = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= left_index:
                left_index = i

        return left_index == 0


if __name__ == '__main__':
    print(Solution().canJump([3,2,1,0,4]))

