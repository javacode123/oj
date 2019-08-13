# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:41
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm
import sys

class Solution:
    def find_num(self, a, b):
        length = len(a)

        count = [0]*length
        for m in range(length):
            temp = 0
            for i in range(length):
                # print("the i is ", i)
                flag = a[i]
                # print("the first flag is ", flag)
                for j in range(temp, length):
                    # print("the length is ", length)
                    # print("the temp is ", j)
                    # print("the test num is", b[temp])
                    if flag == b[j]:
                        # print("the like num is ", flag)
                        count[m] += 1
                        temp = j+1
                        continue
        return length-max(count)


if __name__ == '__main__':
    for line in sys.stdin:  # 读作数组
        s = Solution()
        n = line.split()
        a_arr = [int(i) for i in sys.stdin.readline().strip().split()]
        b_arr = [int(i) for i in sys.stdin.readline().strip().split()]
        print(s.find_num(a_arr, b_arr))