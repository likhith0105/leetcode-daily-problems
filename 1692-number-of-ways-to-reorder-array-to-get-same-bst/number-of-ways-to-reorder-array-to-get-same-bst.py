import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Ways to interleave left and right elements while preserving relative order
            # C(len(left) + len(right), len(left))
            ways_comb = math.comb(len(left) + len(right), len(left))
            
            return (ways_comb * helper(left) * helper(right)) % MOD
            
        # Subtract 1 because the original array ordering itself shouldn't be counted as a "reordering"
        return (helper(nums) - 1 + MOD) % MOD