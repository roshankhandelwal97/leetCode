#https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid: 
            i.sort()        
        res = 0
        for j in range(len(grid[0])):
            temp = []
            for i in grid: 
                p = i.pop()
                temp.append(p)
            res = res + max(temp)
        return res
                


            
            
                    





            
