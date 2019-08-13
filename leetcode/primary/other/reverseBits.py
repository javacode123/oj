# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 14:29
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : reverseBits.py
# @Software: PyCharm


class Solution:

    def reverseBits(self, n):
        res = 0

        for i in range(32):
            res <<= 1
            res += n & 1
            n >>= 1

        return res


if __name__ == '__main__':
    print(len('01110010111100000101001010000000'))

