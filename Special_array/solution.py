<<<<<<< HEAD
class Solution(object):
    def isArraySpecial(self, nums):
        def parity(n):
            if n%2 == 0:
                return True
            else:
                return False
        n = len(nums)
        if n == 1:
            return True
        for i in range(0,n-1):
            if parity(nums[i]) == parity(nums[i+1]):
                return False
=======
class Solution(object):
    def isArraySpecial(self, nums):
        def parity(n):
            if n%2 == 0:
                return True
            else:
                return False
        n = len(nums)
        if n == 1:
            return True
        for i in range(0,n-1):
            if parity(nums[i]) == parity(nums[i+1]):
                return False
>>>>>>> 4a8a6fdb0ccf8608f6dcb4cc59a532462f510ae2
        return True