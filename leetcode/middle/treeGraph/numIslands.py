# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:22
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : numIslands.py
# @Software: PyCharm


class Solution(object):

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        rows = len(grid)
        clos = len(grid[0])

        for r in range(rows):
            for c in range(clos):
                if grid[r][c] == '1':
                    res += 1
                    self.dfs(grid, r, c)  # 周围的1置0

        return res


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
    print(Solution().numIslands(grid))
