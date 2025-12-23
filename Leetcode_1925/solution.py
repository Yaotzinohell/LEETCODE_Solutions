class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                if a!=b:
                    c=a**2 + b**2
                    s = int(math.sqrt(c))
                    if s*s == c and s<=n:
                        count+=1
        return count