#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/11/2 17:06
# @File    : 198.py
# @Address : https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        houses = len(nums)
        if houses <= 1:
            return nums[0] if houses == 1 else 0
        dp = [0 for _ in range(houses)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, houses):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]


a = [2,1,1,2]
S = Solution()
b = S.rob(a)
print(b)
