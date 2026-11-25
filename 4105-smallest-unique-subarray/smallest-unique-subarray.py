from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        BASE1, MOD1 = 100003, 1_000_000_007
        BASE2, MOD2 = 100019, 1_000_000_009

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2

        def has_unique_of_length(length: int) -> bool:
            freq = {}
            p1 = pow1[length]
            p2 = pow2[length]

            for left in range(n - length + 1):
                right = left + length
                h1 = (pref1[right] - pref1[left] * p1) % MOD1
                h2 = (pref2[right] - pref2[left] * p2) % MOD2
                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans