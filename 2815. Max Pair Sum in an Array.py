#https://leetcode.com/problems/max-pair-sum-in-an-array/description/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = {}
        for i in nums: 
            if max(str(i)) in dic: 
                dic[max(str(i))].append(i)
            else: 
                dic[max(str(i))] = [i]

        sum = 0
        for i in dic:
            arr = dic[i]
            if len(arr) > 1: 
                pop1 = max(arr)
                arr.remove(max(arr))
                pop2 = max(arr)
                arr.remove(max(arr))
                sum = max(sum, pop1 + pop2)

        return -1 if sum == 0 else sum
