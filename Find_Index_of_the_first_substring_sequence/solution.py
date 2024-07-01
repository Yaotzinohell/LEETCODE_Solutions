class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        index = haystack.find(needle)
        return index if index != -1 else -1