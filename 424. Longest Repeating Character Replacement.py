#https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0
        res = 0
        dic = {}
        ans = 0

        for r in range(len(s)):
            if(s[r] in dic):
                dic[s[r]] += 1
            else: 
                dic[s[r]] = 1
            print(dic)
            maxK = max(dic.values())
            leng = (r - l) + 1
            while(leng - maxK > k and l < len(s)):
                dic[s[l]] -=1
                l +=1
                leng = (r - l) + 1
            ans = max(ans, leng)
        return ans

        
