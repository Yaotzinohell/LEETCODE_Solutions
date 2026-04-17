class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(num):
            rev = 0
            while num!=0:
                digit = num % 10
                rev = rev * 10 + digit
                num //= 10
            return rev

        last_seen = {}
        min_dis = float('inf')

        for i, num in enumerate(nums):
            rev_num = reverse(num)

            if num in last_seen:
                min_dis = min(min_dis, abs(i - last_seen[num]))
            
            last_seen[rev_num] = i
        
        return min_dis if min_dis != float('inf') else -1