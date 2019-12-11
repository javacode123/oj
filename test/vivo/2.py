# -*- coding: utf-8 -*-
# @Time    : 2019-09-22 16:10
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : 2.py
# @Software: PyCharm


'''
Welcome to vivo !
'''


def solution(N, M):
    numbers = [i+1 for i in range(N)]
    res = []
    index = 1
    pre_index = 1

    while numbers:
        line = []
        for i in range(len(numbers)):
            if index % M == 0:
                line.append(numbers[(index-pre_index)])
            index += 1
        for i in line:
            res.append(i)
            numbers.remove(i)
        pre_index = index

    return ' '.join([str(_) for _ in res])


N, M = [int(i) for i in input().split()]
solution(N, M)