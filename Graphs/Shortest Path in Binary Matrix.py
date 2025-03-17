from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        neighborGrid = [(1,0), (1,1), (1,-1), (0,1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        if not grid or not all(len(i) == len(grid) for i in grid):
            return -1
        queue = deque()
        queue.append((0,0))
        ans = 0
        seen = set()
        
        # run bfs. bfs conditions: indices must be valid, value must be 0.
        def validNode(node: tuple) -> bool:
            if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid) and grid[node[0]][node[1]] == 0 and node not in seen:
                 return True
            return False

        while queue:
            ans += 1
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node == (len(grid)-1, len(grid)-1):
                    return ans
                if validNode(node):
                    seen.add(node)
                    for a, b in neighborGrid:
                        queue.append((node[0] + a, node[1] + b))
        
        return -1
    

if __name__ == '__main__':
    a = Solution()
    b = [[0,0,0],[1,1,0],[1,1,0]]
    c = [[0,0],[0,0]]
    print(a.shortestPathBinaryMatrix(b))
    print(a.shortestPathBinaryMatrix(c))


    
