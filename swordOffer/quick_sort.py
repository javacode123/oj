# -*- coding: utf-8 -*-
# @Time    : 2019-09-09 15:02
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : quick_sort.py
# @Software: PyCharm


def helper(arr, low, high):
    temp = arr[low]

    while low < high:
        while low < high and arr[high] >= temp:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < temp:
            low += 1
        arr[high] = arr[low]

    arr[low] = temp
    return low


if __name__ == '__main__':
    arr = [6, 3, 1, 5, 2, 0]
    k = 3
    low, high = 0, len(arr)-1

    while True:
        mid = helper(arr, low, high)
        if mid == k:
            break
        elif mid > k:
            high = mid-1
        else:
            low = mid+1

    print(arr)
