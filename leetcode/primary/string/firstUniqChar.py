# coding: utf-8
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = collections.OrderedDict()
        for i in range(len(s)):
            if dict_s.get(s[i], None) is None:
                dict_s[s[i]] = i
            else:
                dict_s[s[i]] = -1

        for k in dict_s.keys():
            if dict_s.get(k) != -1:
                return dict_s.get(k)

        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar('loveleetcode'))