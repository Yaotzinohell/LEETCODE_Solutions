class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start_index = 0
        max_length = 0
        char_index={}
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >=start_index:
                start_index = char_index[s[end]]+1
            char_index[s[end]] = end
            max_length = max(max_length,end-start_index+1)
        return max_length
