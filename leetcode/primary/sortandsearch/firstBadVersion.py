# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:04
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : firstBadVersion.py
# @Software: PyCharm


def isBadVersion(version):
    return True


class Solution(object):


    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(low, high):
            if low >= high:
                return low
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                return helper(low, mid)
            else:
                return helper(mid+1, high)

        return helper(1, n)

