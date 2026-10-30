from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: graph[u] = list of (v, weight)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        
        # Min-heap stores: (current_weight, u, count)
        pq = [(0, 0, 1)]
        
        # dist[u][count] stores the minimum weight to reach node u with a given consecutive count
        # Since count ranges from 1 to k, we use size k + 1
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            # If we reached the destination node, return the weight
            if u == n - 1:
                return w
                
            if w > dist[u][count]:
                continue
                
            for v, weight in graph[u]:
                # Determine the new consecutive count
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                # Skip if it exceeds the maximum allowed consecutive identical characters
                if next_count > k:
                    continue
                    
                new_w = w + weight
                if new_w < dist[v][next_count]:
                    dist[v][next_count] = new_w
                    heapq.heappush(pq, (new_w, v, next_count))
                    
        return -1