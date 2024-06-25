#https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res.append(nums[i:j + 1])

        sum = 0
        for i in res:
            arr = set(i)
            sum = sum + (len(arr) * len(arr))
            
        return sum
