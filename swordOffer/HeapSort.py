# -*- coding: utf-8 -*-
# @Time    : 2019-08-26 13:54
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : HeapSort.py
# @Software: PyCharm


def adjust_down(l, start, end):
    temp = l[start]
    i = start
    j = start * 2

    while j < end:
        if j < end and l[j] < l[j+1]:
            j = j + 1
        if l[j] > temp:  #小的向下移动
            l[i] = l[j]
            i = j
            j = i * 2
        else:
            break
    l[i] = temp


def heap_sort(l):
    size = len(l) - 1
    index = size // 2

    for i in range(index):
        adjust_down(l, index-i, size)

    for i in range(size):
        l[1], l[size-i] = l[size-i], l[1]
        adjust_down(l, 1, size-i-1)


if __name__ == '__main__':
    l = [0, 6, 5, 4, 3, 2, 1]
    heap_sort(l)
    print(l[1:])



"""
def adjust_down(l, start, end):  #下标为 start 的数据向下调整
    temp = l[start]
    i = start
    j = start * 2

    while j <= end:
        if j < end and l[j] < l[j+1]:
            j = j+1
        if l[j] > temp:
            l[i] = l[j]
            i = j
            j = i * 2
        else:
            break
    l[i] = temp


def heap_sort(l):  # l 的第一位补充了 0
    size = (len(l) - 1)
    index = size // 2

    for i in range(index):  #初始化堆
        adjust_down(l, index-i, size)

    for i in range(size):
        l[1], l[size-i] = l[size-i], l[1]
        adjust_down(l, 1, size-i-1)

"""