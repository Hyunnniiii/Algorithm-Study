# 최소 이동 횟수 > bfs
N, M = map(int, input().split())
R, C, S, K = map(int, input().split())

# 8방향
di = [-1,-2,-2,-1,1,2,2,1]
dj = [-2,-1,1,2,-2,-1,1,2]

from collections import deque
q = deque()
q.append((R, C))

visit = [[0]*M for _ in range(N)]

def bfs():

    while q:
        si, sj = q.popleft()

        if R == S and C == K:
            break

        for k in range(8):
            ni, nj = si + di[k], sj + dj[k]

            if 1 <= ni <= N and 1 <= nj <= M:
                if visit[ni-1][nj-1] == 0:
                    visit[ni-1][nj-1] = visit[si-1][sj-1] + 1
                    q.append((ni, nj))

bfs()
print(visit[S-1][K-1])