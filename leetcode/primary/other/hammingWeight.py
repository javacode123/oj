# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 14:06
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : hammingWeight.py
# @Software: PyCharm


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0

        while n != 0:
            res += 1
            n = n & n-1

        return res


if __name__ == '__main__':
    print(Solution().hammingWeight(9))