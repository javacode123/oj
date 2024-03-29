# coding: utf-8
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
 必须在原数组上操作，不能拷贝额外的数组。
 尽量减少操作次数。
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return nums

        not_zero_index = 0

        for i in nums:
            if i != 0:
                nums[not_zero_index] = i
                not_zero_index += 1

        while not_zero_index < len(nums):
            nums[not_zero_index] = 0
            not_zero_index += 1


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)

