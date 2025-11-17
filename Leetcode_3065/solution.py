class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count,res=0,0
        for num in nums:
            if num >= k:
                count+=1
        res=len(nums)-count
        return res