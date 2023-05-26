from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        memo = [0 for _ in graph]

        for i in range(len(graph)):
            states = [0 for _ in graph]
            if self.recurse(i, states, graph, memo):
                memo[i] = 1
            else:
                memo[i] = 2

        ans = []
        for i, v in enumerate(memo):
            if v == 2:
                ans.append(i)

        return ans


    def recurse(self, node, states, graph, memo):
        if memo[node] == 1 or states[node] == 1:
            return True
        if memo[node] == 2 or states[node] == 2:
            return False
        states[node] = 1

        for nextNode in graph[node]:
            if states[node] != 2 and self.recurse(nextNode, states, graph, memo):
                    return True
        
        states[node] = 2
        return False


if __name__ == '__main__':
    a = Solution()
    b = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(a.eventualSafeNodes(b))