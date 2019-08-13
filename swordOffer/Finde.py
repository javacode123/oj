# -*- coding: utf-8 -*-
# @Time    : 2019-09-03 13:08
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : Finde.py
# @Software: PyCharm


# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        m, n = 0, len(array[0]) - 1

        while m < len(array) and n >= 0:
            if array[m][n] == target:
                return True
            if array[m][n] < target:
                m += 1
            else:
                n -= 1

        return False


print(Solution().Find(7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))