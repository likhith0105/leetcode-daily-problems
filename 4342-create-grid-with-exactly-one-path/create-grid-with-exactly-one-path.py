class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize an m x n grid filled entirely with obstacles ('#')
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # Carve out the path along the top row
        for j in range(n):
            grid[0][j] = '.'
            
        # Carve out the path down the rightmost column
        for i in range(m):
            grid[i][n - 1] = '.'
            
        # Convert each row list into a string
        return ["".join(row) for row in grid]
        