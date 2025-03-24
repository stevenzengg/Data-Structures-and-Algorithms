class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        self.hmaps = [defaultdict(int) for _ in range(len(words[0]))]
        for word in words:
            for i, v in enumerate(word):
                self.hmaps[i][v] += 1
        self.target = target
        return self.dfs(0, 0) % (10**9 + 7)
    @cache
    def dfs(self, i, j):
        if i == len(self.target):
            return 1
        if j == len(self.hmaps):
            return 0
        
        ans = self.hmaps[j][self.target[i]] * self.dfs(i + 1, j + 1) + self.dfs(i, j + 1)
        
        return ans


# There are mn subproblems where m is the length of a word in words 
# and n is the length of the target string. The work done per subproblem
# is O(1). Therefore,
# Time complexity: O(mn), Space complexity: O(mn)


# Recurrence time! 
# T(target, idx) = (letterCount) * T(target + 1, idx + 1) + T(target, idx + 1)
# T(target, idx) = T(target + 1, idx + 1) + T(target, idx + 1)
# T(target, idx) = 2T(target, idx + 1)
# Runtime Complexity: O(2^m)


