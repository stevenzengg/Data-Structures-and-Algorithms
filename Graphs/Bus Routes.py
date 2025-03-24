class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stopToBus = defaultdict(list)
        for i, v in enumerate(routes):
            for j in v:
                stopToBus[j].append(i)
        
        adj = defaultdict(list)
        for stop, buses in stopToBus.items():
            for i, v in enumerate(buses):
                for j in range(i + 1, len(buses)):
                    adj[v].append(buses[j])
                    adj[buses[j]].append(v)

        source = stopToBus[source]
        target = set(stopToBus[target])
        steps = 1
        visited = set(source)
        q = deque(source)

        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node in target:
                    return steps
                
                for nbr in adj[node]:
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)

            steps += 1
        
        return -1