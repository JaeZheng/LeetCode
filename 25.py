#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/26 15:33
# @File    : 25.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 数组看待，每k个一次处理，效率较差，因为要2次遍历
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        dummy = p = ListNode(0)
        tmp = []

        # 第一次遍历，得到链表长度
        length = 0
        r = head
        while r:
            r = r.next
            length += 1

        # 每k个一次插值
        while count < k <= length:
            tmp.append(head.val)
            head = head.next
            count += 1
            if count == k:
                count = 0
                length -= k
                while len(tmp):
                    p.next = ListNode(tmp.pop())
                    p = p.next
        p.next = head
        return dummy.next