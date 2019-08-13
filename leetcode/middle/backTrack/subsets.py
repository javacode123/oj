# -*- coding: utf-8 -*-
# @Time    : 2019-08-25 15:29
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : subsets.py
# @Software: PyCharm


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_tarck(combination, next_nums, size):

            if len(combination) == size:
                res.append(combination)
            else:
                for i in range(len(next_nums)):
                    back_tarck(combination+[next_nums[i]], next_nums[i+1:], size)

        res = [[]]
        for size in range(1, len(nums)+1):
            back_tarck([], nums, size)

        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
