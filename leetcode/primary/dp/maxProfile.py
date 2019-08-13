# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 20:40
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : maxProfile.py
# @Software: PyCharm


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def helper(max_profile, low_price, i, prices):
            if i == len(prices):
                return max_profile
            price = prices[i]
            max_profile = max(max_profile, price-low_price)
            low_price = min(low_price, price)
            return helper(max_profile, low_price, i+1, prices)

        return helper(0, prices[0], 0, prices)


if __name__ == '__main__':
    l = [7,1,5,3,6,4]
    print(Solution().maxProfit(l))
