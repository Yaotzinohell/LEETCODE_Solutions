class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        if n == 1:
            return 1
        for i in range(1,n+1):
            nums.append(i)
        total = sum(nums)
        flag = 0
        left = 0
        right = 0
        for i, num in enumerate(nums):
            right = total - left
            left += num
            if left == right:
                return i+1
        return -1