class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row with cumulative sums
        for c in range(1, n):
            grid[0][c] += grid[0][c - 1]
            
        # Initialize the first column with cumulative sums
        for r in range(1, m):
            grid[r][0] += grid[r - 1][0]
            
        # Fill in the rest of the grid using the minimum of top and left cells
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                
        return grid[-1][-1]