from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ans = 1
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in memo:
                    ans = max(ans, self.dfs(i, j, matrix, memo))
        
        return ans

    def dfs(self, i, j, matrix, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        ans = 1
        for a, b in self.directions:
            x, y = a + i, b + j
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                ans = max(ans, 1 +self.dfs(x, y, matrix, memo))
        memo[(i, j)] = ans
        return ans
