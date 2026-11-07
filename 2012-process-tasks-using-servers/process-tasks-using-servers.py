import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for free servers: stores (weight, index)
        free_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free_servers)
        
        # Min-heap for busy servers: stores (free_time, weight, index)
        busy_servers = []
        
        ans = []
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            # Advance time to at least the current task's arrival time
            curr_time = max(curr_time, j)
            
            # If no free servers are available, jump time to when the next server finishes
            if not free_servers and busy_servers[0][0] > curr_time:
                curr_time = busy_servers[0][0]
                
            # Release all servers that become free at or before curr_time
            while busy_servers and busy_servers[0][0] <= curr_time:
                _, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # Assign the task to the best available server
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            # Push the server into the busy heap with its new release time
            heapq.heappush(busy_servers, (curr_time + task_time, weight, index))
            
        return ans