# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:41
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm

import sys


if __name__ == '__main__':
    for line in sys.stdin:  # 读作数组
        distance = [int(_) for _ in line.split()]  # 输入
        w = [int(_) for _ in input().split()]
        distance_count = int(input().split()[0])
        w.insert(0, 0)
        distance.insert(0, 0)
        res = 0
        dp = [[0 for _ in range(distance_count+1)] for _ in range(len(distance)+1)]

        for i in range(1, len(distance)):
            for j in range(1, distance_count+1):
                if j >= distance[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-distance[i] + w[i]])
                    res = max(dp[i][j], res)
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        print(res)