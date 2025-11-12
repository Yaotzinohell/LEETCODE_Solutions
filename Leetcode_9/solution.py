class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            y = [int(k) for k in str(x)]
            z = y[::-1]
            if y == z:
                return True
            return False