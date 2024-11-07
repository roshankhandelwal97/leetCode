#https://leetcode.com/problems/majority-element-ii/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hsmp = {}
        for i in nums: 
            hsmp[i] = hsmp.get(i, 0) + 1
        
        return [key for key, value in hsmp.items() if value > len(nums)/3]
