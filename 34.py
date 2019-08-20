#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/8/20 15:22
# @File    : 34.py
# @Address : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""

"""
思路：二分查找。先找到第一个满足的target的下标，在对target左右两侧进行二分查找，更新左值和右值
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findTarget(left, right):
            while left <= right:
                pivot = int((left + right) / 2)
                # 刚好是轴值
                if target == nums[pivot]:
                    return pivot
                if target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            return -1

        idx = [-1, -1]
        n = len(nums)
        if n == 0:
            return idx
        if n == 1:
            return [0, 0] if nums[0] == target else idx
        first = findTarget(0, n-1)
        if first == -1:
            return idx
        else:
            idx = [first, first]
            l_left, l_right, r_left, r_right = 0, first-1, first+1, n-1
            while l_left <= l_right:  # 查找左数组
                left_result = findTarget(l_left, l_right)
                if left_result != -1:
                    idx[0] = left_result
                    l_right = left_result-1
                else:
                    break
            while r_left <= r_right:  # 查找右数组
                right_result = findTarget(r_left, r_right)
                if right_result != -1:
                    idx[1] = right_result
                    r_left = right_result + 1
                else:
                    break
        return idx


solution = Solution()
nums = [8,8,8]
target = 8
result = solution.searchRange(nums, target)
print(result)



