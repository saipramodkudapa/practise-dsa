
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[None for i in range(W+1)] for i in range(n)]

    for r in range(n):
        dp[r][0] = 0

    for c in range(W+1):
        dp[0][c] = values[0] if weights[0] <= c else 0

    for r in range(1, n):
        for w in range(1, W+1):
            if weights[r] <= w:
                dp[r][w] = max(values[r] + dp[r-1][w-weights[r]], dp[r-1][w])
            else:
                dp[r][w] = dp[r-1][w]
    return dp[n-1][W]


wts = [5, 3, 4, 2]
values = [60, 50, 70, 30]
output = knapsack(wts, values, 5)
print(output)
