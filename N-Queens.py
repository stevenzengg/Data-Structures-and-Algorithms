from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.rows, self.cols, self.diag1, self.diag2 = set(), set(), set(), set(),
        self.board = [["." for i in range(n)] for j in range(n)]
        self.ans = []
        self.recurse(n, 0, 0)
        return self.ans

    def recurse(self, n, curr, queens):
        if queens == n:
            self.ans.append(["".join(i) for i in self.board])
            return
        if curr == n*n:
            return

        row, col = divmod(curr, n)
        for r in range(row, n):
            for c in range(n):
                if self.validate(r, c):
                    self.board[r][c] = "Q"
                    self.rows.add(r)
                    self.cols.add(c)
                    self.diag1.add(r - c)
                    self.diag2.add(r + c)
                    self.recurse(n, curr + 1, queens + 1)
                    self.board[r][c] = "."
                    self.rows.remove(r)
                    self.cols.remove(c)
                    self.diag1.remove(r - c)
                    self.diag2.remove(r + c)
                curr += 1
        


    def validate(self, r, c):
        if r in self.rows or c in self.cols or r - c in self.diag1 or r + c in self.diag2:
            return False
        return True


    def validate(self, r, c):
        if r in self.rows or c in self.cols or r - c in self.diag1 or r + c in self.diag2:
            return False
        return True


        




if __name__ == '__main__':
    a = Solution()
    b = 4
    a.solveNQueens(b)