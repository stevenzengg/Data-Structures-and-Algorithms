class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        memo = [float('inf')] * n
        heap = [(0, k - 1)] # time, node

        adj = defaultdict(list)
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        while heap:
            time, node = heapq.heappop(heap)
            if memo[node] < time:
                continue
            memo[node] = time
            for nbr, t in adj[node]:
                if time + t < memo[nbr]:
                    heapq.heappush(heap, (time + t, nbr))
        ans = max(memo)
        return ans if ans != float('inf') else -1
