# 몬스터 발견했을 때 그 거리의 몬스터까지만 BFS 하고싶음
# 조금 더 깔끔하게 하기. global 변수가 너무 많다..
# BFS 함수로는 몬스터의 거리까지 찾고 끝내고 그 뒤의 작업 분리

from collections import deque

## [0] 입력 받기
n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

# 4방향
di = [-1,0,0,1]
dj = [0,-1,1,0]

## [1] 최단 거리의 몬스터 찾기
def bfs(si, sj, level):
    Q = deque([(si, sj)])
    visit = [[-1]*n for _ in range(n)]
    visit[si][sj] = 0

    min_dist = -1
    hubo = []

    while Q:
        i, j = Q.popleft()

        if min_dist != -1 and visit[i][j] >= min_dist:
            continue

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            # 범위내, 미방문, 몬스터 레벨
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if visit[ni][nj] != -1:
                continue
            if arr[ni][nj] > level:
                continue

            visit[ni][nj] = visit[i][j] + 1
            Q.append((ni, nj))

            # 몬스터를 찾으면
            if 0 < arr[ni][nj] < level:
                hubo.append((ni, nj))
                min_dist = visit[ni][nj]

    if not hubo:
        return

    hubo.sort()
    i, j = hubo[0]

    return i, j, min_dist

# 전체 실행
# 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[si][sj] = 0
tot_time = 0
kill = 0
level = 2
while True:
    result = bfs(si, sj, level)

    if result is None:
        break
    si, sj, dist = result

    arr[si][sj] = 0
    kill += 1
    tot_time += dist

    if kill == level:
        kill = 0
        level += 1
print(tot_time)

