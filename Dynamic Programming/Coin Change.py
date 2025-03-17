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

            