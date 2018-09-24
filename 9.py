class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_conv = str(x)[::-1]
        return x_conv == str(x)

s = Solution()
print(s.isPalindrome(10))