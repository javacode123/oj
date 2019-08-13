# -*- coding: utf-8 -*-
# @Time    : 2019-08-25 16:02
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : sortColors.py
# @Software: PyCharm


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0, p2, cur = 0, len(nums)-1, 0

        while cur <= p2:
            if nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            else:
                cur += 1


if __name__ == '__main__':
    l = [2,0,2,1,1,0]
    Solution().sortColors(l)
    print(l)
