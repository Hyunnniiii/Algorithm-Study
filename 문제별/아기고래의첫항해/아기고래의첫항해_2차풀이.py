
""" 아기 고래 / 20261008 / 체감 난이도: 골드5
소요 시간 36분 / 시도 1회 / 실행 시간 121ms (코드트리) / 메모리 18MB (코드트리)

고래 화이팅

"""

# 11:52 ~ 12:28

# 구할 것: 방문하는 바다 칸의 위치 순서대로 출력 (시작 포함)
# =============================
from collections import deque


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


def whale_move(cr, cc):
    Q = deque()
    Q.append((cr, cc))
    qvisit = [[-1]*N for _ in range(N)]
    qvisit[cr][cc] = 0
    dist = float('inf')
    hubo = []

    while Q:
        sr, sc = Q.popleft()

        if qvisit[sr][sc] >= dist:
            break

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr, nc) or qvisit[nr][nc]!=-1:
                continue
            if arr[nr][nc] == 1:
                continue

            if not visit[nr][nc]:
                dist = qvisit[sr][sc] + 1
                qvisit[nr][nc] = qvisit[sr][sc] + 1
                hubo.append((nr, nc, k))

            Q.append((nr, nc))
            qvisit[nr][nc] = qvisit[sr][sc] + 1

    if not hubo:
        return None, None, None

    hubo.sort(key = lambda x : (x[0], x[1]))
    return hubo[0]


################################
N, r, c, d = map(int, input().split())
change = [3,1,0,2]
cur_d = change[d-1]
cur_r = r-1
cur_c = c-1

arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
visit[cur_r][cur_c] = 1

# 좌하우상
dr = [0,1,0,-1]
dc = [-1,0,1,0]

print(cur_r+1, cur_c+1)
while True:
    # [1] 인접 탐험
    while True:
        sr, sc = cur_r, cur_c
        for k in (0,1,-1,2):
            nr, nc = cur_r + dr[(cur_d+k)%4], cur_c + dc[(cur_d+k)%4]

            if not in_range(nr, nc) or arr[nr][nc] == 1:
                continue
            if visit[nr][nc]:
                continue
            visit[nr][nc] = 1
            cur_r, cur_c, cur_d = nr, nc, (cur_d+k)%4
            print(cur_r+1, cur_c+1)
            break

        if cur_r == sr and cur_c == sc:
            break

    # [2] 가까운 바다로 이동
    cur_r, cur_c, cur_d = whale_move(cur_r, cur_c)

    if cur_r is None:
        break
    print(cur_r+1, cur_c+1)
    visit[cur_r][cur_c] = 1