class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        strs.sort() #Sorting the array brings the uncommon word to the last index of the array reducing the comparison operation
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:#Checking the first word with the last word to find the prefix
                result+=strs[0][i]
            else: 
                break
        return result