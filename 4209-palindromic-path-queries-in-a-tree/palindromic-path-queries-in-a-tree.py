
class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import defaultdict

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        for u in reversed(order):
            best = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        seg = [0] * (2 * n)
        values = [1 << (ord(c) - 97) for c in s]

        for u in range(n):
            seg[n + pos[u]] = values[u]

        for i in range(n - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(p, val):
            p += n
            seg[p] = val
            p //= 2
            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        def range_xor(l, r):
            res = 0
            l += n
            r += n
            while l < r:
                if l & 1:
                    res ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= seg[r]
                l //= 2
                r //= 2
            return res

        def path_xor(u, v):
            res = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                res ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            res ^= range_xor(pos[u], pos[v] + 1)
            return res

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                values[u] = 1 << (ord(parts[2]) - 97)
                update(pos[u], values[u])
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_xor(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans

