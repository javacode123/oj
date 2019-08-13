# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 12:41
# @Author  : Shark
# @mail    : zhang_jia_luo@foxmail.com
# @File    : conutPrime.py
# @Software: PyCharm


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)


if __name__ == '__main__':
    print(Solution().countPrimes(10))