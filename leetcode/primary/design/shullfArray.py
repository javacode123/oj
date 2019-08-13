# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 16:40
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : shullfArray.py
# @Software: PyCharm
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arry = nums
        self.origin = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.arry = self.origin
        self.origin = list(self.origin)
        return self.arry

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.arry)):
            j = random.randrange(i, len(self.arry))
            self.arry[i], self.arry[j] = self.arry[j], self.arry[i]

        return self.arry
