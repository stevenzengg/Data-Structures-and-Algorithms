#STEVEN SOLUTION
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])
        for col in range(len(ans)):
            for i in range(len(grid)):
                ans[col] = max(ans[col], self.length(grid[i][col]))
        return ans

    def length(self, num):
        ans = 0
        if num <= 0:
            ans += 1
            num*=-1
        
        while num:
            num, carry = divmod(num, 10)
            ans += 1
        return ans
        