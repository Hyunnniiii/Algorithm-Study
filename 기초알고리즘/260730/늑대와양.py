R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

# 초기 세팅
visit = [[0]*C for _ in range(R)]
q = []

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 탐색 시작
tot_sheep = 0
tot_wolf = 0

for x in range(R):
    for y in range(C):
        if arr[x][y] != '#' and visit[x][y] == 0:
            q.append([x,y])
            visit[x][y] = 1

            sheep = 0
            wolf = 0

            # 시작점에 양이나 늑대 있을 경우
            if arr[x][y] == 'o':
              sheep = 1
            if arr[x][y] == 'v':
                wolf = 1

            while q:
                cur_i, cur_j = q.pop(0)

                for k in range(4):
                    ni, nj = cur_i + di[k], cur_j + dj[k]

                    # 울타리가 아니면 시작
                    if 0 <= ni < R and 0 <= nj < C:
                        if arr[ni][nj] != '#' and visit[ni][nj] == 0:
                            visit[ni][nj] = 1
                            q.append([ni, nj])

                            # 양/늑대 수 구하고 처리
                            if arr[ni][nj] == 'o':
                                sheep += 1
                            elif arr[ni][nj] == 'v':
                                wolf += 1

            if sheep <= wolf:
                tot_wolf += wolf
            else:
                tot_sheep += sheep

print(tot_sheep, tot_wolf)


# --------
# 개선한 코드: 시작점 따로 세지 말고 카운트를 통일하기, 방문처리는 큐에 넣을 때 하기
# BFS    # 늑대와 양
from collections import deque

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

q = deque()
visit = [[0] * C for _ in range(R)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

tot_sheep, tot_wolf = 0, 0

for i in range(R):
    for j in range(C):
        # 울타리가 아니면 탐색 시작 (하나의 영역)
        if arr[i][j] == '#':
            continue

        if visit[i][j] == 0:
            q.append([i, j])
            visit[i][j] = 1

            sheep, wolf = 0, 0

            while q:
                start_i, start_j = q.popleft()

                if arr[start_i][start_j] == 'o':
                    sheep += 1
                elif arr[start_i][start_j] == 'v':
                    wolf += 1

                for k in range(4):
                    ni, nj = start_i + di[k], start_j + dj[k]

                    if 0 <= ni < R and 0 <= nj < C:
                        if arr[ni][nj] != '#' and visit[ni][nj] == 0:
                            visit[ni][nj] = 1
                            q.append([ni, nj])

            if sheep > wolf:
                tot_sheep += sheep
            else:
                tot_wolf += wolf

print(tot_sheep, tot_wolf)
