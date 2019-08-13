# -*- coding: utf-8 -*-
# @Time    : 2019-08-31 13:32
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : searchRange.py
# @Software: PyCharm


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums)-1
        res = [-1, -1]
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start > 0:
                    if nums[start-1] == target:
                        start -= 1
                    else:
                        break
                while end < len(nums)-1:
                    if nums[end+1] == target:
                        end += 1
                    else:
                        break
                res = [start, end]
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return res


if __name__ == '__main__':
    print(Solution().searchRange([1], 1))
