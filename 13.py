class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic  = {"M":1000, "CM":900, "D":500, "CD":400, "C":100,
                "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        prev_value = total_value = 0
        for i in range(len(s)-1, -1, -1):
            int_val = dic[s[i]]
            if int_val < prev_value:
                total_value -= int_val
            else:
                total_value += int_val
            prev_value = int_val
        return total_value
