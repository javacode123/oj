# coding: utf-8
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or needle == '':
            return 0
        try:
           return haystack.index(needle)
        except:
            return -1


if __name__ == '__main__':
    print(Solution().strStr('aaaaa', 'bba'))
