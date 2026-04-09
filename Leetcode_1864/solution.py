class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count0 = s.count('0')
        count1 = s.count('1')
        n = len(s)

        if abs(count0 - count1) > 1:
            return -1
        
        def minimumSwaps(starting):
            misplaced0 = 0
            misplaced1 = 0
            expected = starting
            for ch in s:
                if ch != expected:
                    if ch == '1':
                        misplaced1 += 1
                    else:
                        misplaced0 += 1
                expected = '1' if expected == '0' else '0'
            if misplaced0 != misplaced1:
                return float('inf')
            return misplaced0

        if count0 == count1:
            return min(minimumSwaps('0'), minimumSwaps('1'))
        if count0 > count1:
            return minimumSwaps('0')
        else:
            return minimumSwaps('1')