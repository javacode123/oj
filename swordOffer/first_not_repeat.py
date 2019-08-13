# -*- coding: utf-8 -*-
# @Time    : 2019-09-08 12:54
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : first_not_repeat.py
# @Software: PyCharm


import collections


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        res = -1
        if not s:
            return res

        o_dict = collections.OrderedDict()

        for c in s:
            if o_dict.get(c):
                o_dict[c] += o_dict[c]
            else:
                o_dict[c] = 1

        for k, v in o_dict.items():
            if v == 1:
                res = s.index(k)
                break

        return res


if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('google'))
