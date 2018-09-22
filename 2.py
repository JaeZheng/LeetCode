#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/7/26 19:36
# @File    : 2.py

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2.py -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1, str_l2 = "", ""
        while l1:
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:
            str_l2 += str(l2.val)
            l2 = l2.next
        num_l1 = int(str_l1[::-1])
        num_l2 = int(str_l2[::-1])
        str_l3 = str(num_l1 + num_l2)
        return list(map(int, str_l3))

