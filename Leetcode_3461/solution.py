class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s)!=2:
            sus=""
            s = list(int(ch) for ch in s)
            print(s)
            for i in range(len(s)-1):
                sus+=str((s[i]+s[i+1])%10)
                print(sus)
            s=sus
        if s[0]==s[1]:
            return True
        else:
            return False