class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        n = len(nums[0])-1
        sorted_matrix=[]
        score=0
        for num in nums:
            num = sorted(num)
            sorted_matrix.append(num)
        while n!=-1:
            m=0
            for num in sorted_matrix:
                m = max(m,num[n])
            print(m)
            score+=m
            n-=1
        return score
