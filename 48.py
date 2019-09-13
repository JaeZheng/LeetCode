#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/13 12:05
# @File    : 48.py
# @Address : https://leetcode-cn.com/problems/rotate-image/

"""
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

"""
思路：在正方形四边依次旋转替换对应位置，比较困难的点是确认每次转换的索引
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        if n <= 1:
            return matrix
        n -= 1
        for i in range(int(n/2)+1):
            # print("i: ", i)
            for j in range(i, n-i):
                # print("j: ", j)
                matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] = \
                    matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]


solution = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution.rotate(matrix)
print(matrix)
