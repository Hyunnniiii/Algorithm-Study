# 1이면 탐색 시작. 근데 모든 지점에서 다 볼거임
# 가장 먼 길이를 저장, 이때 좌표도 같이 저장.
# 갱신할 때 최대값보다 커야만 갱신. 그래야 작은 행/열 번호로 선택됨
# 마지막에 출력할 때 좌표 인덱스 +1 해줘야됨 주의

for TC in range(1, int(input())+1):
    # N행 M열
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    from collections import deque

    max_length = -1
    for row in range(N):
        for col in range(M):
            visit = [[-1]*M for _ in range(N)]    # 거리 표시

            # 암석지대(1)일 때 시작
            if arr[row][col] == 1:
                q = deque()
                q.append((row, col))
                visit[row][col] = 0
                ans_row, ans_col = row, col

                while q:
                    si, sj = q.popleft()

                    for k in range(4):
                        ni, nj = si + di[k], sj + dj[k]

                        if 0 <= ni < N and 0 <= nj < M:
                            if arr[ni][nj] == 1 and visit[ni][nj] == -1:
                                visit[ni][nj] = visit[si][sj] + 1
                                q.append((ni, nj))

                # 가장 먼 최단거리, 좌표 구하기
                for x in range(N):
                    for y in range(M):
                        if visit[x][y] > max_length:
                            max_length = visit[x][y]
                            lst = [x, y, visit[x][y], ans_row, ans_col]

    print(f'#{TC} {lst[3]+1} {lst[4]+1}')