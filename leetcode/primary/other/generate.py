# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 19:36
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : generate.py
# @Software: PyCharm
'''
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1],
[1,5,10,10,5,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return None
        if numRows == 1:
            return [[1]]

        res = [[1], [1, 1]]

        for i in range(2, numRows):
            pre_line = res[-1]
            new_line = []
            i = 0
            for j in pre_line:
                new_line.append(i + j)
                i = j
            new_line.append(1)
            res.append(new_line)

        return res


if __name__ == '__main__':
    print(Solution().generate(5))