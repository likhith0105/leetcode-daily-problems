class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    # BFS to find island total value
                    queue = [(r, c)]
                    visited[r][c] = True
                    total_value = 0

                    while queue:
                        curr_r, curr_c = queue.pop(0)
                        total_value += grid[curr_r][curr_c]

                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] > 0:
                                visited[nr][nc] = True
                                queue.append((nr, nc))

                    if total_value % k == 0:
                        count += 1

        return count