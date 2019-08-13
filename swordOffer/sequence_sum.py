# -*- coding: utf-8 -*-
# @Time    : 2019-09-17 15:10
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : sequence_sum.py
# @Software: PyCharm


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        for i in range(1, tsum):
            temp = [i]
            temp_sum = i
            for j in range(i + 1, tsum):
                temp.append(j)
                temp_sum += j
                if temp_sum == tsum:
                    res.append(temp)
                    break
                if temp_sum > tsum:
                    break

        return res


if __name__ == '__main__':
    print(Solution().FindContinuousSequence(3))