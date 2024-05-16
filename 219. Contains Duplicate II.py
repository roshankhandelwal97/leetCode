#https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        index = 0
        for i in nums:
            #print(dic)
            if i not in dic: 
                dic[i] = index
            else: 
                if abs(dic.get(i) - index) <=k:
                    return True
                else: 
                    dic[i] = index
            index +=1

        return False
