# 巧解
# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if len(s) == 0:
#             return True
#         if len(s)%2 != 0:
#             return False
#         while "()" in s or "[]" in s or "{}" in s:
#             s = s.replace("()","").replace("[]","").replace("{}","")
#         if s == "":
#             return True
#         else:
#             return False

# 出栈入栈的思路
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0
