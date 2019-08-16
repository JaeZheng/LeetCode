#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/8/16 15:38
# @File    : 31.py
# @Address : https://leetcode.com/problems/next-permutation/

"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


"""
思路：从右往左寻找第一个出现升序的数，将这个数与其后面子数组中最小的大于该数的值互换，
然后对后面子数组进行升序排序，注意：题目要求不需要返回数组，而是在原地修改
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur = len(nums)-1
        while cur>0:
            if nums[cur] > nums[cur-1]:
                sub_cur = cur
                for i in range(cur, len(nums)-1):
                    if nums[sub_cur+1] > nums[cur-1]:
                        sub_cur += 1
                    else:
                        break
                self.swap(nums, cur-1, sub_cur)  # 将当前值与后面子数组中最小的大于该值的数交换
                self.reverse(nums, cur, len(nums)-1)  # 将后面子数组升序排序
                break
            else:
                cur -= 1
        if cur == 0:
            self.reverse(nums, cur, len(nums)-1)
        print(nums)

    # 交换数组中的两个值
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    # 将一个数组反转
    def reverse(self, nums, begin, end):
        left, right = begin, end
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1


solution = Solution()
nums = [3,2,1]
solution.nextPermutation(nums)
