class Solution(object):
    def myAtoi(self,s):
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        result *= sign
        MIN, MAX = -2**31, 2**31 - 1
        if result < MIN:
            return MIN
        elif result > MAX:
            return MAX
        else:
            return result