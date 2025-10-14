class Solution(object):
    def isValid(self, s):
        s = list(s)
        stack = []
        for i,char in enumerate(s):
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            elif char==')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif char==']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif char=='}':
                if stack:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True