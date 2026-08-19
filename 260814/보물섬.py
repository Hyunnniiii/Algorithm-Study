# 육지 L / 바다 W
# 상하좌우 이동, 한 칸 이동에 한 시간
# 보물 간 최단 거리로 이동하는 시간 구하기

R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

from collections import deque
q = deque()
lst = []

def bfs():
    for x in range(R):
        for y in range(C):
            # L이면 시작
            if map[x][y] == 'L':
                q.append((x, y))
                visit = [[-1] * C for _ in range(R)]
                visit[x][y] = 0

                while q:
                    si, sj = q.popleft()

                    for k in range(4):
                        ni, nj = si + di[k], sj + dj[k]

                        if 0 <= ni < R and 0 <= nj < C:
                            if map[ni][nj] == 'L' and visit[ni][nj] == -1:
                                visit[ni][nj] = visit[si][sj] + 1
                                q.append((ni, nj))

                max_route = 0
                for row in range(R):
                    for col in range(C):
                        max_route = max(visit[row][col], max_route)
                lst.append(max_route)

bfs()
print(max(lst))