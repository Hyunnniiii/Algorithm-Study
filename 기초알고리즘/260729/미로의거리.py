# 0 통로 / 1 벽 / 2 출발 / 3 도칙
# 지나는 0의 개수 = 거리, 경로가 없으면 0

for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    route = [[0]*N for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_r, start_c = i, j
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = [[start_r, start_c]]

    while q:
        r, c = q.pop(0)
        answer = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < N:
                # 0이 있으면
                if arr[nr][nc] == 0:
                    q.append([nr, nc])
                    arr[nr][nc] = 1
                    route[nr][nc] = route[r][c] + 1
                # 3이 있으면 큐를 비우고 거리 계산
                elif arr[nr][nc] == 3:
                    q = []
                    answer = route[r][c]
                    break
    print(f'#{T} {answer}')
