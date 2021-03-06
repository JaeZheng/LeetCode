#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/14 16:29
# @File    : 55.py
# @Address : https://leetcode-cn.com/problems/jump-game/

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""

"""
思路：贪心算法，遍历一遍数组就可以，每次都取当前索引下能走的最大的步伐。
如果某一个起跳的格子可以跳跃的距离是3，那么表示后面3个格子都可以作为起跳点。
可以对每一个能作为起跳的格子都尝试跳一次，把能跳到最远的距离不断更新。
如果可以一直跳到最后，就成功了。
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        current_idx = 0
        for i in range(n):
            if i > current_idx:
                return False
            current_idx = max(current_idx, i+nums[i])
            if current_idx == n-1:
                return True
        return True


solution = Solution()
nums = [3,2,1,0,4]
result = solution.canJump(nums)
print(result)
