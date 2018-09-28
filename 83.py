#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/28 16:53
# @File    : 83.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         a = []
#         while head:
#             if head.val not in a:
#                 a.append(head.val)
#             head = head.next
#         a = list(set(a))
#         dummy = l = ListNode(0)
#         for i in a:
#             l.next = ListNode(i)
#             l = l.next
#         return dummy.next

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        b = a = head
        while head:
            if head.val == a.val:
                a.next = head.next
            else:
                a = a.next
            head = head.next
        return b

