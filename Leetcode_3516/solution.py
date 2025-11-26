class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        p1,p2 = abs(x-z), abs(y-z)
        if p1 > p2:
            return 2
        elif p2 > p1:
            return 1
        elif p1 == p2:
            return 0