class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remember = []
        while n!=1:
            if n not in remember:
                remember.append(n)
                lst = list(str(n))
                sum=0
                for i in lst:
                    sum+=int(i)**2
                n=sum
            else:
                return False
        return True
        