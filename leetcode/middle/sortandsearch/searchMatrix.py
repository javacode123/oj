# -*- coding: utf-8 -*-
# @Time    : 2019-08-31 15:04
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : searchMatrix.py
# @Software: PyCharm


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False


if __name__ == '__main__':
    print(Solution().searchMatrix([
  [4]
], 4))
