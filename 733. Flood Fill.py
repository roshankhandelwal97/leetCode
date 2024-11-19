#https://leetcode.com/problems/flood-fill/submissions/1456872189/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        start_color = image[sr][sc]
        
        if color == start_color:
            return image

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = deque([(sr, sc)])

        while(q):
            r, c = q.popleft()
            if image[r][c] == start_color:
                image[r][c] = color
                for dr, dc in directions: 
                    row, col = dr + r, dc + c
                    if row in range(ROWS) and col in range(COLS):
                        q.append((row, col))

        return image
