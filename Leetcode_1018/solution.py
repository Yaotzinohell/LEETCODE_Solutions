class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        x=0
        answer=[]
        for num in nums:
            new_num = x*2 + num
            if new_num%5==0:
                answer.append(True)
            else:
                answer.append(False)
            x=new_num
        
        return answer