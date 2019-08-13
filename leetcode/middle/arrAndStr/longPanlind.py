# -*- coding: utf-8 -*-
# @Time    : 2019-08-19 16:37
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : longPanlind.py
# @Software: PyCharm


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = '' if len(s) == 0 else s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for r in range(1, len(s)):
            for l in range(r):
                if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if len(res) < r-l+1:
                        res = s[l: r+1]

        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome('abcba'))