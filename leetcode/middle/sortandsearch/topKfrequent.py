# -*- coding: utf-8 -*-
# @Time    : 2019-08-26 20:14
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : topKfrequent.py
# @Software: PyCharm
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_num = {}

        for num in nums:
            if dict_num.get(num):
                dict_num[num] = dict_num[num] + 1
            else:
                dict_num[num] = 1

        return [k for k,v in heapq.nlargest(k, dict_num.items(), key=lambda x: x[1])]


if __name__ == '__main__':
    print(Solution().topKFrequent(['1', '1', '1', '2', '3', '4'], 2))