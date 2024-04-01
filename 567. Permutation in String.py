#https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        dict1 = {}
        dict2 = {}
        
       
        for char in s1:
            if char not in dict1:
                dict1[char] = 0
            dict1[char] += 1
            
        
        for i in range(len(s1)):
            char = s2[i]
            if char not in dict2:
                dict2[char] = 0
            dict2[char] += 1
        
        l = 0
        for r in range(len(s1)-1,len(s2)):
            
            if dict1 == dict2:
                return True
            
            if r != len(s2)-1:  
                dict2[s2[l]] -= 1
                if dict2[s2[l]] == 0:
                    del dict2[s2[l]]  
                l += 1
                
                if s2[r+1] not in dict2:
                    dict2[s2[r+1]] = 0
                dict2[s2[r+1]] += 1
        
        return False
