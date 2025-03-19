class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.recurse(s, p, 0, 0, memo)


    def recurse(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = False
        if j >= len(p):
            return i >= len(s)

        firstMatch = i < len(s) and p[j] in [".", s[i]]
        if j + 1 < len(p) and p[j + 1] == "*":
            return self.recurse(s, p, i, j + 2, memo) or (firstMatch and self.recurse(s, p, i + 1, j, memo))
        return firstMatch and self.recurse(s, p, i + 1, j + 1, memo)