#https://leetcode.com/problems/projection-area-of-3d-shapes/description/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x_area = 0
        y_area = 0
        z_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        #y area calculate
        for val in grid:
            y_area += max(val)
        
        #z area calculate
        for col in range(COLS):
            max_value = grid[0][col]  # Start with the first row in each column
            for row in range(1, ROWS):
                if grid[row][col] > max_value:
                    max_value = grid[row][col]
            z_area += max_value
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != 0:
                    x_area+= 1

        return (x_area+y_area+z_area)
