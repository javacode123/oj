# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:41
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm


def process_line(line):
    start = 0
    res = [0] * len(line)

    while start < len(line)-1:
        if line[start] == line[start+1]:
            line[start] = line[start] * 2
            line[start+1] = 0
        start += 1

    index = 0

    for i in line:
        if i != 0:
            res[index] = i
            index += 1

    return res


if __name__ == '__main__':
    while True:
        n = int(input().split()[0])
        arr = [[0] for _ in range(n)]

        for i in range(n):
            input_raw = [int(_) for _ in input().split(' ')]
            arr[i] = process_line(input_raw)

        for line in arr:
            print(' '.join([str(_) for _ in line]))


