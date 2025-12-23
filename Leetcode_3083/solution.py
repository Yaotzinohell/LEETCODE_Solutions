class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rs=s[::-1]
        for i in range(len(s)-1):
            if s[i:i+2] in s and s[i:i+2] in rs:
                return True
        return False