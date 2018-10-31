#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/10/31 17:51
# @File    : max_sub.py


def max_sub(A):
    size = len(A)
    dp = [0 for i in range(size)]
    dp[0] = A[0]
    for i in range(1, size):
        dp[i] = max(dp[i-1] + A[i], A[i])
    return max(dp)

A = [-2, 11, -4, 13, -5, 2, -5, -3, 12, -9]
print(max_sub(A))