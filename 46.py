#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/12 17:22
# @File    : 46.py
# @Address : https://leetcode-cn.com/problems/permutations/

"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
思路：回溯法。固定一个位置的数字，交换对应位置的数字，直到位置相同，不用交换，回溯。
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_track(first=0):
            # 所有交换的可能情况已经遍历过，到达最后一个，此时加入结果
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # 交换first和当前索引i的数
                nums[first], nums[i] = nums[i], nums[first]
                # 进一步搜索
                back_track(first+1)
                # 回溯，返回到交换前的状态
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        back_track()
        return output


solution = Solution()
nums = [1,2,3]
result = solution.permute(nums)
print(result)
