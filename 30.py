#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/4/12 9:11
# @File    : 30.py
# @Address : https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1
        word_len = len(words[0])
        result = []
        for i in range(word_len):
            start = i
            cur = i
            tmp_dict = defaultdict(int)
            while cur+word_len <= len(s):
                tmp_word = s[cur:cur+word_len]
                if tmp_word in words:
                    tmp_dict[tmp_word] += 1
                    if tmp_dict[tmp_word] > word_dict[tmp_word]:
                        tmp_dict.clear()
                        start += word_len
                        cur = start
                        continue
                    if len(tmp_dict) == len(word_dict):
                        flag = True
                        for k, v in tmp_dict.items():
                            if v != word_dict[k]:
                                flag = False
                        if flag:
                            result.append(start)
                            start += word_len
                            cur = start
                            tmp_dict.clear()
                            continue
                    cur += word_len
                else:
                    start = cur + word_len
                    cur = start
                    tmp_dict.clear()
        return result


solution = Solution()
# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo","barr","wing","ding","wing"]
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
a = solution.findSubstring(s, words)
print(a)
