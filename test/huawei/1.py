# -*- coding: utf-8 -*-
# @Time    : 2019-08-28 19:24
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : 1.py
# @Software: PyCharm
import sys

if __name__ == '__main__':
    for line in sys.stdin:  # 读作数组
        input_num = int(line.split()[0])  # 输入

        x = 0
        count = 0
        for i in range(1, int(input_num / 3)):
            x = (input_num * input_num - 2 * input_num * i) / (2 * input_num - 2 * i)
            if i <= x and x <= input_num-i-x and x%1 == 0:
                count += 1

        print(count)
