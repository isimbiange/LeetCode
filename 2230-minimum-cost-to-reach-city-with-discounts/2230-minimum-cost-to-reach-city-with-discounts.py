import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)
        
        # Build the undirected graph
        for u, v, cost in highways:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        # (total_cost, current_city, discounts_left)
        heap = [(0, 0, discounts)]

        # visited[city][d] = True means we've already been to `city` with `d` discounts left
        visited = [[False] * (discounts + 1) for _ in range(n)]

        while heap:
            cost, city, d = heapq.heappop(heap)
            
            # If we've reached the destination city n - 1, return the cost
            if city == n - 1:
                return cost
            
            # Skip if we've already visited this state
            if visited[city][d]:
                continue
            visited[city][d] = True

            # Explore neighbors
            for nei, toll in graph[city]:
                # Move without using a discount
                heapq.heappush(heap, (cost + toll, nei, d))
                # Move using a discount, if any left
                if d > 0:
                    heapq.heappush(heap, (cost + toll // 2, nei, d - 1))

        return -1
