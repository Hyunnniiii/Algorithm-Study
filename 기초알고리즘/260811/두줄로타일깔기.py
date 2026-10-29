N = int(input())

dp = [0] * N
dp[0] = 1
dp[1] = 3

for k in range(2, N):
    if dp[k] == 0:
        dp[k] = (dp[k-1] + 2*dp[k-2])%20100529
print(dp[N-1])