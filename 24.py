#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/26 15:15
# @File    : 24.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            cur.next.next.next, cur.next.next, cur.next, cur = cur.next, cur.next.next.next, cur.next.next, cur.next
        return dummy.next
