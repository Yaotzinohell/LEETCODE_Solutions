class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        length = 0
        maps = {0 : -1}
        #Making use of Hmap to calcualte the no. of 0's and 1's
        for i, num in enumerate(nums):
            #Increment the count value if the number is 1 else decerement if the number is 0
            count += (-1 if num else 1)
            #Check if the count is already in hmap, if yes the find the length of the string using max()
            if count in maps:
                length = max(length, i - maps[count])
            else:
            #else add the count to hmap
                maps[count] = i
        return length
