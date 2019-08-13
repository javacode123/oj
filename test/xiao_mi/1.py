#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

# 1(2(3,4(,5)),6(7,))

def solution(input):
    stack = []

    for i in input:
        if i not in ['(', ')', ',']:
            stack.append(i)

    return ''.join(str(_) for _ in stack)


# ******************************结束写代码******************************


try:
    _input = input()
except:
    _input = None

res = solution(_input)

print(res + "\n")