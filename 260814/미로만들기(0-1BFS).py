N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]
visit = [[float('inf')]*N for _ in range(N)]

def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    visit[si][sj] = 0

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            break

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] > visit[ci][cj] + (1 - arr[ni][nj]):
                # 흰 방일 때
                if arr[ni][nj] == 1:
                    q.appendleft((ni, nj))
                    visit[ni][nj] = visit[ci][cj]

                # 검은 방일 때
                if arr[ni][nj] == 0:
                    q.append((ni, nj))
                    visit[ni][nj] = visit[ci][cj] + 1
bfs(0,0,N-1,N-1)
print(visit[N-1][N-1])