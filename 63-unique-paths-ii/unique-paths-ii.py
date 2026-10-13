class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting cell has an obstacle, 0 paths are possible
        if obstacleGrid[0][0] == 1:
            return 0
        
        # DP array to store the number of ways to reach each cell
        dp = [0] * n
        dp[0] = 1
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]
                    
        return dp[-1]