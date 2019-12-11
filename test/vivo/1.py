# -*- coding: utf-8 -*-
# @Time    : 2019-09-22 15:56
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : 1.py
# @Software: PyCharm


'''
 Welcome to vivo !
'''

def solution(step_list):
    if not step_list:
        return 0

    count = 0
    temp = [0 for _ in range(len(step_list))]

    for index, num in enumerate(step_list):
        if index != 0:
            for i in range(index):
                if temp[i] + step_list[i] >= index:
                    temp[index] = temp[i] + 1
                    break

    return temp[-1]


step_list = [int(i) for i in input().split()]
print(solution(step_list))
