# -*- coding: utf-8 -*-
# @Time    : 2019-08-19 14:12
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : setZeros.py
# @Software: PyCharm


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        clo_num = []
        raw_num = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    raw_num.append(i)
                    clo_num.append(j)

        for i in raw_num:
            matrix[i] = [0] * n

        for j in clo_num:
            for line in matrix:
                line[j] = 0


if __name__ == '__main__':
    matrix = [
      [1,1,1],
      [0,1,1],
      [1,1,1]
    ]
    Solution().setZeroes(matrix)
    print(matrix)
