# coding: utf-8
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # 行, 列排查
        for i in range(9):
            row = {str(_): 0 for _ in range(10)}
            clo = {str(_): 0 for _ in range(10)}
            for j in range(9):
                if row.get(board[i][j], None) is not None:
                    if row.get(board[i][j]) == 1:
                        return False
                    else:
                        row[board[i][j]] =1
                if clo.get(board[j][i], None) is not None:
                    if clo.get(board[j][i]) == 1:
                        return False
                    else:
                        clo[board[j][i]] = 1

        # 3 * 3 排查
        for i in range(3):
            for j in range(3):  # 9 块
                t = {str(_): 0 for _ in range(10)}
                for k in range(3):  # 3 行
                    for l in range(3):  # 3 列

                        if t.get(board[i * 3 + k][j * 3 + l], None) is not None:
                            if t.get(board[i * 3 + k][j * 3 + l]) == 1:
                                return False
                            else:
                                t[board[i * 3 + k][j * 3 + l]] = 1

        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))