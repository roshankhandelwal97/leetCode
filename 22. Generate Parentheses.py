#https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def para(openP, closeP):
            if openP == closeP == n:
                res.append("".join(stack))
                return res
            if openP < n:
                stack.append("(")
                para(openP + 1, closeP)
                stack.pop()
            if openP > closeP: 
                stack.append(")")
                para(openP, closeP + 1)
                stack.pop()
        para(0,0)
        return res
        
