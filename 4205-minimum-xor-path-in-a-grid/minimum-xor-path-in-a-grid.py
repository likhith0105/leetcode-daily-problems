class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Maximum possible value for grid[i][j] is 1023, so max XOR value is < 1024
        MAX_XOR = 1024
        
        # dp[j] is a set of all possible XOR values achievable at column j in the current row
        dp = [set() for _ in range(n)]
        
        # Initialize the starting cell (0, 0)
        dp[0].add(grid[0][0])
        
        # Fill the first row (can only come from the left)
        for j in range(1, n):
            for x in dp[j - 1]:
                dp[j].add(x ^ grid[0][j])
                
        # Fill the rest of the grid
        for i in range(1, m):
            # Update the first column of the current row (can only come from above)
            new_dp_0 = set()
            for x in dp[0]:
                new_dp_0.add(x ^ grid[i][0])
            dp[0] = new_dp_0
            
            # Update the remaining cells
            for j in range(1, n):
                new_set = set()
                # From top
                for x in dp[j]:
                    new_set.add(x ^ grid[i][j])
                # From left
                for x in dp[j - 1]:
                    new_set.add(x ^ grid[i][j])
                dp[j] = new_set
                
        # The answer is the minimum XOR value at the bottom-right cell (m - 1, n - 1)
        return min(dp[n - 1])