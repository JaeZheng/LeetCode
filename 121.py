#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/11/6 21:15
# @File    : 121.py
# @Address : https://leetcode.com/problems/best-time-to-buy-and-sell-stock

import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = sys.maxsize
        max_profit = 0
        for price in prices:
            if price < min_value:
                min_value = price
            if price - min_value > max_profit:
                max_profit = price - min_value
        return max_profit

S = Solution()
prices = [7,6,4,3,1]
a = S.maxProfit(prices)
print(a)