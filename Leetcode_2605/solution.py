class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        match=[]
        for num in nums1:
            if num in nums2:
                match.append(num)
        if match:
            return min(match)
        else:
            n1, n2 = min(nums1),min(nums2)
            if n1>n2:
                return n2*10 + n1
            else:
                return n1*10 + n2