def count_strings(n):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = dp[0][2] = 1

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
        dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]

    return dp[n][0] + dp[n][1] + dp[n][2]

n = int(input())
print(count_strings(n))
