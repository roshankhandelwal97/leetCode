#https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}

        if len(s) != len(t): 
            return False

        for i in range(len(s)): 
            if(s[i] not in dic1):
                dic1[s[i]] = 1
            if(t[i] not in dic2):
                dic2[t[i]] = 1
            dic1[s[i]] += 1
            dic2[t[i]] += 1
        if dic1 != dic2:
            return False
        
        return True 
        
