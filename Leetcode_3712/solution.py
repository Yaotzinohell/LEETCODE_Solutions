class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = {}
        total=0
        for num in nums:
            hash_map[num] = hash_map.get(num,0)+1
        for key,value in hash_map.items():
            if hash_map[key]%k==0:
                total += (key*value)

        return total