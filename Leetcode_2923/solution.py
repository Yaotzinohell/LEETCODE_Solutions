class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        for i in range(n):
            for j in range(n):
                champion=True
                if i!=j and grid[i][j]==0:
                    champion=False
                    break
            if champion:
                return i
                