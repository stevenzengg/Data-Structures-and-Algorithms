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
    

# There are s * p subproblems where s is the length of the string s
# and p is the length of the string p. We do O(1) work per subproblem.
# Therefore,
# Time complexity: O(s*p), Space complexity: O(s*p)



# Recurrence time! The recurrence relationship here is:
# T(i, j) = T(i, j + 2) + T(i + 1, j) if p[j + 1] == "*"
# T(i, j) = T(i + 1, j + 1) if p[j + 1] != "*"
# Let's break both down. The first one can be simplified to
# T(i, j) = 2T(i, j + 2) = 2^(i + j). The second one can be simplified to
# T(i, j) = T(i + 1, j + 1) = max(i, j). Therefore the time complexity
# is dominated by the first case, which is O(2^(i + j)).