# class Solution(object):
#     def getSumAbsoluteDifferences(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         result=[]
#         for i in range(0,len(nums)):
#             total=0
#             for j in range(0,len(nums)):
#                 if j!=i:
#                     total+=abs(nums[i]-nums[j])
#             result.append(total)
#         return result

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left_sum=0
        result=[]
        total=sum(nums)
        for i in range(n):
            left = (i*nums[i]) - left_sum
            left_sum+=nums[i]

            right_sum=total-left_sum
            right = right_sum - ((n-i-1)*nums[i])
            result.append((left+right))
        return result

# Breakdown of Absolute Differences

# For a number at index i, we split the absolute difference sum into two parts:

# Left side (elements before i)

# All elements nums[0] … nums[i−1] are ≤ nums[i].

# So:
# |nums[i] - nums[j]| = nums[i] - nums[j]

# The total contribution from the left side becomes:

# (number of elements on the left) × nums[i] minus (sum of all left elements)

#------------------------------------------------------------------------------------------------------

# Right side (elements after i)

# All elements nums[i+1] … nums[n−1] are ≥ nums[i].

# So:
# |nums[i] - nums[j]| = nums[j] - nums[i]

# The total contribution from the right side becomes:

# (sum of all right elements) minus (number of elements on the right × nums[i])