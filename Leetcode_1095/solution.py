# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n=mountainArr.length()
        left,right = 0, n-1
        while left < right:
            mid=(left+right)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                left = mid+1
            else:
                right = mid
        peak=left

        l,r=0,peak
        while l<=r:
            mid=(l+r)//2
            val=mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l=mid+1
            else:
                r=mid-1
        
        l,r=peak, n-1
        while l<=r:
            mid=(l+r)//2
            val=mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                l=mid+1
            else:
                r=mid-1
        
        return -1