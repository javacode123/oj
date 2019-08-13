# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 13:20
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : isPowerOfThree.py
# @Software: PyCharm


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPowerOfThree(9))