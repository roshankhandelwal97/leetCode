# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        astStack = []

        for i in range(len(s)): 
            if s[i] == '(':
                openStack.append(i)
            elif s[i] == '*':
                astStack.append(i)
            
            elif s[i] == ')':
                if openStack:
                    openStack.pop()
                    continue
                elif astStack: 
                    astStack.pop()
                else: 
                    return False
        
        while openStack and astStack:
            if openStack[-1] < astStack[-1]:
                openStack.pop()
                astStack.pop()
            else:
                return False
        
        return not openStack
                


        
