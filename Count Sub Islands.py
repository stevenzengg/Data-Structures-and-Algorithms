from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] != 1:
                    continue
                if self.recurse(i, j, grid1, grid2):
                    ans += 1
        return ans



    def recurse(self, i, j, grid1, grid2):
        grid2[i][j] = 0
        subStatus = True
        for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if 0 <= x < len(grid2) and 0 <= y < len(grid2[0]) and grid2[x][y] == 1:
                subStatus = self.recurse(x, y, grid1, grid2) and subStatus
        
        return subStatus and grid1[i][j]
        

if __name__ == '__main__':
    a = Solution()
    b = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    c = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(a.countSubIslands(b, c))