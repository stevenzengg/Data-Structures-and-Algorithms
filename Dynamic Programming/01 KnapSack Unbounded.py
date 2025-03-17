class Solution():

    def KnapSack(self, W, wt, val):
        n = len(wt)
        dp = [0 for _ in range(W+1)]
        for weight in range(1, W+1):
            for knapsack in range(len(wt)):
                if wt[knapsack] <= weight:
                    dp[weight] = max(val[knapsack] + dp[weight - wt[knapsack]], dp[weight-1], dp[weight])
                else:
                    dp[weight] = max(dp[weight], dp[weight-1])
        
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    W = 100
    val = [10, 30, 20]
    wt = [5, 10, 15]
    n = len(val)
 
    print(a.KnapSack(W, wt, val))