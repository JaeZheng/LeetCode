# 找出一个字符串中最长的回文子串
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 特例: 长度为1, 最长回文子串是它本身
        if len(s) < 2:
            return s
        self.res = ""
        for i in range(len(s)):
            # 从相同字符和相邻字符向左右两边拓展
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res


    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 如果大于历史存储的最大回文子串长度，则更新
        if right - left - 1 > len(self.res):
            self.res = s[left+1 : right]
