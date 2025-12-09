class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            
            #Consider adding the number
            path.append(nums[index])
            backtracking(index+1,path)

            #Consider not adding the number
            path.pop()
            backtracking(index+1,path)
            
        backtracking(0,[])
        return result
