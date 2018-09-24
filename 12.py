class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roma = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        s = ["0" for _ in base]
        result = ""
        for i in range(len(base)):
            tmp = int(num/base[i])
            if tmp == 0:
                continue
            else:
                num %= base[i]
                s[i] = str(tmp)
            result += int(s[i]) * roma[i]
        return result

s = Solution()
num = 1994
r = s.intToRoman(num)
print(r)