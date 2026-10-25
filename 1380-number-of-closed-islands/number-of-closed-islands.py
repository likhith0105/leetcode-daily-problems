class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1 or (r, c) in visit:
                return True
            
            visit.add((r, c))
            
            is_closed = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not dfs(r + dr, c + dc):
                    is_closed = False
            
            return is_closed

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visit:
                    if dfs(r, c):
                        count += 1
                        
        return count