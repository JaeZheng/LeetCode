# import re
#
# class Solution:
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         a = re.match(p, s)
#         if a is None:
#             return False
#         start, end = a.span()
#         if end == len(s):
#             return True
#         else:
#             return False

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(2, len(p)+1):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"
        for i in range(1,len(s)+1):
            for j in range(1, len(p) + 1):
                if p[j-1] != "*":
                    dp[i][j] = dp[i-1][j-1] and (p[j-1]=="." or s[i-1]==p[j-1])
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2]=="." or s[i-1]==p[j-2]))

        return dp[-1][-1]


a = Solution()
s = "mississippi"
p = "mis*is*p*."
result = a.isMatch(s,p)
print(result)