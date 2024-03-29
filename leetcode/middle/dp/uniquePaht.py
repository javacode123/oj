# -*- coding: utf-8 -*-
# @Time    : 2019-08-31 16:16
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : uniquePaht.py
# @Software: PyCharm


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__  == '__main__':
    print(Solution().uniquePaths(7, 3))
