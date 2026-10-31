class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Helper to find the landing position given a starting cell and initial move direction
        # dir_move: 0 for right, 1 for down
        def get_jump(r, c, dir_move):
            curr_r, curr_c = r, c
            curr_dir = dir_move
            
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                if curr_dir == 0:  # moving right into mirror -> turns down
                    curr_r += 1
                    curr_dir = 1
                else:  # moving down into mirror -> turns right
                    curr_c += 1
                    curr_dir = 0
            
            if 0 <= curr_r < m and 0 <= curr_c < n:
                return (curr_r, curr_c)
            return None

        # dp[r][c] stores number of valid paths reaching (r, c)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    if r == 0 and c == 0:
                        pass
                    else:
                        continue
                
                # Try moving Right: target cell if we step right is (r, c + 1)
                if c + 1 < n:
                    if grid[r][c + 1] == 1:
                        jump = get_jump(r, c + 1, 0)
                        if jump:
                            jr, jc = jump
                            dp[jr][jc] = (dp[jr][jc] + dp[r][c]) % MOD
                    else:
                        dp[r][c + 1] = (dp[r][c + 1] + dp[r][c]) % MOD
                
                # Try moving Down: target cell if we step down is (r + 1, c)
                if r + 1 < m:
                    if grid[r + 1][c] == 1:
                        jump = get_jump(r + 1, c, 1)
                        if jump:
                            jr, jc = jump
                            dp[jr][jc] = (jr, jc) and (dp[jr][jc] + dp[r][c]) % MOD
                    else:
                        dp[r + 1][c] = (dp[r + 1][c] + dp[r][c]) % MOD
                        
        return dp[m - 1][n - 1]