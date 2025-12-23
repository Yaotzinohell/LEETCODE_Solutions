class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        count = 1
        final_sum=0
        for i in range(len(n)):
            if count%2!=0:
                final_sum+=int(n[i])
            else:
                final_sum-=int(n[i])
            count+=1
        return final_sum