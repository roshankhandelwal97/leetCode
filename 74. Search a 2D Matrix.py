#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        print(matrix[0][-1])

        top = 0
        bottom = rows - 1
        while(top <= bottom):
            row = top + (bottom - top)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else: 
                break
        if(top > bottom):
            return False
        l = 0
        r = cols - 1

        while(l <= r):
            mid = l + (r-l)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target <  matrix[row][mid]: 
                r = mid -1
            else: 
                return True


        
