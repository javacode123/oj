# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 14:13
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : get_leats_k.py
# @Software: PyCharm


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []

        def quick_sore(n, low, high):
            if low < high:
                mid = self.helper(tinput, low, high)
                quick_sore(n, low, mid - 1)
                quick_sore(n, mid + 1, high)
        quick_sore(tinput, 0, len(tinput)-1)
        return tinput

    def helper(self, numbers, low, high):
        temp = numbers[low]
        while low < high:
            while low < high and numbers[high] >= temp:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] < temp:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = temp
        return low


print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 2))
