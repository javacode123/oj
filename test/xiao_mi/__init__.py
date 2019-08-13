# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 18:48
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm

import sys
prices = [2, 4, 6]
count = 10
dp = [sys.maxsize] * (count + 1)

for i in prices:
    dp[i] = 1

for i in range(1, count+1):
    arr = []
    for price in prices:
        if i >= price:
            if dp[i-price] != sys.maxsize:
                arr.append(dp[i-price] + 1)
    arr.append(dp[i])
    dp[i] = max(arr) if arr else sys.maxsize

print(dp)