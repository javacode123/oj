# -*- coding: utf-8 -*-
# @Time    : 2019-09-02 14:38
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : lengthOfLIS.py
# @Software: PyCharm


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        hepler = [nums[0]]
        for i in nums[1:]:
            if i > hepler[-1]:
                hepler.append(i)
                continue
            low, high = 0, len(hepler)-1
            while low < high:
                mid = low + (high-low) // 2
                if hepler[mid] >= i:
                    high = mid
                else:
                    low = mid+1
            hepler[high] = i
        print(hepler)
        return len(hepler)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([4,10,4,3,8,9]))
