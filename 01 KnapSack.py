def knapSack(W, wtVal, n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for knapsack in range(1, n+1):
        for weight in range(1, W+1):
            if wtVal[knapsack-1][0] <= weight:
                dp[knapsack][weight] = max(dp[knapsack-1][weight], wtVal[knapsack-1][1] + dp[knapsack - 1][weight - (wtVal[knapsack-1][1])])
            else:
                dp[knapsack][weight] = dp[knapsack-1][weight]
    
    return dp[-1][-1]
# Driver code

wtVal = [(2,10), (1,6), (3,12)]
W = 10
n = len(wtVal)
print(knapSack(W, wtVal, n))