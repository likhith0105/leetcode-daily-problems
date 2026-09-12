from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in arr]

        nxt = []
        for l, r, w, i in arr:
            nxt.append(bisect_right(starts, r))

        dp = [[None] * (n + 1) for _ in range(5)]

        def solve(pos, k):
            if k == 0 or pos >= n:
                return (0, ())

            if dp[k][pos] is not None:
                return dp[k][pos]

            score1, ids1 = solve(pos + 1, k)

            score2, ids2 = solve(nxt[pos], k - 1)
            score2 += arr[pos][2]
            ids2 = tuple(sorted((arr[pos][3],) + ids2))

            if score2 > score1:
                ans = (score2, ids2)
            elif score2 < score1:
                ans = (score1, ids1)
            else:
                ans = (score2, min(ids1, ids2))

            dp[k][pos] = ans
            return ans

        return list(solve(0, 4)[1])