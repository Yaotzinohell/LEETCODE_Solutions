from collections import Counter
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = []
        freq = dict(Counter(nums))
        for k,v in freq.items():
            if freq[k]>1:
                arr.append(k)
        return arr