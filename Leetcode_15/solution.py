# class Solution(object):
#     def threeSum(self, nums):
#         res = []
#         for i in range(len(nums)):
#             for j in range(i+1):
#                 for k in range(j+1):
#                     if i!=j and j!=k and i!=k:
#                         if nums[i]+nums[j]+nums[k] == 0:
#                             res.append([nums[i],nums[j],nums[k]])
#         return res
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1

            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
        return res