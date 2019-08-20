#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/8/20 11:31
# @File    : 33.py
# @Address : https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""

"""
思路：二分搜索。先二分搜素找出轴值（数组最小值），再二分搜索找出target值。
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 寻找轴值，返回轴值的下标
        def findPivot(nums):
            left, right = 0, len(nums) - 1
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = int((left + right) / 2)
                if nums[pivot] > nums[pivot + 1]:  # 出现降序，即为分界
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:  # 左数组有序，因此轴值在左数组
                        right = pivot - 1
                    else:  # 左数组无序，因此轴值在右数组
                        left = pivot + 1
            return 0  # 找不到符合要求的轴值，说明为升序数组，最小值下标为0

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

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        pivot = findPivot(nums)  # 先用二分查找找出轴值下标
        if pivot == 0:  # 升序排序数组
            return findTarget(0, n-1)
        if target < nums[0]:  # 小于左数组最小值，在右数组中搜索
            return findTarget(pivot, n-1)
        else:
            return findTarget(0, pivot)


solution = Solution()
nums = [5,1,3]
target = 0
result = solution.search(nums, target)
print(result)
