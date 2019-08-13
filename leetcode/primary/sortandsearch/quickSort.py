# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:54
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : maxSubArray.py
# @Software: PyCharm


class Solution(object):
    def sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return []
        self.quick_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, nums, low, high):
        if low >= high:
            return
        mid = self.get_mid(nums, low, high)
        self.quick_sort(nums, low, mid-1)
        self.quick_sort(nums, mid+1, high)

    def get_mid(self, nums, low, high):
        temp = nums[low]

        while low < high:
            while nums[high] >= temp and low < high:
                high -= 1
            nums[low] = nums[high]
            while nums[low] < temp and low < high:
                low += 1
            nums[high] = nums[low]

        nums[low] = temp
        return low


if __name__ == '__main__':
    print(Solution().sort([9, 8, 7, 0]))
