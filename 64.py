#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/19 15:40
# @File    : 64.py
# @Address : https://leetcode-cn.com/problems/minimum-path-sum/

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

"""
思路：动态规划，每一步都保存最小的
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid[0]), len(grid)
        for j in range(1, m):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, n):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i - 1][j]+grid[i][j], grid[i][j - 1]+grid[i][j])
        return grid[n - 1][m - 1]


solution = Solution()
grid = [[1]]
result = solution.minPathSum(grid)
print(result)