# -*- coding: utf-8 -*-
# @Time    : 2019-08-28 20:04
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : 2.py
# @Software: PyCharm
import sys


if __name__ == '__main__':
    A = [[1, 2, 3, 4, 5],
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45]]

    def next_char(i, j, opt):
        if opt == 'up':
            return [i-1, j] if i > 0 else None
        elif opt == 'down':
            return [i+1, j] if i < 4 else None
        elif opt == 'right':
            return [i, j+1] if j < 4 else None
        elif opt == 'left':
            return [i, j-1] if j > 0 else None


    def dfs(i, j, line):
        flag = [[0 for i in range(5)] for i in range(5)]
        stack = [[i, j]]
        while stack:
            [i, j] = stack.pop()
            if A[i][j] in line:
                del line[line.index(A[i][j])]
                flag[i][j] = -1
            for dirs in ['up', 'left', 'down', 'right']:
                ret = next_char(i, j, dirs)
                if ret:
                    if flag[ret[0]][ret[1]] == 0 and A[ret[0]][ret[1]] in line:
                        stack.append(ret)
        return not line

    def find(line):
        for i in range(5):
            for j in range(5):
                if A[i][j] in line:
                    return dfs(i, j, line)
        return False

    for line in sys.stdin:  # 读作数组
        line = [int(_) for _ in line.split()]
        if not line:
            break
        print(1 if find(line) else 0)
