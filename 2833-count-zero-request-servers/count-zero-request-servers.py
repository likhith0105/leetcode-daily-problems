from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda log: log[1])
        
        # Pair each query with its original index and sort by query time
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        server_counts = {}
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for q_idx, q_time in indexed_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand window to include logs <= window_end
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                if server_counts.get(server_id, 0) == 0:
                    active_servers += 1
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                right += 1
                
            # Shrink window from the left to remove logs < window_start
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Servers with zero requests = total servers (n) - active servers in window
            ans[q_idx] = n - active_servers
            
        return ans