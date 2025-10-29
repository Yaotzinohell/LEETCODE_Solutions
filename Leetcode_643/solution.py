class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        first_sum = sum(nums[:k])
        max_sum = first_sum

        for i in range(k,n):
            first_sum+=nums[i]-nums[i-k]
            max_sum = max(max_sum, first_sum)
        
        return float(max_sum)/k