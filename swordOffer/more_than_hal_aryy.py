# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 14:11
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : more_than_hal_aryy.py
# @Software: PyCharm


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        num = numbers[0]
        count = 1

        for i in numbers[1:]:
            if i == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                num = i
        count = 0
        for i in numbers:
            if i == num:
                count += 1

        return num if count > len(numbers) // 2 else 0


if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
