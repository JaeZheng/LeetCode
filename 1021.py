#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/4/11 19:15
# @File    : 1021.py
# @Address : https://leetcode.com/problems/remove-outermost-parentheses/


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        left = 0
        right = 0
        result = ""
        start = 0
        for idx, s in enumerate(S):
            if s == "(":
                left += 1
            else:
                right += 1
            if left == right:
                result += S[start+1:idx]
                left = 0
                right = 0
                start = idx+1
        return result


solution = Solution()
S = "()()"
a = solution.removeOuterParentheses(S)
print(a)