#https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0

        hsmp = {}
        hsmp[0] = 1

        for i in nums:
            sum = sum + i
            temp = sum - k
            if temp in hsmp: 
                res = res + hsmp[temp]
            hsmp[sum] = hsmp.get(sum, 0) + 1
            temp = 0
        return res
