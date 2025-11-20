from collections import defaultdict
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff_dict = defaultdict(int)
        good_pair=0
        for i,val in enumerate(nums):
            diff = val-i

            good_pair+=diff_dict[diff]

            diff_dict[diff]+=1
        
        total_pair = (len(nums)*(len(nums)-1)//2)
        return total_pair-good_pair