# top-down으로 한거 > 메모리 초과 뜸
# N = int(input())
#
# dp = [0]*(N+1)
# dp[1] = 1
#
# def fibo(n):
#     if dp[n] == 0 and n >= 0:
#         dp[n] = fibo(n-1) + fibo(n-2)
#     return dp[n]
#
# x = fibo(N)
# print(x%1000000007)

# bottom-up
N = int(input())
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%1000000007)