# 그냥 싹 다 BFS 돌리는 코드 + heapq
import heapq

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1,0,0,1]
dj = [0,-1,1,0]

def bfs():
    Q = []
    heapq.heappush(Q, (0, si, sj))

    visit = [[-1]*n for _ in range(n)]

    while Q:
        dist, row, col = heapq.heappop(Q)

        for k in range(4):
            ni, nj = row + di[k], col + dj[k]

            if not (0 <= ni < n and 0 <= nj <n):
                continue
            if visit[ni][nj] != -1:
                continue
            if arr[ni][nj] > level:
                continue







# 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[si][sj] = 0