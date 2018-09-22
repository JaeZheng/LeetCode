# class Solution:
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         len_s = len(s)
#         # print("len_s: " + str(len_s))
#         # 两列完整的列之间的间隔
#         jian = numRows-1
#
#         tmp = numRows + jian - 1
#         if tmp <= 0:
#             return s
#
#         tmp_a = int(len_s / (numRows + jian - 1))
#         #if tmp_a < 1:
#              #return s
#
#         tmp_b = len_s % (numRows + jian - 1)
#
#         width = tmp_a*jian if tmp_b==0 else tmp_a*jian+int(tmp_b/numRows)+tmp_b%numRows
#         arr = [[0 for col in range(width)] for row in range(numRows)]
#         # print(arr)
#         for i in range(numRows):
#             start = i
#             end = numRows - 1
#             idx = 0
#             while idx < width and start<len_s:
#                 arr[i][idx] = s[start]
#                 if i!=0 and i!=(numRows-1) and end+jian-i<len_s and idx+jian-i<width:
#                     # print(idx+jian-i)
#                     # print(end+jian-i)
#                     arr[i][idx+jian-i] = s[end+jian-i]
#                     end += 2*(numRows-1)
#                 idx += jian
#                 start += 2*(numRows-1)
#             # print(arr[i])
#         result = ""
#         for i in range(numRows):
#             for j in arr[i]:
#                 if j != 0:
#                     result += j
#         return result
#
# # s = Solution()
# # re = s.convert("PAYPALISHIRING", 5)
# # print(re)

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ["" for i in range(numRows)]
        i = 0
        flag = True
        for c in s:
            if i == 0:
                flag = True
            elif i == numRows-1:
                flag =False
            result[i] = result[i]+c
            if flag:
                i += 1
            else:
                i -= 1

        return "".join(result)

s = Solution()
a = s.convert("PAYPALISHIRING", 3)
print(a)