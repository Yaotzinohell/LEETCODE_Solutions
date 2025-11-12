class Solution(object):
    def letterCombinations(self, digits):
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        if not digits:
            return []
        res = []
        def back(comb, index):
            if index == len(digits):
                res.append(comb)
                return
            letters = phone[digits[index]]
            for char in letters:
                back(comb+char, index+1)
        back("",0)
        return res