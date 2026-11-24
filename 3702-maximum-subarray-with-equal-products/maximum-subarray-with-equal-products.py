import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        max_possible_lcm = 2520  # lcm(1..10)

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                curr_gcd = x if curr_gcd == 0 else math.gcd(curr_gcd, x)
                curr_lcm = math.lcm(curr_lcm, x)

                if prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)

                # Pruning: gcd only decreases and lcm <= 2520
                if prod > max_possible_lcm * curr_gcd * curr_lcm:
                    break

        return max_len