# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return ss
        res = set()
        queue = [('', ss)]

        while queue:
            connect, s = queue.pop()
            if not s:
                res.add(connect)
            else:
                for i, c in enumerate(s):
                    queue.append((connect + c, s[:i] + s[i + 1:]))

        return sorted(list(res))