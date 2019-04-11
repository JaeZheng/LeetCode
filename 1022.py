#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/4/11 18:13
# @File    : 1022.py
# @Address : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = ""
        result = []
        tmp = 0
        self.BFS(root, s, result)
        for s in result:
            tmp += int(s, 2)
        return tmp

    def BFS(self, root, s, result):
        s += str(root.val)
        if not root.left and not root.right:
            result.append(s)
        if root.left:
            self.BFS(root.left, s, result)
        if root.right:
            self.BFS(root.right, s, result)
        return


