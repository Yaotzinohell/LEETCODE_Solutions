class Solution(object):
    def removeElement(self, nums, val):
        i,j = 0,0
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i+=1
        return j