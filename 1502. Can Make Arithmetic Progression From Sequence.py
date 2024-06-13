#https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        i = 0
        j = 1
        diff = arr[j] - arr[i]
        while j < len(arr):
            if arr[j] - arr[i] != diff: 
                return False
            i +=1
            j +=1
        
        return True

            



