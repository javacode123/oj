# -*- coding: utf-8 -*-
# @Time    : 2019-08-31 14:10
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : merge.py
# @Software: PyCharm


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return None
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        res = []

        for interval in sort_intervals:
            if res and res[-1][1] >= interval[0]:
                temp = res.pop()
                temp[1] = max(temp[1], interval[1])
                res.append(temp)
            else:
                res.append(interval)

        return res


if __name__ == '__main__':

    arr = [[1, 4], [0, 4]]
    print(Solution().merge(arr))