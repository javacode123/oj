# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 12:23
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : fizzBuzz.py
# @Software: PyCharm


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n % 3 == 0:
            if n % 5 == 0:
                return "FizzBuzz"
            else:
                return "Fizz"
        elif n % 5 == 0:
            return "Buzz"

        return str(n)


if __name__ == '__main__':
    for i in range(6):
        print(Solution().fizzBuzz(i))
