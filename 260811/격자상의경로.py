
N, M, K = map(int, input().split())
dp = [[0]*M for _ in range(N)]

# 0행, 0열은 거리가 1
for x in range(N):
    for y in range(M):
        if x == 0 or y == 0:
            dp[x][y] = 1

# 나보다 위 & 왼쪽인 애들까지의 경우의 수를 더해주면 된다
# O 표시가 없으면 > 그냥 구하기
if K == 0:
    for x in range(N):
        for y in range(M):
            if dp[x][y] == 0:
                dp[x][y] = dp[x][y-1] + dp[x-1][y]
    print(dp[N-1][M-1])

# O 표시 있으면 > 중간 지점에서 한번 끊고 세기
if K != 0:
    row = (K-1) // M    # K의 행
    col = (K-1) % M     # K의 열

    for x in range(0, row+1):
        for y in range(0, col+1):
            if dp[x][y] == 0:
                dp[x][y] = dp[x][y - 1] + dp[x - 1][y]
    mid = dp[row][col]   # K까지의 거리

    # 다시 K를 시작점으로 끝점까지의 거리 구하기
    # K와 같은 행, 열은 거리 1
    for x in range(row, N):
        for y in range(col, M):
            if x == row or y == col:
                dp[x][y] = 1

            if dp[x][y] == 0:
                dp[x][y] = dp[x][y - 1] + dp[x - 1][y]
    end = dp[N-1][M-1]

    print(mid*end)