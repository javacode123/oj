# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 14:20
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : hanmingDistance.py
# @Software: PyCharm


class Solution(object):
    def hammingDistance(self, x, y):
        dis = x ^ y
        res = 0

        while dis != 0:
            res += 1
            dis &= dis - 1

        return res


if __name__ == '__main__':
    print(Solution().hammingDistance(5,1))

