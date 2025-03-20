class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        heap = [(0, 0, 0)] # (cost, time, city)
        adj = defaultdict(list)
        for a, b, time in edges:
            adj[a].append((b, time))
            adj[b].append((a, time))
        
        # memo on time bc cost is monotonically increasing
        memo = defaultdict(int) # city : time

        while heap:
            cost, time, city = heapq.heappop(heap)
            newCost = cost + passingFees[city]
            if city in memo and memo[city] <= time or time > maxTime:
                continue
            if city == n - 1:
                return newCost
            memo[city] = time
            for nbr, newTime in adj[city]:
                heapq.heappush(heap, (newCost, time + newTime, nbr))
        return -1