#https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = dict(('()', '[]', '{}'))
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif len(stack) == 0 or i!= dic[stack.pop()]:
                return False
        return len(stack) == 0

        
