class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = [0] * numCourses
        adj = defaultdict(list)
        self.ans = []
        for a, b in prerequisites:
            adj[b].append(a)
        
        for i in range(numCourses):
            if not self.dfs(i, adj, seen):
                return []
        
        return list(reversed(self.ans))
        
    
    def dfs(self, i, adj, seen):
        if seen[i] == 2:
            return True
        if seen[i] == 1:
            return False
        seen[i] = 1

        for nbr in adj[i]:
            if not self.dfs(nbr, adj, seen):
                return False
        
        seen[i] = 2
        self.ans.append(i)
        return True
        

    # idea here is to do post order, and then reverse the traversal order