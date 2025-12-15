class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        for i in range(len(s)-k+1):
            if len(set(s[i:i+k]))==1:
                ch = s[i]

                if i>0 and s[i-1]==ch:
                    continue
                
                if i+k<len(s) and s[i+k]==ch:
                    continue

                return True
        return False