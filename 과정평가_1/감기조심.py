# 3 <= N, M <= 100
from collections import deque

for T in range(1, int(input())+1):
    N,M = map(int, input().split())   # N행 M열
    arr = [list(map(int, input().split())) for _ in range(N)]   # 교실 배치도

    # 감기 걸린 교육생 좌표: 1씩 빼줘야 함
    row, col = map(int, input().split())
    row, col = row - 1, col - 1

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    # 날짜 표시할 배열(visit), 다음에 탐색할 곳 큐
    visit = [[0]*M for _ in range(N)]
    visit[row][col] = 1
    q = deque()
    q.append([row, col])

    # 탐색 시작: 감기 걸린 사람부터
    while q:
        start_i, start_j = q.popleft()

        for k in range(4):
            ni, nj = start_i + di[k], start_j + dj[k]

            # 교실 범위 벗어나지 않으면서 방문하지 않은 칸일 때
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0:

                # 좌석에 학생이 있는 경우 > 날짜 표시, 큐 추가
                if arr[ni][nj] == 1:
                    visit[ni][nj] = visit[start_i][start_j] + 1
                    q.append([ni, nj])

    # 감기에 걸리는 날짜(max(arr)), 걸리지 않은 교육생 수 찾기
    # 걸리지 않은 교육생: arr에서는 1인데 visit에서 0
    last_cold = 0
    no_cold = 0
    for i in range(N):
        for j in range(M):
            # 날짜 찾기
            if last_cold < visit[i][j]:
                last_cold = visit[i][j]
            # 안 걸린 교육생 찾기
            if arr[i][j] == 1 and visit[i][j] == 0:
                no_cold += 1

    print(f'#{T} {last_cold} {no_cold}')


# x += 1 이거 안하고 그냥 visit[start_i][start_j] + 1 하면 됨