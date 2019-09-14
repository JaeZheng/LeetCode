#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/9/14 11:53
# @File    : 49.py
# @Address : https://leetcode-cn.com/problems/group-anagrams/

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""

"""
思路：对字符串按字典序排序后建立哈希表（暴力解）
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) <= 1:
            return [strs]
        dict_str = {}
        for s in strs:
            s_tmp = "".join((lambda x:(x.sort(), x)[1])(list(s)))
            if s_tmp not in dict_str:
                dict_str[s_tmp] = [s]
            else:
                dict_str[s_tmp].append(s)
        result = [x for x in dict_str.values()]
        return result


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strs)
print(result)
