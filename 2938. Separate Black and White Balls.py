#https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        swap = 0
        for i in range(len(s)): 
            if s[i] == '0': 
                swap = swap + (i - count)
                count +=1
        return swap
