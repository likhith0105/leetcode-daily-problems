class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        
        # prefix_sum tracks the number of reachable '0's in the sliding window
        prefix_sum = 0
        
        for i in range(1, n):
            # Add the element entering the sliding window from the left
            if i >= minJump:
                prefix_sum += int(dp[i - minJump])
            
            # Remove the element leaving the sliding window from the right
            if i > maxJump:
                prefix_sum -= int(dp[i - maxJump - 1])
                
            # Current index is reachable if it's '0' and there is at least one reachable index in our window
            if s[i] == '0' and prefix_sum > 0:
                dp[i] = True
                
        return dp[-1]