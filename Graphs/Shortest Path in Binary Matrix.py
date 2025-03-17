from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        q = deque([(0, 0)]) if grid and grid[0] and not grid[0][0] else []
        seen = set([(0, 0)])
        steps, n = 1, len(grid)
        while q:
            length = len(q)
            for _ in range(length):
                node = i, j = q.popleft()
                if node == (n - 1, n - 1):
                    return steps
                for di, dj in directions:
                    x, y = i + di, j + dj
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and grid[x][y] == 0:
                        seen.add((x, y))
                        q.append((x, y))
            steps += 1

        return -1
    

if __name__ == '__main__':
    a = Solution()
    b = [[0,0,0],[1,1,0],[1,1,0]]
    c = [[0,0],[0,0]]
    print(a.shortestPathBinaryMatrix(b))
    print(a.shortestPathBinaryMatrix(c))


    
