from collections import defaultdict, deque
from typing import List
class Solution:

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        bPath = []
        self.dfs(bob, None, bPath, adjList)
        bPathLen = len(bPath)
        ans = -float('inf')
        q = deque([(0, None, 0)]) # node, parent, score
        steps = 0
        opened = set()
        while q:
            length = len(q)
            for _ in range(length):
                node, parent, score = q.popleft()
                bNode = bPath[steps] if steps < bPathLen else None
                if bNode == node:
                    score += amount[node]/2
                elif node not in opened:
                    score += amount[node]
                opened.update([bNode, node])
                
                nbrs = adjList[node]
                if len(nbrs) == 1 and parent == nbrs[0]:
                    ans = max(ans, score)
                    continue
                for child in nbrs:
                    if parent != child:
                        q.append((child, node, score))

            steps += 1
        return int(ans)

    def dfs(self, node, parent, builder, adjList):
        if node == 0:
            builder.append(0)
            return True
        builder.append(node)
        for child in adjList[node]:
            if child == parent:
                continue
            path = self.dfs(child, node, builder, adjList)
            if path:
                return True
        builder.pop()
        return False