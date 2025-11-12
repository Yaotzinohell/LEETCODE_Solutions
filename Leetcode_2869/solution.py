class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.reverse()
        collect = set()
        count=0
        for num in nums:
            count+=1
            if num <= k:
                collect.add(num)
            if len(collect)==k:
                return count