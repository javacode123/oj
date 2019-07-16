# coding: utf-8
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) == 0:
            return s

        start, end = 0, len(s)-1

        while start < end:
            t = s[start]
            s[start] = s[end]
            s[end] = t
            start += 1
            end -= 1

