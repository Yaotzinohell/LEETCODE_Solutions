class Solution(object):
    def longestValidParentheses(self, s):
        para = [-1] #Para acts as a stack here, it's basically a list LOL
        max_len = 0
        for i,char in enumerate(s):
            if char == '(':
                para.append(i) #Appending the index of the open parenthesis
            else:
                para.pop() #When closing paranthesis is found it pops
                if not para: #After the pop operation if the para is empty then we append the closing paranthesis
                    para.append(i)
                else:
                    max_len = max(max_len, i-para[-1]) #para = [-1] is initialised to know the starting index of the stack
        return max_len