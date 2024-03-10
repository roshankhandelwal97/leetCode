#https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        print(r)
        area = 0
        while(l < r):
            print(height[l], height[r])
            area = max(area,min(height[l], height[r]) * (r-l))
            print("area", area)
            if(height[l] < height[r]):
                l += 1
            else: 
                r -=1
        return area
