# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 13:46
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : randomToInt.py
# @Software: PyCharm


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        print(dict(sorted(dict_char.items(), key=lambda k: k[1])))
        res = 0
        i = 0

        while i < len(s):
            if dict_char.get(s[i: i+2]):
                res += dict_char.get(s[i: i+2])
                i += 2
            elif dict_char.get(s[i]):
                res += dict_char.get(s[i])
                i += 1
            else:
                return None

        return res


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
