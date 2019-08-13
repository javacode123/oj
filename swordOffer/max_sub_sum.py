# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 14:45
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : max_sub_sum.py
# @Software: PyCharm


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        res = array[0]
        dp = [array[0]]

        for i in range(1, len(array)):
            dp.append(max(array[i], dp[i - 1] + array[i]))
            print(dp)
            res = max(dp[i - 1], dp[i])

        return res


if __name__ == '__main__':
    print(Solution().FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))
