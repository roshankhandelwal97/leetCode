#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = sorted(nums)
        print(temp)

        for x in range(1, len(nums)+1):
            for j in range(len(nums)):
                if temp[j] != nums[(j+x) % len(temp)]:
                    break
            if j == len(nums) -1:
                return True
        return False





        
