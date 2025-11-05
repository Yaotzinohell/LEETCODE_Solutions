from collections import Counter
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)-k+1):
            sub=nums[i:i+k]
            freq = Counter(sub)
            sorted_items = [(frequency,number) for number,frequency in freq.items()]
            sorted_items.sort(reverse=True)
            top_x = sorted_items[:x]

            total = 0
            for num,count in top_x:
                total+= num*count
            res.append(total)
        
        return res
