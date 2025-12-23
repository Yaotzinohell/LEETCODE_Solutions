class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        length = len(nums1)
        for i in range(length-1):
            swapped=False
            for j in range(length-i-1):
                if nums1[j]>nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
                    swapped=True
            if not swapped:
                break