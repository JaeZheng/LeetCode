#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/3/17 20:52
# @File    : 1011.py
# @Address : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left+right)/2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left


S = Solution()
weights = [1,2,3,1,1]
D = 4
answer = S.shipWithinDays(weights, D)
print(answer)