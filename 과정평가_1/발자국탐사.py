# 3 <= N <= 50, 1 <= K <= 10, 1 <= C <= 9
for T in range(1, int(input())+1):
    # N 유적지 크기 / K 좌표 수 / C 찾을 색깔
    N, K, C = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    for _ in range(1, K+1):
        # 행/열/높이/너비/색깔
        row, col, height, width, color = map(int, input().split())

        for i in range(row, row+height):
            for j in range(col, col+width):
                arr[i][j] = color

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == C:
                cnt += 1
    print(f'#{T} {cnt}')
