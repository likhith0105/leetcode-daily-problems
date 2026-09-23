from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions mapping: street_type -> list of valid (dr, dc)
        # Directions: (-1, 0) -> Up, (1, 0) -> Down, (0, -1) -> Left, (0, 1) -> Right
        pipes = {
            1: [(0, -1), (0, 1)],   # Left, Right
            2: [(-1, 0), (1, 0)],   # Up, Down
            3: [(0, -1), (1, 0)],   # Left, Down
            4: [(0, 1), (1, 0)],    # Right, Down
            5: [(0, -1), (-1, 0)],  # Left, Up
            6: [(0, 1), (-1, 0)]    # Right, Up
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True
            
            street = grid[r][c]
            for dr, dc in pipes[street]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and visited status
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    next_street = grid[nr][nc]
                    # Check if neighboring cell can connect back to current cell
                    if (-dr, -dc) in pipes[next_street]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False