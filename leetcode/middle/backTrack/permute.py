# -*- coding: utf-8 -*-
# @Time    : 2019-08-25 14:56
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : permute.py
# @Software: PyCharm
import copy


class Solution(object):
    def permute_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_track(combination, next_nums):
            if not next_nums:
                res.append(combination)
            else:
                for i in range(len(next_nums)):
                    back_track(combination + [next_nums[i]], next_nums[0: i] + next_nums[i+1:])

        res = []
        back_track([], nums)

        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        queue = []
        res = []

        for i in range(len(nums)):
            queue.append(([nums[i]], nums[0: i]+nums[i+1:]))

        while queue:
            size = len(queue)
            for i in range(size):
                sub_num, tail = queue.pop(0)
                if not tail:
                    res.append(sub_num)
                else:
                    for j in range(len(tail)):
                        queue.append((sub_num+[tail[j]], tail[0: j]+tail[j+1:]))

        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
