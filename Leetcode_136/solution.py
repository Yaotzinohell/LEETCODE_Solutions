# class Solution(object):
#     def singleNumber(self, nums):
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[i]==nums[j]:
#                     count+=1
#             if count==1:
#                 return nums[i]
class Solution(object):
    def singleNumber(self,nums):
        fre={}
        for n in nums:
            fre[n]=fre.get(n,0)+1
        for key,value in fre.items():
            if value == 1:
                return key