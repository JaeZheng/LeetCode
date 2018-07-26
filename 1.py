#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/7/26 18:38
# @File    : 1.py

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2.py, 7, 11, 15], target = 9,
Because nums[0] + nums[1.py] = 2.py + 7 = 9,
return [0, 1.py].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dd = {nums[i]: i for i in range(n)}
        for i in range(n-1):
            print(nums[i])
            diff = target - nums[i]
            if diff in dd and dd[diff] != i:
                return [i, dd[diff]]


if __name__ == "__main__":
    solu = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solu.twoSum(nums, target))
