class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s[i] in t:
                ind = t.index(s[i])
                #Removing the matched character
                t=t[ind+1:]
            else:
                return False
        return True