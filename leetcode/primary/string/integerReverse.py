# coding: utf-8
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True if x >= 0 else False
        x = x if x >= 0 else -x
        res = 0

        while x != 0:
            res = res * 10 + (x % 10)
            x /= 10

        res = 0 if res > 2**31-1 or res < -2**31 else res
        return res if flag else -res


if __name__ == '__main__':
    print Solution().reverse(1563847412)
