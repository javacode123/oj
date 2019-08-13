# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 21:22
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : threeSum.py
# @Software: PyCharm


class Solution(object):
    # [-1, 0, 1, 2, -1, -4]
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            raise Exception('not valid params')

        nums = sorted(nums)  #排序
        res = []

        for i in range(len(nums)):  #遍历
            if nums[i] > 0:  #第一个数大于 0, 则三个数的和一定大于 0
                break
            if i > 0 and nums[i] == nums[i-1]:  #去重
                continue

            left, right = i+1, len(nums)-1  #右区间

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:  #去重
                        left += 1
                    while left < right and nums[right] == nums[right-1]:  #去重
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:  #增加中间值
                    left += 1
                else:  #减小最大值
                    right -= 1

        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))