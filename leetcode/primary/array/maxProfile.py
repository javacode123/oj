# coding: utf-8


class Solution(object):
    '''
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    '''
    def maxProfit(self, prices):
        """
        solution:
            最大利润就是全部递增子数组的差值只和，使用贪心算法的思想，只要明天的价格比今天的高我就买，直到一天价格比前一天价格低卖出
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if prices is None or len(prices) == 0:
            return res

        for i in range(len(prices) -1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]

        return res


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))