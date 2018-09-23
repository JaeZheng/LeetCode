# import re
#
#
# class Solution:
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         str = str.lstrip(" ")
#         if len(str) == 0:
#             return 0
#         if str=="-" or str=="+" or (str[0]=="+" and str[1]=="-") or (str[0]=="-" and str[1]=="+"):
#             return 0
#         # 确定第一个字符是否为负号或数字
#         first_pattern = "^\-|\+|\d"
#         if re.match(first_pattern, str[0]) is None:
#             return 0
#
#         # 匹配出第一个数字
#         num_pattern = "^\+\d*|\-\d*|\d+"
#         start, end = re.match(num_pattern, str).span()
#         str_tmp = str[start:end]
#         # 特殊样例，只有负号
#         if str_tmp == "-" or str_tmp == "+":
#             return 0
#         if str_tmp[0] == "+":
#             str_tmp = str_tmp[1:]
#         num = int(round(float(str_tmp)))
#         if str_tmp[0] == "-":
#             if num < -2**31:
#                 return -2**31
#         else:
#             if num > 2**31 -1:
#                 return 2**31 -1
#         return num
#
# s = Solution()
# a = "+413"
# b = s.myAtoi(a)
# print(b)

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        found = False
        result = 0
        sign = 1
        for c in str:
            if not found and c == " ":
                continue
            elif not found and c == "-":
                sign = -1
                found  = True
            elif not found and c == "+":
                found = True
            elif c.isdigit():
                found = True
                result = result*10 + int(c)
                if sign == 1 and result > 2**31-1:
                    return 2**31-1
                if sign == -1 and result > 2**31:
                    return -2**31
            else:
                break
        return sign * result
