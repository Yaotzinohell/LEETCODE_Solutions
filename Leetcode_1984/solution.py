class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        
        nums.sort()

        res = float('inf')
        for i in range(len(nums) - k+1):
            vals = nums[i+k-1]-nums[i]
            res = min(res,vals)
        
        return res