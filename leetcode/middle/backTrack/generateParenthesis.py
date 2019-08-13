# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 16:29
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : generateParenthesis.py
# @Software: PyCharm


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def back_track(s='', l=0, r=0):
            if len(s) == n*2:
                res.append(s)
                return
            if l < n:
                back_track(s+'(', l+1, r)
            if r < l:
                back_track(s+')', l, r+1)

        back_track()
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(2))
