# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:45
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : letterCombinations.py
# @Software: PyCharm


class Solution(object):
    def letterCombinations_v1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def back_track(combination, next_digits):
            if len(next_digits) == 0:
                return res.append(combination)

            for c in char_dict[next_digits[0]]:
                back_track(combination + c, next_digits[1:])

        res = []
        back_track('', digits)

        return res


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return None

        queue = [_ for _ in char_dict[digits[0]]]

        for i in range(1, len(digits)):
            queue_size = len(queue)
            for _ in range(queue_size):
                sub_str = queue.pop(0)
                for c in char_dict[digits[i]]:
                    queue.append(sub_str + c)

        return queue


if __name__ == '__main__':
    print(Solution().letterCombinations('2'))
