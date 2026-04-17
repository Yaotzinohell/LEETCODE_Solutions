class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        res = float('inf')
        for i in range(n):
            if words[i] == target:
                distance = abs(i-startIndex)
                res = min(res, min(distance, n-distance))
        
        return res if res!=float('inf') else -1