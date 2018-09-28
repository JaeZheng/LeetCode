#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/28 15:47
# @File    : 29.py


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        sign = False
        if dividend < 0:
            sign = not sign
            dividend = -dividend
        if divisor < 0:
            sign = not sign
            divisor = -divisor
        if dividend < divisor:
            return 0

        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                result += i
                i = i << 1
                tmp = tmp << 1

        if sign:
            result = -result
        return min(max(-2147483648, result), 2147483647)


s = Solution()
dividend, divisor = -2147483648, -1
# dividend, divisor = 1,1
a = s.divide(dividend, divisor)
print(a)
