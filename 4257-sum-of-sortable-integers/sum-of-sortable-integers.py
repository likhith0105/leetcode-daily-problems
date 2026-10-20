from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        divisors = []

        for k in range(1, int(n ** 0.5) + 1):
            if n % k == 0:
                divisors.append(k)
                if k != n // k:
                    divisors.append(n // k)

        ans = 0

        for k in divisors:
            prev_max = None
            valid = True

            for start in range(0, n, k):
                end = start + k
                mn = mx = nums[start]
                descents = 0

                for i in range(start + 1, end):
                    x = nums[i]
                    if x < mn:
                        mn = x
                    if x > mx:
                        mx = x
                    if nums[i - 1] > x:
                        descents += 1

                if nums[end - 1] > nums[start]:
                    descents += 1

                if descents > 1:
                    valid = False
                    break

                if prev_max is not None and prev_max > mn:
                    valid = False
                    break

                prev_max = mx

            if valid:
                ans += k

        return ans