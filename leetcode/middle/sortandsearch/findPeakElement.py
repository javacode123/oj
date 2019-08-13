# -*- coding: utf-8 -*-
# @Time    : 2019-08-30 17:27
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : findPeakElement.py
# @Software: PyCharm


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        low, high = 0, len(nums)-1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == '__main__':

    print(Solution().findPeakElement([1,2,1,3,5,6,4]))