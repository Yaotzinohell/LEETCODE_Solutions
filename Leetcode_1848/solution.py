class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        result = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                result = min(result, abs(i-start))
        
        return result