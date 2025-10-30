class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        n = len(password)
        special = "!@#$%^&*()-+"
        if n>=8:
            if any(c.islower() for c in password):
                if any(c.isupper() for c in password):
                    if any(c.isdigit() for c in password):
                        if any(c in special for c in password):
                            for i in range(1,n):
                                if password[i]==password[i-1]:
                                    return False
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False