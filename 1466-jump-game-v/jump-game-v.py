from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n

        def dfs(i):
            if dp[i]:
                return dp[i]

            dp[i] = 1

            for direction in (-1, 1):
                j = i + direction
                steps = 0

                while 0 <= j < n and steps < d and arr[j] < arr[i]:
                    dp[i] = max(dp[i], 1 + dfs(j))
                    if arr[j] >= arr[i]:
                        break
                    j += direction
                    steps += 1

            return dp[i]

        return max(dfs(i) for i in range(n))