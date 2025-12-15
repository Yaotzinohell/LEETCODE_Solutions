class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken_list = set(brokenLetters)
        text_list = text.split()

        count=0
        for texts in text_list:
            if not any(ch in broken_list for ch in texts):
                count+=1
        
        return count