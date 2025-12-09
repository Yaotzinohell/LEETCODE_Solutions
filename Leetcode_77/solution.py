class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        def backtracking(start):
            if len(path)==k:
                result.append(path[:])
                return
            
            for num in range(start, n+1):
                #Considering to add it to the subset
                path.append(num)
                backtracking(num+1)

                #Considering it not to add it to the subset
                path.pop()
        
        backtracking(1)
        return result