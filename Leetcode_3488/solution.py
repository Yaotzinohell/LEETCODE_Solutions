class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        index_value = defaultdict(list)
        indexs = []

        for i, num in enumerate(nums):
            indexs.append(len(index_value[num]))
            index_value[num].append(i)
        
        res = []

        for q in queries:
            qvalue = index_value[nums[q]]

            if len(qvalue)==1:
                res.append(-1)
            else:
                j = indexs[q]
                previous = qvalue[(j-1) % len(qvalue)]
                next = qvalue[(j + 1) % len(qvalue)]
                res.append(min(
                    (next + n - qvalue[j]) % n,
                    (qvalue[j] - previous + n) % n,
                )) 
        return res