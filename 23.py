#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/26 15:06
# @File    : 23.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result_arr = []
        for list in lists:
            while list:
                result_arr.append(list.val)
                list = list.next

        result_arr = sorted(result_arr)

        dummy = head = ListNode(0)
        for i in result_arr:
            head.next = ListNode(i)
            head = head.next

        return dummy.next
