#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans= 0

        if(len(tokens) == 1):
            return int(tokens[-1])

        for i in tokens: 
            if i not in ['+', '/', '*', '-']:
                stack.append(i)
            else: 
                    n = int(stack.pop())
                    m = int(stack.pop())
                    if(i == '+'):
                        ans = m + n
                    if(i == '-'):
                        ans = m - n
                    if(i == '/'):
                        ans = math.trunc(m / n)
                    if(i == '*'):
                        ans = m * n
                    stack.append(ans)
        return ans
        
