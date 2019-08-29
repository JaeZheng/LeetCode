#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/8/29 10:18
# @File    : 36.py
# @Address : https://leetcode.com/problems/valid-sudoku/

"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

示例 2:
输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
"""

"""
思路：首先想到暴力破解，直接遍历所有情况。然而时间空间复杂度都偏高。
官方题解建议：只遍历81个数一次，记录行、列、子盒的出现情况，如果有重复就是false
"""

import numpy as np


class Solution(object):
    # def isValidSudoku(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: bool
    #     """
    #     board = np.array(board)
    #     for i in range(9):
    #         row = board[i]
    #         row_string = "".join(row)
    #         col = board[:, i]
    #         col_string = "".join(col)
    #         for i in range(1, 10):
    #             if row_string.count(str(i)) > 1:
    #                 return False
    #             if col_string.count(str(i)) > 1:
    #                 return False
    #
    #     for i in range(3):
    #         for j in range(3):
    #             box = np.reshape(board[i*3:i*3 + 3, j*3:j*3 + 3], (1, 9))
    #             box_string = "".join(box[0].tolist())
    #             for k in range(1, 10):
    #                 if box_string.count(str(k)) > 1:
    #                     return False
    #     return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 初始化
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # 遍历每个数
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    box_index = (i//3) * 3 + j//3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


solution = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board))