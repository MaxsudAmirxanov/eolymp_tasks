def min_energy(h):
    n = len(h)
    dp = [0] * n
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))
    return dp[-1]

h = list(map(int, input().split()))
print(min_energy(h))
