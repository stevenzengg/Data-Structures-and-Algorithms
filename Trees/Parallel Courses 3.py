class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        times = [0 for _ in range(n)]

        adj = defaultdict(list)
        indegs = defaultdict(int)
        for a, b in relations:
            adj[a-1].append(b-1)
            indegs[b-1] += 1
        
        q = deque([(i, time[i]) for i in range(n) if indegs[i] == 0])

        for course, dur in q:
            times[course] = dur

        while q:
            course, dur = q.popleft()

            for nbr in adj[course]:
                times[nbr] = max(times[nbr], time[nbr] + dur)
                indegs[nbr] -= 1
                if indegs[nbr] == 0:
                    q.append((nbr, times[nbr]))
        
        return max(times)