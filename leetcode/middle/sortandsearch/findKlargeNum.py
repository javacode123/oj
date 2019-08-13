# -*- coding: utf-8 -*-
# @Time    : 2019-08-26 20:33
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : findKlargeNum.py
# @Software: PyCharm
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partion(nums, low, high):
            temp = nums[low]

            while low < high:
                while low < high and nums[high] <= temp:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] > temp:
                    low += 1
                nums[high] = nums[low]

            nums[low] = temp

            return low

        low, high = 0, len(nums)-1
        while True:
            p = partion(nums, low, high)
            if p == k-1:
                return nums[p]
            if p > k-1:
                high = p - 1
            else:
                low = p + 1


if __name__ == '__main__':
    l = [3,2,1,5,6,4]
    print(Solution().findKthLargest(l, 2))
    print(l)
