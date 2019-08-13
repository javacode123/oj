# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 19:57
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : isValid.py
# @Software: PyCharm


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        mapping = {')': '(', '}': '{', ']': '['}

        stack = []
        for char in s:

           if char in mapping:
               top_element = stack.pop() if len(stack) > 0 else '#'
               if top_element != mapping[char]:
                   return False
           else:
               stack.append(char)

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid('((())'))
