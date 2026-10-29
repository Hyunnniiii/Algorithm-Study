# 1 벽 / 2 출발 / 3 도착 / 0 통로
def dfs(si, sj):
    # 방문
    visit[si][sj] = 1

    # 연결된 노드 -> 4개 방향
    # 이때 범위 체크 & 미방문 확인 & 조건 맞으면 -> dfs 호출
    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
        ni, nj = si + di, sj + dj

        if 0 <= ni < N and 0 <= nj < N:
            if visit[ni][nj] == 0 and miro[ni][nj] != 1:
                dfs(ni, nj)

for T in range(1, int(input()) + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    # 출발, 도착 위치 저장
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_i, start_j = i, j
            elif miro[i][j] == 3:
                end_i, end_j = i, j

    dfs(start_i, start_j)
    print(f'#{T} {visit[end_i][end_j]}')


