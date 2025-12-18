class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = set()
        hash_map = {}

        for digit in digits:
            hash_map[digit] = hash_map.get(digit,0) + 1
        
        def backtracking(path):
            if len(path) == 3:
                if (path[0]*100 + path[1]*10 + path[2])%2 == 0:
                    arr.add(path[0]*100 + path[1]*10 + path[2])
                return

            for digit in hash_map:
                if len(path)==0 and digit == 0:
                    continue
                if hash_map[digit]>0:
                    hash_map[digit]-=1
                    path.append(digit)
                    backtracking(path)
                    path.pop()
                    hash_map[digit]+=1
        backtracking([])
        return sorted(list(arr))