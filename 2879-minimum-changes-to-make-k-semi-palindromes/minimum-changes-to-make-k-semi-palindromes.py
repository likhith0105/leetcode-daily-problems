class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute divisors for lengths up to n (d < length)
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # cost[i][j] stores the min changes to make s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                # Try every valid divisor d
                for d in divisors[length]:
                    current_changes = 0
                    group_len = length // d
                    
                    # Each group consists of elements separated by step 'd'
                    for group in range(d):
                        left = i + group
                        right = i + group + (group_len - 1) * d
                        
                        while left < right:
                            if s[left] != s[right]:
                                current_changes += 1
                            left += d
                            right -= d
                            
                    min_changes = min(min_changes, current_changes)
                
                cost[i][j] = min_changes

        # dp[i][parts] -> min changes to partition suffix s[i:] into 'parts' semi-palindromes
        memo = {}
        
        def solve(i, parts):
            if parts == 1:
                return cost[i][n - 1]
            if (i, parts) in memo:
                return memo[(i, parts)]
            
            res = float('inf')
            # Try all possible end points x for the first substring in this partition
            # Each substring must have a length of at least 2
            for x in range(i, n - 2 * (parts - 1) + 1):
                res = min(res, cost[i][x] + solve(x + 1, parts - 1))
                
            memo[(i, parts)] = res
            return res

        return solve(0, k)