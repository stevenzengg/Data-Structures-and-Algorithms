from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initial pass, which oranges are rotten, which oranges arent
        rotten = deque()
        fresh = set()
        minutes = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        

        while fresh:
            length = len(rotten)
            if length == 0:
                return -1 
            for _ in range(length):
                i, j = rotten.popleft()
                for a, b in directions:
                    x, y = a + i, b + j
                    if (x, y) in fresh:
                        rotten.append((x, y))
                        fresh.remove((x, y))

            minutes += 1
        
        return minutes


        # bfs per minute passing, stop when all oranges are rotten / no oranges are fresh


if __name__ == '__main__':
    a = Solution()
    b = [[0]]
    print(a.orangesRotting(b))