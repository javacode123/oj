# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 16:19
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : rob.py
# @Software: PyCharm


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        pre_1, pre_2, cur = 0, 0, 0

        for i in nums:
            cur = max(pre_1, pre_2+i)
            pre_2 = pre_1
            pre_1 = cur

        return max(cur, pre_1)


if __name__ == '__main__':
    print(Solution().rob([2,7,9,3,1]))