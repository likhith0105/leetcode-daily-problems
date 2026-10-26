import bisect

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = 0
        for q in queries:
            max_x = max(max_x, q[1])
            if q[0] == 2:
                max_x = max(max_x, q[1] + q[2])
        
        # We can use a sorted list or Fenwick tree / Segment tree. 
        # Given constraints, max_x can be up to min(5 * 10^4, 3 * queries.length).
        # Let's use a Segment tree to maintain the maximum gap between consecutive obstacles.
        
        # Obstacles initially at 0 and max_x + 1
        obs = [0, max_x + 1]
        
        # Segment tree over the coordinate range [0, max_x + 1]
        # tree[node] will store the maximum gap covered by this segment
        size = max_x + 2
        tree = [0] * (4 * size)
        
        def update(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])
            
        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr))

        # Insert initial boundaries
        update(1, 0, max_x + 1, 0, 0)
        update(1, 0, max_x + 1, max_x + 1, 0)
        
        # Using a sorted list for obstacles
        from sortedcontainers import SortedList
        sl = SortedList([0, max_x + 1])
        
        # Initially gap between 0 and max_x + 1 is max_x + 1
        update(1, 0, max_x + 1, max_x + 1, max_x + 1)
        
        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_right(x)
                succ = sl[idx]
                pred = sl[idx - 1]
                
                sl.add(x)
                
                # Update gaps
                update(1, 0, max_x + 1, x, x - pred)
                update(1, 0, max_x + 1, succ, succ - x)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x)
                pred = sl[idx - 1]
                
                # Max gap in [0, pred]
                max_gap = query(1, 0, max_x + 1, 0, pred)
                # Also check the last segment from pred to x
                max_gap = max(max_gap, x - pred)
                
                if max_gap >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans