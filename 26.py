#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/26 16:09
# @File    : 26.py

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tail = 0
        for i in range(1, len(nums)):
            if nums[tail] != nums[i]:
                tail += 1
                nums[tail] =nums[i]
        return tail+1

s = Solution()
nums = [1,1,2]
print(s.removeDuplicates(nums))
print(nums)