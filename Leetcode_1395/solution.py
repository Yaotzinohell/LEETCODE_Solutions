class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count=0
        for j in range(len(rating)):
            left_small=left_big=0
            right_small=right_big=0
            for i in range(j):
                if rating[i]<rating[j]:
                    left_small+=1
                if rating[i]>rating[j]:
                    left_big+=1
            
            for k in range(j+1,len(rating)):
                if rating[k]<rating[j]:
                    right_small+=1
                if rating[k]>rating[j]:
                    right_big+=1
            
            count += left_small*right_big + left_big*right_small
        
        return count