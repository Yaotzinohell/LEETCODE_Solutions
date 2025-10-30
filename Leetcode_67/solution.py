class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_decimal = int(a,2)
        b_decimal = int(b,2)

        res = a_decimal+b_decimal
        return bin(res)[2:]