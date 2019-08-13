# -*- coding: utf-8 -*-
# @Time    : 2019-09-02 14:13
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : coinCharge.py
# @Software: PyCharm
import sys


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        helper = [sys.maxsize for _ in range(amount+1)]
        helper[0] = 0

        for i in range(amount+1):
            for c in coins:
                if i >= c:
                    helper[i] = min(helper[i-c]+1, helper[i])

        return -1 if helper[amount] == sys.maxsize else helper[amount]


if __name__ == '__main__':
    print(Solution().coinChange([2], 5))