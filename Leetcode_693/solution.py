class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = ''
        while n > 0:
            binary = str(n & 1) + binary
            n >>= 1
        for i in range(1, len(binary)):
            if binary[i-1] == binary[i]:
                return False
        return True