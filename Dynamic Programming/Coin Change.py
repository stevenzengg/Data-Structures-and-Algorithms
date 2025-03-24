class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        self.dfs(coins, amount, dp)
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def dfs(self, coins, amount, dp):
        if amount in dp:
            return dp[amount]
        ans = float('inf')
        for coin in coins:
            if amount - coin >= 0:
                ans = min(ans, 1 + self.dfs(coins, amount - coin, dp))
        dp[amount] = ans 
        return ans


# The number of unique subproblems is amount. At every amount, the
# subproblem is the least number of coins to get to 0. The
# work done per subproblem is O(len(coins)) for the loop. Therefore,

# Time complexity: O(amount * len(coins)), Space complexity: O(amount)
# The space complexity is O(amount) because we memoize the number 
# of coins


# Let's practice recurrence relations! Without memoization, the 
# recurrence relation is: T(n) = mint(T(A-C0), T(A-C1), ..., T(A-Ck)) + O(k)
# where A is amount, C0, C1, ..., Ck are the coins, and k is the number 
# of coins. This can be simplified to T(n) = kT(A-...) + O(k) = O(k*2^k).
# Again, this is a very loose bound since A shrinks by the value of the
# coins, not just 1.