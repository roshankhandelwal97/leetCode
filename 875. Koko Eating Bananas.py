#https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 0
        sum = 0
        k = max(piles)

        while(l < r):
            mid = l + (r-l)//2 
            if(mid == 0):
                return k 
            sum = 0
            for i in piles:
                sum = sum + math.ceil(i/ mid)
            if sum > h: 
                l = mid + 1
            elif sum <= h:
                r = mid
            if(sum <= h):
                k = min(mid, k)
        return k
        
