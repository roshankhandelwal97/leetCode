#https://leetcode.com/problems/find-peak-element/description/

#Could also be done using binary search!!

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # i = 1
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        ans = 0
        # if len(nums)< 4: 
        for i in range(0,len(nums)):
                if nums[i] > nums[ans]:
                    ans = i
        return ans

        
