# -*- coding: utf-8 -*-
# @Time    : 2019-09-03 13:17
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : replaceChar.py
# @Software: PyCharm


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = list(s)
        size = len(s)

        for i in range(size):
            if s[i] == ' ':
                s.append(' ')
                s.append(' ')

        cur, tail = size - 1, len(s) - 1

        while cur >= 0:
            if s[cur] != ' ':
                s[tail] = s[cur]
                tail -= 1
            else:
                s[tail-2: tail + 1] = ['%', '2', '0']
                tail -= 3

            cur -= 1

        return ''.join(s)


if __name__ == '__main__':
    print(Solution().replaceSpace('We Are Happy'))