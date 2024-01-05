#https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isAlpha = [w.lower() for w in s if w.isalnum()]
        print(isAlpha)

        start = 0
        end = len(isAlpha)-1

        while(start<=end):
            if(isAlpha[start] != isAlpha[end]):
                return False
            start = start + 1 
            end = end - 1

        return True
