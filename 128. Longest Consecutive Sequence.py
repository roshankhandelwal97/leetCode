#https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        res = 0
        
        for n in numSet:
            if n-1 not in numSet: 
                length = 0
                while((n + length) in numSet):
                    length +=1
                res = max(res,length)

        return res

        

                
