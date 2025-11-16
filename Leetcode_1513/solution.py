class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        segments=[]
        count=0
        for ch in s:
            if ch=='1':
                count+=1
            else:
                if count>0:
                    segments.append(count)
                count=0
        if count>0:
            segments.append(count)
        k=0
        MOD = 10**9+7
        for segment in segments:
            k+=((segment*(segment+1))//2) % MOD
        return k