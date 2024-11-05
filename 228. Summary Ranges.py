#https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: 
            return []
        temp = [nums[0]]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == temp[-1] + 1 : 
                temp.append(nums[i])
            else: 
                if len(temp) > 1:
                    string = f"{temp[0]}->{temp[-1]}"
                else: 
                    string = f"{temp[-1]}"
                res.append(string)
                temp = [nums[i]]
        if len(temp) > 1:
            string = f"{temp[0]}->{temp[-1]}"
            res.append(string)
        else: 
            string = f"{temp[-1]}"
            res.append(string)
        return res


        
