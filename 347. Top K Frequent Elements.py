#https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        res = []

        for i in nums: 
            if i not in dic: 
                dic[i] = 1
            else: 
                dic[i] +=1
        
        while(len(res) < k and dic):
            maxi = max(dic, key=dic.get)
            res.append(maxi)
            del dic[maxi]

        return res
