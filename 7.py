import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        s = str(x)
        result = ""
        flag = False
        if s[0]=="-":
            s = "".join(s[1:])
            flag = True
        s = "".join(s[::-1])
        if s[0]=="0":
            result = result + "".join(s[1:])
        else:
            result = result + s
        if flag:
            return -int(result) if -int(result)>=-math.pow(2,31) and -int(result)<math.pow(2,31)-1 else 0
        else:
            return int(result) if int(result)>=-math.pow(2,31) and int(result)<math.pow(2,31)-1 else 0

s = Solution()
a = s.reverse(123)
print(a)
