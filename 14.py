class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l_strs = len(strs)
        if l_strs == 0:
            return ""
        if l_strs == 1:
            return strs[0]

        l_max = min(len(str) for str in strs)
        for i in range(l_max):
            for j in range(1, l_strs):
                while strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0][:l_max]

s = Solution()
arr = ["dog","racecar","car"]
a = s.longestCommonPrefix(arr)
print(a)