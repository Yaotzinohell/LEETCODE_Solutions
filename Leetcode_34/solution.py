class Solution(object):
    def searchRange(self, nums, target):
        pos=[]
        for i in range(len(nums)):
            if nums[i]==target:
                pos.append(i)
                break
        for j in range(len(nums),0,-1):
            if nums[j-1]==target:
                pos.append(j-1)
                break
        if len(pos)==0:
            return [-1,-1]
        if len(nums)==1:
            return [0,0]
        return pos