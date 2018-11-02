#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/11/2 18:01
# @File    : 303.py
# @Address : https://leetcode.com/problems/range-sum-query-immutable/


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [i for i in nums]
        self.nums = nums
        for i in range(1, len(nums)):
            self.sum[i] = self.sum[i-1] + nums[i]
        print(self.sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j]-self.sum[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

nums = [-2, 0, 3, -5, 2, -1]
S = NumArray(nums)
a = S.sumRange(0, 5)
print(a)
