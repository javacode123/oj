# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 00:20
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : increaseTuple.py
# @Software: PyCharm


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a, b = float('inf'), float('inf')

        for i in nums:
            if i <= a:
                a = i
            elif i <= b:
                b = i
            else:
                return True

        return False
