#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/22 0:37
# @File    : 229.py
# @Address : https://leetcode-cn.com/problems/majority-element-ii/

"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:
输入: [3,2,3]
输出: [3]

示例 2:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
"""

"""
思路：摩尔投票法升级版。169题升级版。
超过1/3，即候选数不超过两个，第一遍遍历计数投票确定两个候选数，第二遍遍历确认频率大小，如果有小于等于1/3的，去掉。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [n for n in (cand1, cand2) if nums.count(n) > (len(nums)//3)]
