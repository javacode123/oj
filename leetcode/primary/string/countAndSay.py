# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 2:39 PM
# @Author  : zhang_jia_luo@foxmail.com
# @File    : countAndSay.py
# @Software: PyCharm
"""
1.     1
2.     11
3.     21
4.     1211
5.     111221

对上一个进行报数，2：一个一 11，3：两个一 21，4：一个二一个一 1211，5：一个一一个二两个一 111221

示例 1:
    输入: 1
    输出: "1"
示例 2:
    输入: 4
    输出: "1211"
"""


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype:
        """
        res = ['1']
        if n < 1:
            return None
        if n == 1:
            return '1'

        for i in range(n-1):
            res = self.process(res)

        return ''.join(res)

    def process(self, res):
        process_res = []
        count, cur_c = 0, 0

        for _ in res:
            if _ == cur_c:
                count = count + 1
            else:
                process_res.append(str(count))
                process_res.append(cur_c)
                count = 1
                cur_c = _

        process_res.append(str(count))
        process_res.append(cur_c)

        return process_res[2:]


if __name__ == '__main__':

   for i in range(1, 5):
       print(Solution().countAndSay(i))
