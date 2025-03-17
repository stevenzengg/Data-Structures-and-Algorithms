from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [[0] * n for _ in range(n)]
        self.rows, self.cols, self.diags1, self.diags2 = set(), set(), set(), set()
        self.ans = []
        self.recurse(n, 0)
        return self.ans
    
    def recurse(self, n, i):
        if n == i:
            self.ans.append(["".join(["." if j == 0 else "Q" for j in i]) for i in self.board])
            return
        for j in range(n):
            if self.validate(i, j):
                self.addSeen(i, j)
                self.recurse(n, i + 1)
                self.remSeen(i, j)
    
    def validate(self, i, j):
        if i in self.rows or j in self.cols or i - j in self.diags1 or i + j in self.diags2:
            return False
        return True
    
    def addSeen(self, i, j):
        self.rows.add(i)
        self.cols.add(j)
        self.diags1.add(i - j)
        self.diags2.add(i + j)
        self.board[i][j] = 1
    
    def remSeen(self, i, j):
        self.rows.remove(i)
        self.cols.remove(j)
        self.diags1.remove(i - j)
        self.diags2.remove(i + j)
        self.board[i][j] = 0


if __name__ == '__main__':
    a = Solution()
    b = 4
    a.solveNQueens(b)