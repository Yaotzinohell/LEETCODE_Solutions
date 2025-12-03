class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = max(nums)
        for i in range(maxi+1):
            count=0
            for num in nums:
                if num>=i:
                    count+=1
            if count == i:
                return i
        return -1