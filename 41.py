#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/5 10:49
# @File    : 41.py
# @Address : https://leetcode.com/problems/first-missing-positive/


"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i] = 1
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        for i in range(1,n):
            if nums[i] > 0:
                return i
        if nums[0]>0:
            return n
        return n+1


solution = Solution()
nums = [1,2]
result = solution.firstMissingPositive(nums)
print(result)
