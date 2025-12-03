class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapping = {}
        mapset = set()
        slist = s.split(" ")
        if len(pattern)!=len(slist):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]]!=slist[i]:
                    return False
            elif slist[i] not in mapset:
                mapping[pattern[i]]=slist[i]
                mapset.add(slist[i])
            else:
                return False
        return True