class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.helper(word1, word2, memo)
    def helper(self, word1, word2, memo):
        if (word1, word2) in memo:
            return memo[(word1, word2)]
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        ans = float('inf')
        if word1[0] == word2[0]:
            ans = self.helper(word1[1:], word2[1:], memo)
        else:
            ans = 1 + min(self.helper(word1[1:], word2, memo), self.helper(word1[1:], word2[1:], memo), self.helper(word1, word2[1:], memo))
        memo[(word1, word2)] = ans
        return ans
    

# The number of unique subproblems is the number of unique pairs of
# substrings O(n*m). The work done per subproblem is O(3m) where m
# is the longer string. Therefore,
# Time complexity: O(n*m^2), Space complexity: O(n*m) for memo

# Now, without memoization, we derive the recurrence relation
# T(m) = 3T(m-1) + O(m) = O(m3^m). We can reduce this to O(3^m) by
# using indices.
# Time complexity: O(3^(m)), Space complexity: O(m) where m is the size