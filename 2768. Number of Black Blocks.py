#https://leetcode.com/problems/number-of-black-blocks/description/

from collections import Counter

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # Convert the list of coordinates to a set for O(1) lookups
        black_cells = set(map(tuple, coordinates))
        directions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        block_counts = Counter()
        
        # Iterate through each black cell and determine which 2x2 blocks it affects
        for r, c in black_cells:
            for dr, dc in directions:
                row = r - dr
                col = c - dc
                # Check if the top-left corner of the 2x2 block is within grid bounds
                if 0 <= row < m - 1 and 0 <= col < n - 1:
                    block_counts[(row, col)] += 1

        # Initialize the result array to count blocks with 0 to 4 black cells
        result = [0] * 5
        
        # There are (m-1) * (n-1) total 2x2 blocks in the grid
        total_blocks = (m - 1) * (n - 1)
        
        # Count the blocks based on how many black cells they have
        for count in block_counts.values():
            result[count] += 1
        
        # Calculate blocks with 0 black cells by subtracting those with 1-4 black cells
        result[0] = total_blocks - sum(result[1:])
        
        return result
