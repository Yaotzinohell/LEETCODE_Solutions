class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = []
        n = len(nums)
        for i in range(n):
            diff.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        return diff