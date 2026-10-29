# N, M = map(int, input().split())
# R, C, S, K = map(int, input().split())
#
# # 8방향
# di = [-1,-2,-2,-1,1,2,2,1]
# dj = [-2,-1,1,2,-2,-1,1,2]
#
# #
# visit = [[0]*M for _ in range(N)]
# visit[R-1][C-1] = 1
#
# min_cnt = float('inf')
# def mar(si, sj, cnt):
#     global min_cnt
#     # 가지치기
#     if cnt >= min_cnt:
#         return
#     # 종료조건: 말 잡았을 때
#     if si == S and sj == K:
#         min_cnt = cnt
#         return
#     # 빈복
#     for k in range(8):
#         ni, nj = si + di[k], sj +dj[k]
#
#         if 1 <= ni <= N and 1 <= nj <= M:
#             if visit[ni-1][nj-1] == 0:
#                 visit[ni-1][nj-1] = 1
#                 mar(ni, nj, cnt + 1)
#                 visit[ni-1][nj-1] = 0
# mar(R,C,0)
# print(min_cnt)

# =============

# BFS
N, M = map(int, input().split())
R, C, S, K = map(int, input().split())

# 8방향
di = [-1,-2,-2,-1,1,2,2,1]
dj = [-2,-1,1,2,-2,-1,1,2]

from collections import deque
q = deque()
q.append((R, C))
visit = [[0]*M for _ in range(N)]

while q:
    si, sj = q.popleft()

    for k in range(8):
        ni, nj = si + di[k], sj + dj[k]

        if 1 <= ni <= N and 1 <= nj <= M:
            if visit[ni-1][nj-1] == 0:
                visit[ni-1][nj-1] = visit[si-1][sj-1] + 1
                q.append((ni, nj))

print(visit[S-1][K-1])



