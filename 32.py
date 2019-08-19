#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/8/19 16:18
# @File    : 32.py
# @Address : https://leetcode.com/problems/longest-valid-parentheses/



"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


# 出栈入栈的思路，但出入栈的是当前已经满足匹配的长度
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        stack = [0]
        longest = 0
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2  # 这一步很关键，记录当前已经满足的最大长度
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest


solution = Solution()
s = ")())"
result = solution.longestValidParentheses(s)
print(result)

