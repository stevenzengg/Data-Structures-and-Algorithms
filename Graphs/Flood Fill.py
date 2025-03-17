from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
        self.visited = set([(sr, sc)])
        ogColor = image[sr][sc]
        self.dfs(sr, sc, ogColor, color, image)
        return image
    
    def dfs(self, i, j, ogColor, color, image):
        image[i][j] = color
        for a, b in self.directions:
            x, y = a + i, b + j
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and (x, y) not in self.visited and image[x][y] == ogColor:
                self.visited.add((x, y))
                self.dfs(x, y, ogColor, color, image)


if __name__ == '__main__':
    a = Solution()
    b = [[1,1,1],[1,1,0],[1,0,1]]
    sr, sc, color = 1, 1, 2
    print(a.floodFill(b, sr, sc, color))
