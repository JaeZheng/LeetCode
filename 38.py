#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/17 15:11
# @File    : 38.py
# @Address : https://leetcode-cn.com/problems/count-and-say/

"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""

"""思路：暴力破解。按序计数。"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        current_str = "1"
        for i in range(1, n):
            result = ""
            count = 0
            current_val = current_str[0]
            for i in current_str:
                if i == current_val:
                    count += 1
                else:
                    result += str(count) + current_val
                    current_val = i
                    count = 1
            result += str(count) + current_val
            current_str = result
        return current_str


solution = Solution()
result = solution.countAndSay(5)
print(result)