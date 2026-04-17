class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        for i, val in enumerate(nums):
            if val not in dictionary:
                dictionary[val] = []
            dictionary[val].append(i)
        min_distance = float('inf')
        for key, value in dictionary.items():
            if len(value) >= 3:
                for i in range(len(value) - 2):
                    i, j, k = value[i], value[i+1], value[i+2]
                    distance = abs(i-j) + abs(j-k) + abs(k-i)
                    min_distance = min(min_distance, distance)
        if min_distance == float('inf'):
            return -1
        return min_distance