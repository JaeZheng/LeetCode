#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/26 16:27
# @File    : 27.py

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        cnt = nums.count(val)
        for i in range(cnt):
            nums.remove(val)
        return len(nums)

