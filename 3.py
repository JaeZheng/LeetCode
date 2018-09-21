class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        if len(s) <= 1:
            max_len = len(s)
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    if j - i > max_len:
                        max_len = j - i
                    break
                elif j == len(s)-1:
                    if max_len < j - i + 1:
                        max_len = j - i + 1
        return max_len

s = Solution()
a = s.lengthOfLongestSubstring("bwf")
print(a)