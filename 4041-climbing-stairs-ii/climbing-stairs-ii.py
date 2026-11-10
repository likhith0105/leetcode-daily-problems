class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] represents the minimum total cost to reach step j.
        # Since we can jump from step i to i+1, i+2, or i+3, 
        # the state dp[j] depends on the previous 3 states: j-1, j-2, and j-3.
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting from step 0 with cost = 0
        
        for j in range(1, n + 1):
            # Check all possible previous steps (j-1, j-2, j-3) that can jump to j
            for i in range(max(0, j - 3), j):
                jump_cost = costs[j - 1] + (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + jump_cost)
                
        return dp[n]