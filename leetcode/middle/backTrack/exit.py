# -*- coding: utf-8 -*-
# @Time    : 2019-08-25 15:40
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : exit.py
# @Software: PyCharm


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def back_track(arr, word, i, j):
            if not word:
                return True
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]) or arr[i][j] != word[0]:
                return False
            arr[i][j] = None
            res = back_track(arr, word[1:], i-1, j) or back_track(arr, word[1:], i+1, j) or back_track(arr, word[1:], i, j-1) or back_track(arr, word[1:], i, j+1)
            arr[i][j] = word[0]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if back_track(board, word, i, j):
                        return True

        return False


if __name__ == '__main__':
    print(Solution().exist([
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ], 'ABCCE'))

