# -*- coding: utf-8 -*-
# @Time    : 2019-08-19 14:34
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : groupAngrapms.py
# @Software: PyCharm


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []

        res = []
        word_ditc = {}

        for word in strs:
            sort_word = ''.join(sorted(word))

            if word_ditc.get(sort_word, None):
                sub_res = word_ditc.get(sort_word)
                sub_res.append(word)
                word_ditc[sort_word] = sub_res
            else:
                sub_res = [word]
                word_ditc[sort_word] = sub_res

        for k, v in word_ditc.items():
            res.append(v)

        return res


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))