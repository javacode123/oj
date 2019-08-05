# coding: utf-8
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution(object):
    def plusOne_v1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = 0
        res = []

        for i in digits:
            value = value * 10 + i

        value += 1

        while value != 0:
            res.insert(0, value % 10)
            value = value / 10

        return res

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = True  # 是否需要进位置
        for i in range(len(digits)-1, -1, -1):
            if flag:
                if digits[i] + 1 >= 10:
                    flag = True
                else:
                    flag = False
                digits[i] = (digits[i] + 1) % 10
            else:
                break

        if flag:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    print(Solution().plusOne([9,9,9]))