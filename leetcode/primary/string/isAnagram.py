# coding: utf-8
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_dict = {}

        for i in s:
            if char_dict.get(i, None) is None:
                char_dict[i] = 1
            else:
                char_dict[i] += 1

        for i in t:
            if char_dict.get(i, 0) > 0:
                char_dict[i] -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    print Solution().isAnagram('ab', 'a')