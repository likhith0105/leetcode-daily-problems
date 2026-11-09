import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to keep track of busy servers: stores tuples of (free_time, server_id)
        busy_servers = []
        
        # Available servers pool, initially containing all servers from 0 to k-1
        available = list(range(k))
        
        # Track request count for each server
        request_counts = [0] * k
        
        for i, (arr_time, l_time) in enumerate(zip(arrival, load)):
            # Free up servers whose tasks have finished by the current arrival time
            while busy_servers and busy_servers[0][0] <= arr_time:
                _, free_server = heapq.heappop(busy_servers)
                # Insert back into the sorted available list maintaining order
                idx = bisect.bisect_left(available, free_server)
                available.insert(idx, free_server)
            
            # If no servers are available, drop the request
            if not available:
                continue
            
            # Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If no server >= target is available, wrap around to the beginning (index 0)
            if idx == len(available):
                idx = 0
            
            server_id = available.pop(idx)
            
            # Assign the request to this server
            request_counts[server_id] += 1
            heapq.heappush(busy_servers, (arr_time + l_time, server_id))
        
        # Find the maximum requests handled by any server
        max_handled = max(request_counts)
        
        # Return all servers that matched the maximum count
        return [i for i, count in enumerate(request_counts) if count == max_handled]