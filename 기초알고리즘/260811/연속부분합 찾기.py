N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N
dp[0] = lst[0]

for i in range(1, N):
    # 지금까지 연속합 중 최대 vs 현재 위치에서 다시 시작
    dp[i] = max(lst[i], dp[i-1] + lst[i])

# 아무 배열도 택하지 않는 게 최대일 수 있다
print(max(0, max(dp)))