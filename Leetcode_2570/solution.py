class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        hash_table = {}
        ans= []
        for num in nums1+nums2:
            hash_table[num[0]] = hash_table.get(num[0], 0) + num[1]
        
        for key,values in sorted(hash_table.items()):
            ans.append([key,values])

        return ans