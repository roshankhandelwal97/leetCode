#https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/description/

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return []
    
        j = (tomatoSlices - 2 * cheeseSlices) // 2
        s = cheeseSlices - j
        
        if j >= 0 and s >= 0:
            return [j, s]
        return []
        
