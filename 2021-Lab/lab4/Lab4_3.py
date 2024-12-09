# FIRST SOLUTION:
# REGEX SOLUTION

import re

class SolOne:
    def __init__(self, input_s:str) -> str:
        self.input_s = input_s
    
    def cleaner_slicer(self) -> bool:
        cleaned = re.sub(r'[a-zA-Z0-9]','',self.input_s).lower() # O(n), resub for scanning the entire str
        return cleaned == cleaned[::-1] # O(n) time complexity for slicing [::-1]
        # O (n) for comparison
        # O(n) + O(n) + O(n) = O(n)
    """
    Optimization for palindrome check
    """
    def is_palindrome(self) -> bool:
        cleaned = re.sub(r'[a-zA-Z0-9]','',self.input_s).lower()
        L, R = 0, len(cleaned) - 1

        while L < R:
            if cleaned[L] != cleaned[R]:
                return False
            L, R = L+1, R-1 
            # Each pointer travels once O(n)
            # No space used O(1)
        return True
    

# USE .isalnum() 
class SolTwo:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def palindrome(self) -> bool:
        newStr = ""

        for c in self.input_str: # O(n) for looping the string
            if c.isalnum():
                newStr += c.lower() # O(n) for space complexity
        
        return newStr == newStr[::-1]
    
# HOW DO WE USE THE .isalnum() EVEN???
# LET'S WRITE THE FUNCTION OURSELVES.

class SolThree:
    def __init__(self, input_str):
        self.input_str = input_str

    def palindrome(self, s):
        s = self.input_str

        L, R = 0, len(s) - 1
        while L < R:
            while L<R and not self.alphaNum(s[L]):
                L += 1
            while L<R and not self.alphaNum_ord(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L, R = L+1, R-1
        return True
    # isalnum() can we written like so: 
    def alphaNum(self, c):
        return (
            ('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9')
        )
    # Or using ord() to get the ASCII values
    def alphaNum_ord(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or 
                (ord('a') <= ord(c) <= ord('z')) or 
                (ord('0') <= ord(c) <= ord('9'))
                )

