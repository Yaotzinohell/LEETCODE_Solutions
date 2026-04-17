class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr_sum = sum(nums)

        if arr_sum % k == 0:
            return 0
        else:
            return arr_sum % k