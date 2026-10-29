# 11:05 ~

# 탈출구까지 이동하는데 걸리는 최소 시간 (불가능하면 -1)
# ================================
from collections import deque


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


def in_range_brr(nr,nc):
    return 0<=nr<3*M and 0<=nc<3*M

# 십자가 이어주기
def change_loc(r, c):
    if r == M-1 and 0<=c<M:
        return c, r+1
    elif r == M-1 and 2*M<=c<3*M:
        return 3*M-c-1, 3*M-(r+1)-1
    elif 0<=r<M and c==M-1:
        return c+1, r
    elif 0<=r<M and c==2*M:
        return 3*M-(c-1)-1, 3*M-r-1
    elif r==2*M and 2*M<=c<3*M:
        return 3*M-c-1, 3*M-(r-1)-1
    elif 2*M<=r<3*M and c==M-1:
        return 3*M-(c+1)-1, 3*M-r-1
    elif 2*M<=r<3*M and c==2*M:
        return c-1, r
    elif r==2*M and 2*M<=c<3*M:
        return c, r-1
    else:
        return r, c

def bfs():
    Q = deque()
    Q.append((sr, sc))
    visit = [[-1]*(3*M) for _ in range(3*M)]
    visit[sr][sc] = 0

    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            nr, nc = change_loc(nr,nc)

            if not in_range_brr(nr, nc) or visit[nr][nc]!=-1:
                continue
            if brr[nr][nc] == 1:
                continue
            if nr==er and nc==ec:
                return visit[r][c] + 1
            Q.append((nr, nc))
            visit[nr][nc] = visit[r][c] + 1

        for row in visit:
            print(row)
        print()


def bfs2():
    Q = deque()
    Q.append((br, bc))
    visit = [[-1]*N for _ in range(N)]
    visit[br][bc] = 0

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr, nc) or visit[nr][nc] != -1:
                continue
            if arr[nr][nc] == 1 or arr[nr][nc] == -1 or arr[nr][nc] == 3:
                continue

            # 탈출구 찾았다면
            if arr[nr][nc] == 4:
                pass

            # 경로라면



def debug_print(msg):
    if DEBUG:
        print(msg)
        print('평면도')
        for row in arr:
            print(row)
        print()
        print('3차원')
        for row in brr:
            print(row)
        print()

##################
DEBUG = True
N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
east = [list(map(int, input().split())) for _ in range(M)]
west = [list(map(int, input().split())) for _ in range(M)]
south = [list(map(int, input().split())) for _ in range(M)]
north = [list(map(int, input().split())) for _ in range(M)]
central = [list(map(int, input().split())) for _ in range(M)]

# 3차원 평면 만들기
brr = [[0]*(3*M) for _ in range(3*M)]
# 중앙
for row in range(M, 2*M):
    for col in range(M, 2*M):
        brr[row][col] = central[row-M][col-M]
# 남쪽
for row in range(2*M, 3*M):
    for col in range(M, 2*M):
        brr[row][col] = south[row-2*M][col-M]
# 동쪽
east = [list(row[:]) for row in zip(*east)][::-1]
for row in range(M, 2*M):
    for col in range(2*M, 3*M):
        brr[row][col] = east[row-M][col-2*M]
# 서쪽
west = [list(row[:]) for row in zip(*west[::-1])]
for row in range(M, 2*M):
    for col in range(M):
        brr[row][col] = west[row-M][col]
# 북쪽
north = [list(row[:]) for row in zip(*north)][::-1]
north = [list(row[:]) for row in zip(*north)][::-1]
for row in range(M):
    for col in range(M, 2*M):
        brr[row][col] = north[row][col-M]

# 이상 현상
time = [[float('inf')]*N for _ in range(N)]
weird = []
for _ in range(F):
    r, c, d, v = map(int, input().split())
    weird.append([r, c, d, v])
    arr[r][c] = -1
    time[r][c] = 0

# 우좌하상
dr = [0,0,1,-1]
dc = [1,-1,0,0]


# 출구 위치 찾기
status, sr, sc = False, None, None
for row in range(N):
    for col in range(N):
        if arr[row][col] == 3:
            sr, sc = row, col
            status = True
            break
    if status:
        break

status = False
exit_d, br, bc = None, None, None
for row in range(sr, sr+M):
    for col in range(sc, sc+M):
        for k in range(4):
            nr, nc = row + dr[k], col + dc[k]

            if not in_range(nr, nc):
                continue
            if arr[nr][nc] == 0:
                exit_d = k
                br, bc = nr, nc
                status = True
                break
        if status:
            break
    if status:
        break

if exit_d == 0:
    er, ec = M+(br-sr), 3*M-1
elif exit_d == 1:
    er, ec = M+(br-sr), 0
elif exit_d == 2:
    er, ec = 3*M-1, M+(bc-sc)
elif exit_d == 3:
    er, ec = 0, M+(bc-sc)

############################

# [1] 3차원에서 bfs
# 시작 위치 찾기
find = False
for r in range(3*M):
    for c in range(3*M):
        if brr[r][c] == 2:
            sr,sc = r, c
            find = True
            break
    if find:
        break

# 출구 갈 때까지 bfs 돌리기
time = bfs()

# 이상현상 생기는 시간 배열에 다 표시해두기
for idx in range(len(weird)):
    r, c, d, v = weird[idx]

    for length in range(1, N+1):
        nr, nc = r + dr[d]*length, c + dc[d]*length

        if not in_range(nr, nc):
            break
        if arr[nr][nc] == 1:
            break
        time[nr][nc] = v*length
        weird[idx][0], weird[idx][1] = nr, nc






