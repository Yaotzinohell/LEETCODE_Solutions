class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        q=n//7
        r=n%7
        loop=1
        end=7
        total=0
        while q!=0:
            for i in range(loop,end+loop):
                total+=i
            q-=1
            loop+=1
        if r > 0:
            for i in range(loop,r+loop):
                total+=i
        
        return total