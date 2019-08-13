# -*- coding: utf-8 -*-
# @Time    : 2019-09-10 18:43
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : inverse_pair.py
# @Software: PyCharm


class Solution:
    def InversePairs(self, data):
        res = 0
        count = len(data)

        for i in range(1, count):
            for j in range(count - i, count):
                if data[count - i - 1] > data[j]:
                    res += 1

        return res % 1000000007


if __name__ == '__main__':
    print(Solution().InversePairs([2, 0,1,2,3,4,5,6,7,0]))