# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:41
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm

import sys


if __name__ == '__main__':
    for line in sys.stdin:  # 读作数组
        input_num = [int(_) for _ in line.split()]  # 输入
        print(input_num)