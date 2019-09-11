#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/11 18:59
# @File    : 42.py
# @Address : https://leetcode-cn.com/problems/trapping-rain-water/

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


# 暴力解法，对数组中每个元素计算当前元素能接的雨水数量，叠加
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         size = len(height)
#         if size <= 1:
#             return 0
#         abs = 0
#         highest_index = 0
#         highest = 0
#         for i in range(size):
#             if height[i] > highest:
#                 highest_index = i
#                 highest = height[i]
#         for i in range(size):
#             max_side = 0
#             if i <= highest_index:
#                 max_side = max(height[:i+1])
#             else:
#                 max_side = max(height[i:])
#             abs += max_side - height[i]
#         return abs

# 动态规划，记下每个元素的最大左值和最大右值
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size <= 1:
            return 0
        abs = 0
        left_max, right_max = [0 for _ in range(size)], [0 for _ in range(size)]
        i = 1
        left_max[0] = height[0]
        while i < size:
            left_max[i] = max(left_max[i-1], height[i])
            i += 1
        i = size - 2
        right_max[size-1] = height[-1]
        while i >= 0:
            right_max[i] = max(right_max[i+1], height[i])
            i -= 1
        for i in range(size):
            abs += min(left_max[i], right_max[i]) - height[i]
        return abs


solution = Solution()
height = [2,0,2]
result = solution.trap(height)
print(result)