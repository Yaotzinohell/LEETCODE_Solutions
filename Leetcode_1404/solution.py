class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        decimal = int(s, 2)
        step_count = 0

        if decimal == 1:
            return step_count

        print(decimal)
        
        while decimal!=1:
            if decimal % 2 == 0:
                decimal //= 2
                step_count+= 1
            else:
                decimal += 1
                step_count+=1
        
        return step_count