#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/14 23:23
# @File    : 56.py
# @Address : https://leetcode-cn.com/problems/merge-intervals/

"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        result = []
        left = sorted([x[0] for x in intervals])
        right = sorted([x[1] for x in intervals])
        i, j, cur_l, cur_r = 1, 0, left[0], right[0]
        while i < len(left):
            # 有重叠区域，更新右值到下一个区间右值
            if cur_r >= left[i]:
                j += 1
                cur_r = right[j]
            elif cur_r < left[i]:  # 出现空隙，将当前区间加入结果，更新左值和右值到当前i值所指的子区间
                result.append([cur_l, cur_r])
                j = i
                cur_l = left[i]
                cur_r = right[j]
            i += 1
            if i == len(left):
                result.append([cur_l, cur_r])
        return result


solution = Solution()
intervals = [[1,4],[4,5]]
result = solution.merge(intervals)
print(result)