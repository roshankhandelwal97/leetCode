#https://leetcode.com/problems/group-anagrams/description/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []

        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i in dic: 
                dic[sorted_i].append(i)
            else: 
                dic[sorted_i] = [i]
        
        res = list(dic.values())

        print(dic)

        return res




        
        
