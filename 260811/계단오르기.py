# 연속 3개 불가, 한칸 또는 두칸만 이동 가능
# 마지막 계단 반드시 밟음, 시작점은 계단x

N = int(input())    # 계단의 개수
stair = list(int(input()) for _ in range(N))     # 계단의 점수

# N = 1일 때
if N == 1:
    print(stair[0])
else:
    # 1칸 전에서 올 때 / 2칸 전에서 올 때
    dp = [0]*(N+1)
    dp[1] = stair[0]
    dp[2] = max(dp[1]+stair[1], stair[1])

    for k in range(3, N+1):
        if dp[k] == 0:
            dp[k] = max(dp[k-2] + stair[k-1], dp[k-3] + stair[k-2] + stair[k-1])

    print(dp[N])

################## 인댁싱 너무 헷갈려서 수정

N = int(input())    # 계단의 개수
stair = [0] + list(int(input()) for _ in range(N))     # 계단의 점수

dp = [0]*(N+1)
dp[1] = stair[1]

if N >= 2:
    dp[2] = stair[1] + stair[2]    # 모두 자연수라 이게 최대

    # 1칸 전에서 올 때 / 2칸 전에서 올 때
    for k in range(3, N+1):
        dp[k] = max(dp[k-2] + stair[k], dp[k-3] + stair[k-1] + stair[k])

print(dp[N])
