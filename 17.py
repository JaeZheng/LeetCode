class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {"2":[i for i in "abc"], "3":[i for i in "def"], "4":[i for i in "ghi"],
                "5": [i  for i in "jkl"], "6": [i for i in "mno"], "7": [i for i in "pqrs"],
                "8": [i for i in "tuv"], "9": [i for i in "wxyz"]}
        result = [""]
        if len(digits) == 0:
            return []
        for digit in digits:
            chars = dict[digit]
            tmp = []
            for char in chars:
                tmp += [x+char for x in result]
            result = tmp
        return result
