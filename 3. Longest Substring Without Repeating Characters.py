#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        ans = 0
        if len(s)== 0:
            return 0
        res.append(s[0])
        for i in s[1:]:
            if(i in res):
                while(i in res): 
                        res.pop(0)
                        continue
            ans = max(len(res),ans)
            res.append(i)
        return ans +1


        
