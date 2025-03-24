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


# Time complexity: O(n!n^2), Space complexity: O(n!n^2)
# T(n) = nT(n-1) + O(n^2)* S(n), where S(n) is number of solutions
# S(n) is bounded by n! and O(n^2) is the time complexity of copying the board
# T = n! + O(n!n^2)

# Space complexity is merely the space taken up by the output, 
# which is O(n!n^2) because there are n! solutions and each 
# solution is n^2

# You would think here that nT(n-1) = n^n, but actually n shrinks by 1
# every recurrence. Therefore a constant like 2 is more powerful than
# n in the recurrence, and nT(n-1) = n!