class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        for num in nums:
            if i==0 or num > nums[i-1]:
                nums[i] = num
                i += 1
        return i