class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, -1: 0}
        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        
        memo[n] = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
        return memo[n]
    

# For dynamic programming, the naive runtime can be calculated by
# recurrence relations. For example, here, the recurrence relation is
# T(n) = T(n-1) + T(n-2), which in big O, simplified to 2T(n-1) = O(2^n)
# The true asymptotic bound however, since T(n-2) shrinks much faster
# than T(n-1), can be calculated by the golden ratio, which is O(1.6^n)
# This is because the golden ratio is the limit of the ratio of two
# consecutive Fibonacci numbers.

# However, once memoized, it's easier to calculate time complexity
# by looking at the number of unique subproblems and multiplying by
# the work done per subproblem. Here, there are n unique subproblems
# and O(1) work done per subproblem. Therefore,

# Time complexity: O(n), Space complexity: O(n)

# Note that the space complexity can be reduced to O(1) by only storing
# the last two values in the memo dictionary in a bottom-up approach.
# This is because the current value only depends on the last two values.