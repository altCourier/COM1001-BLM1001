# First solution two pointers
class SolOne:
    def __init__(self, s):
        self.s = s
    
    def reverser(self, s) -> str:
        s = list(self.s) # Conversion because strings are immutable.
        L, R = 0, len(s) - 1

        while L < R:
            if not (s[L]).isalnum():
                L += 1
            elif not (s[R].isalnum()):
                R -= 1
            else:
                s[R], s[L] = s[L], s[R]
                L, R = L + 1, R - 1
        return ''.join(s)

# Stack solution
class SolTwo:
    def __init__(self, s):
        self.s = s

    def reverser(self,s) -> str:
        s = self.s

        stack = [c for c in s if c.isalnum()]
        result = []

        for c in s:
            if c.isalnum():
                result.append(stack.pop())
            else:
                result.append(c)
        return ''.join(result)
    
# REGEX solution
import re

class SolThree:
    def __init__(self, s):
        self.s = s

    def reverser(self,s) -> str:
        s = self.s

        alnumChars = re.findall(r'[a-zA-Z0-9]', s)
        result = list(s)

        for i in range(len(result)):
            if i.isalnum():
                result[i] = alnumChars.pop() # Change it to the last character.