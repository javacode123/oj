# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 4:38 PM
# @Author  : zhang_jia_luo@foxmail.com
# @File    : longestCommonPrefix.py
# @Software: PyCharm


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if len(strs) <= 0 or strs is None:
            return res

        res = strs[0]

        for word in strs:

            min_len = min(len(word), len(res))
            res = res[: min_len]
            for i in range(min_len):
                if res[i] != word[i]:
                    res = res[:i]
                    break

        return res


if __name__ == '__main__':
    s = ["aaa","aa","aaa"]
    print(Solution().longestCommonPrefix(s))


