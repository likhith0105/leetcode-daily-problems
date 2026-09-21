class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k  # dp[r] stores the count of subarrays ending at current index with product % k == r
        
        for num in nums:
            next_dp = [0] * k
            val = num % k
            
            # Single-element subarray starting and ending at current index
            next_dp[val] += 1
            
            # Extend existing subarrays ending at the previous index
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val) % k] += dp[r]
            
            dp = next_dp
            
            # Accumulate current index counts into total answers
            for r in range(k):
                ans[r] += dp[r]
                
        return ans