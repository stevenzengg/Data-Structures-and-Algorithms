from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfsValidation(node: tuple) -> bool:
            if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]) and node not in seen and grid[node[0]][node[1]] != 0:
                return True
            return False
        

        if not grid or len(grid[0]) == 0 or not all([len(i) == len(grid[0]) for i in grid]):
            return -1
        
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        seen = set()
        oranges = set()
        queue = deque()
        
        for i, v in enumerate(grid):
            for i2, v2 in enumerate(v):
                if not isinstance(v2, int):
                    return -1
                if v2 == 1:
                    oranges.add((i, i2))
                elif v2 == 2:
                    oranges.add((i, i2))
                    queue.append((i, i2))
                    
        if not queue:
            if not oranges:
                return 0
            return -1
        
        score = -2
        while queue:
            score += 1
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if bfsValidation(node):
                    seen.add(node)
                    for a,b in directions:
                        queue.append((node[0] + a, node[1] + b))
        
        if seen == oranges:
            return score
        return -1
        
            
        

if __name__ == '__main__':
    a = Solution()
    b = [[0]]
    print(a.orangesRotting(b))