from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.append((sr, sc))
        ogColor = image[sr][sc]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()

        while queue:
            x, y = queue.popleft()
            seen.add((x, y))
            image[x][y] = color
            for a, b in directions:
                newX, newY = x + a, y + b
                if 0 <= newX < len(image) and 0 <= newY < len(image[0]) and image[newX][newY] == ogColor and (newX, newY) not in seen:
                    queue.append((newX, newY))
        
        return image


if __name__ == '__main__':
    a = Solution()
    b = [[1,1,1],[1,1,0],[1,0,1]]
    sr, sc, color = 1, 1, 2
    print(a.floodFill(b, sr, sc, color))
