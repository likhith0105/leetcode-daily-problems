from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)

        # Count occurrences of each factor
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        # mult_count[d] = number of items whose factor is a multiple of d
        mult_count = [0] * (max_f + 1)
        for d in range(1, max_f + 1):
            total_mults = 0
            for m in range(d, max_f + 1, d):
                total_mults += freq[m]
            mult_count[d] = total_mults

        # dp[b] = maximum total item copies obtainable with budget b
        dp = [0] * (budget + 1)

        for f, p in items:
            if p > budget:
                continue

            # Exclude item itself (j != i)
            free_gain = mult_count[f] - 1
            new_dp = dp[:]

            for r in range(p):
                best_prev = float("-inf")
                max_m = (budget - r) // p
                for m in range(max_m + 1):
                    b = r + m * p
                    if best_prev != float("-inf"):
                        candidate = best_prev + m + free_gain
                        if candidate > new_dp[b]:
                            new_dp[b] = candidate
                    cur_val = dp[b] - m
                    if cur_val > best_prev:
                        best_prev = cur_val

            dp = new_dp

        return max(dp)