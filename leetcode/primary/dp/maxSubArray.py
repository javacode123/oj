# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:54
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : maxSubArray.py
# @Software: PyCharm


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        max_sum, pre_sum = nums[0], nums[0]

        for i in nums[1:]:
            pre_sum = max(pre_sum+i, i)
            max_sum = max(pre_sum, max_sum)

        return max_sum


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
