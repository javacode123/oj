# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:31
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : climbStairs.py
# @Software: PyCharm


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [1, 2]:
            return n

        res = [1, 2]

        for i in range(n-2):
            res.append(res[-1] + res[-2])

        return res[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(5))