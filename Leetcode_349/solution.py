class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1,n2=set(nums1),set(nums2)
        res=[]
        for num in n1:
            if num in n2:
                res.append(num)
        return res