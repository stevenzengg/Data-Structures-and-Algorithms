from typing import List
from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # start from terminal nodes and work outwards
        reverse_g = defaultdict(list)
        outdegs = [len(graph[i]) for i in range(len(graph))]
        q = deque([])
        for i, v in enumerate(graph):
            for j in v:
                reverse_g[j].append(i)
            if not v:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nbr in reverse_g[node]:
                outdegs[nbr] -= 1
                if outdegs[nbr] == 0:
                    q.append(nbr)
        
        return [i for i, v in enumerate(outdegs) if v == 0]


if __name__ == '__main__':
    a = Solution()
    b = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(a.eventualSafeNodes(b))