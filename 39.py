#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/4 19:55
# @File    : 39.py
# @Address : https://leetcode.com/problemset/top-100-liked-questions/

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
1.所有数字（包括 target）都是正整数。
2.解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        result = []
        path = []
        self.__dfs(path, candidates, size, target, 0, result)
        return result

    def __dfs(self, path, candidates, size, target, begin, result):
        if target == 0:
            result.append(path[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.__dfs(path, candidates, size, residue, index, result)
            path.pop()


solution = Solution()
candidates = [2,3,6,7]
target = 7
result = solution.combinationSum(candidates, target)
print(result)