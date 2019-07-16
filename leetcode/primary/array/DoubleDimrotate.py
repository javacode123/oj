# coding: utf-8
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
#  你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


class Solution(object):
    def rotate(self, matrix):
        """
        [   0,1,2
        0  [1,2,3],
        1  [4,5,6],
        2  [7,8,9]
        ],
        ----->(0,0)(2,2)  (0,1)(1,2)  (1,0)(2,1)
                [
          [9,6,3],
          [8,5,2],
          [7,4,1]
        ],
        ----->
                [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ],
        solution:
            先讲数组沿对角线对折，然后在折
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        clos = len(matrix[0])

        for i in range(rows-1):  # 对角转换
            for j in range(clos-i-1):
                t = matrix[i][j]
                matrix[i][j] = matrix[rows-j-1][clos-i-1]
                matrix[rows - j - 1][clos - i - 1] = t

        for i in range(rows/2):
            for j in range(clos):
                t = matrix[i][j]
                matrix[i][j] = matrix[rows-i-1][j]
                matrix[rows - i - 1][j] = t


if __name__ == '__main__':
    matirx = [
      [5, 1, 9, 11],
      [2, 4, 8, 10],
      [13, 3, 6, 7],
      [15, 14, 12, 16]
    ]
    Solution().rotate(matirx)
    for i in matirx:
        print i