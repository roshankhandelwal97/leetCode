#https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0: 
            return -1

        ROW, COL = len(grid), len(grid[0])
        if ROW == 1 and COL == 1:  # Edge case for a single cell grid
            return 1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        level = 1

        while q: 
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) == (ROW - 1, COL - 1):
                    return level
                for dr, dc in directions: 
                    row, col = r + dr, c + dc
                    if 0 <= row < ROW and 0 <= col < COL and (row, col) not in visited and grid[row][col] == 0: 
                        q.append((row, col))
                        visited.add((row, col))
            level += 1

        return -1
