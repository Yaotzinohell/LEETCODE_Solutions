class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        cyc = 2 * numRows - 2
        ans = [""] * numRows
        for i in range(n):
            j = i % cyc
            ans[j if j < numRows else cyc - j] += s[i]
        return "".join(ans)