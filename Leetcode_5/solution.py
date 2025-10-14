class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest = ''
        for i in range(n):
            for j in range(i+1,n+1):
                res = s[i:j]
                if res == res[::-1]:
                    if len(res) > len(longest):
                        longest = res
        return longest