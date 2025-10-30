class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            columnNumber-=1
            remainder = columnNumber%26
            result.append(chr(remainder+ord('A')))
            columnNumber//=26
        
        return ''.join(reversed(result))