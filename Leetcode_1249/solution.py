class Solution(object):
    def minRemoveToMakeValid(self, s):
        s=list(s)
        stack = []
        for i,char in enumerate(s):
            if char=='(':
                stack.append(i)
            elif char==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''
        for i in stack:
            s[i]=''
        
        return ''.join(s)