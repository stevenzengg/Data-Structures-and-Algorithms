# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# [[0,0,1], 
#  [0,0,0], 
#  [0,1,1]] -> answer is 2

# [[1,0,1], 
#  [1,1,1], 
#  [0,1,1]] -> 7

# [[0,0,0], 
#  [0,0,0], 
#  [0,0,0]] -> 0
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    ans = max(ans, self.dfs(i, j, grid, visited))
        return ans

    def dfs(self, i, j, grid, visited):
        ans = 1
        for a, b in self.directions:
            x, y = a + i, b + j
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == 1:
                visited.add((x, y))
                ans += self.dfs(x, y, grid, visited)
        return ans

if __name__ == '__main__':
    a = Solution()
    b = [[0,0,0], [0,0,0], [0,0,0]]
    print(a.maxAreaOfIsland(b))
  
