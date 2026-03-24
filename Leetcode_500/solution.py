class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        for word in words:
            if set(word.lower()).issubset(set(first)):
                result.append(word)
            elif set(word.lower()).issubset(set(second)):
                result.append(word)
            elif set(word.lower()).issubset(set(third)):
                result.append(word)
        return result