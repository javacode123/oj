# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 16:57
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : ugly_num.py
# @Software: PyCharm


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 1:
            return 1
        res = [1]
        p2, p3, p5 = 0, 0, 0

        for i in range(index):
            temp = min(res[0] * 2, res[p3] * 3, res[p5] * 5)
            res.append(temp)
            if temp % 2 == 0:
                p2 += 1
            elif temp % 3 == 0:
                p3 += 1
            else:
                p5 += 1

        return res[index]