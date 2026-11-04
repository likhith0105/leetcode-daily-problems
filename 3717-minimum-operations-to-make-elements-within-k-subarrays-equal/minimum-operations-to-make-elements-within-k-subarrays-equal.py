from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)

        pos = {v: i + 1 for i, v in enumerate(vals)}

        bit1 = [0] * (m + 1)
        bit2 = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(t):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit1[nxt] < t:
                    idx = nxt
                    t -= bit1[nxt]
                step >>= 1

            return vals[idx]

        def add(v, delta):
            p = pos[v]
            update(bit1, p, delta)
            update(bit2, p, v * delta)

        costs = []
        total = 0

        for i, v in enumerate(nums):
            add(v, 1)
            total += v

            if i >= x:
                old = nums[i - x]
                add(old, -1)
                total -= old

            if i >= x - 1:
                med = kth((x + 1) // 2)
                p = pos[med]

                cnt_left = query(bit1, p)
                sum_left = query(bit2, p)

                cnt_right = x - cnt_left
                sum_right = total - sum_left

                cost = (
                    med * cnt_left - sum_left
                    + sum_right - med * cnt_right
                )

                costs.append(cost)

        inf = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [inf] * (n + 1)

            for i in range(x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]