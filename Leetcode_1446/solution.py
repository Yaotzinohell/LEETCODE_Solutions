class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        streak=1
        maximum=1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                streak+=1
                continue
            maximum = max(maximum,streak)
            streak=1
        maximum = max(maximum,streak)
        return maximum