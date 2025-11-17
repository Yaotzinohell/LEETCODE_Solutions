class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,item in freq.items():
            if item>1:
                return key