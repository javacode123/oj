# -*- coding: utf-8 -*-
# @Time    : 2019-08-19 15:36
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : longSubString.py
# @Software: PyCharm


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sub_dict = {}
        start = 0  #窗口起点

        for i in range(len(s)):
            if sub_dict.get(s[i], None):
                start = max(start, sub_dict.get(s[i]))
            res = max(res, i-start+1)
            sub_dict[s[i]] = i+1  #不重复的 s[i] 起点

        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('mainmain'))
