# -*- coding: utf-8 -*-
# @Time    : 2019-09-23 20:23
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : 3.py
# @Software: PyCharm
'''
5
2 3 5
1 4
2 2 5
0
1 4
'''


N = int(input().split()[0])
temp = [False for _ in range(N)]
condations = {}

for i in range(N):
    line = [int(_) for _ in input().split()]
    condations[i+1] = line[1:]

res = []
s = set()
pre = 0

for i in range(N):
    queue = condations[i+1]
    s.add(i+1)
    while len(queue) > 0:
        node = queue.pop(0)
        s.add(node)
        if len(condations[node]) != 0:
            queue = condations[node]+queue
    res.append(len(s) - pre)
    pre = len(s)

print(' '.join([str(_) for _ in res]))
