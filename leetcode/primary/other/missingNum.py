# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 20:19
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : missingNum.py
# @Software: PyCharm


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int  [1, 0, 2, #]
        """
        if nums:
            missing_num = len(nums)

            for i in range(len(nums)):
                missing_num ^= (i ^ nums[i])

            return missing_num

        else:
            raise Exception('invalid params')


if __name__ == '__main__':
    print(Solution().missingNumber([0, 1, 3]))