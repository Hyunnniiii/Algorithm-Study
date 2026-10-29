
"""
아기 고래의 첫 항해 / 20261002

[선정 사유]
- 방향 우선순위를 `k in (0,-1,1,2)`로 표현해 복잡한 방향 분기를 간단하게 구현
- 깔-끔한 풀이. 귀여운 변수명. >_<

[시간 복잡도]
 N^4

[엣지 케이스]
5 3 3 2
0 0 0 1 1
1 1 0 1 1
1 1 0 0 0
1 1 0 1 1
1 1 0 1 1

- 정답:
3 3
4 3
5 3
2 3
1 3
1 2
1 1
3 4
3 5

선정 사유
: 가장 가까운 칸 선택 후 sorting을 하지 않은 경우 오답 출력


"""

# 구할 것: 방문하는 바다 칸의 위치 출력 (시간 칸 포함)

# =============================================
from collections import deque

# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


# 인접 탐험
def gore_go_1(gr, gc, gd):
    while True:
        visited_sea[gr][gc] = 1
        rgr, rgc, rgd = gr, gc, gd
        for k in (0,-1,1,2):
            nr, nc = gr + dr[(gd+k)%4], gc + dc[(gd+k)%4]

            if not in_range(nr, nc) or arr[nr][nc] == 1:
                continue
            if visited_sea[nr][nc]:
                continue

            gr, gc, gd = nr, nc, (gd+k)%4
            break

        if rgr==gr and rgc==gc:
            break
        print(gr + 1, gc + 1)
    return rgr, rgc, rgd


# 가장 가까운 바다로 이동
def gore_go_2(gr, gc):
    Q = deque()
    Q.append((gr, gc))
    visit = [[-1]*N for _ in range(N)]
    visit[gr][gc] = 0
    hubo = []
    dist = float('inf')

    while Q:
        sr, sc = Q.popleft()

        # 더 먼 거리가 나오기 시작하면 끝내기
        if visit[sr][sc] >= dist:
            break

        for k in range(4):
            nr, nc = sr + bdr[k], sc + bdc[k]

            if not in_range(nr, nc) or visit[nr][nc] != -1:
                continue
            if arr[nr][nc] == 1:
                continue

            if visited_sea[nr][nc] == 0:
                visit[nr][nc] = visit[sr][sc]+1
                dist = visit[nr][nc]
                hubo.append((nr, nc, k))

            else:
                Q.append((nr, nc))
                visit[nr][nc] = visit[sr][sc] + 1

    # 갈 수 있는 곳이 없다면
    if not hubo:
        return None, None, None

    hubo.sort(key = lambda x : (x[0], x[1]))
    return hubo[0][0], hubo[0][1], hubo[0][2]


######################
N, gore_r, gore_c, gore_d = map(int, input().split())
gore_r -= 1
gore_c -= 1

change = [None, 0, 2, 3, 1]
change2 = [3,2,1,0]
gore_d = change[gore_d]

arr = [list(map(int, input().split())) for _ in range(N)]
visited_sea = [[0]*N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
            visited_sea[row][col] = 1

# 상우하좌 (1번용)
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 좌하우상 (2번용)
bdr = [0,1,0,-1]
bdc = [-1,0,1,0]


## 실행
print(gore_r+1, gore_c+1)   # 첫 위치
while True:
    # [1] 인접 탐험
    gore_r, gore_c, gore_d = gore_go_1(gore_r, gore_c, gore_d)

    # [2] 가장 가까운 바다로 이동
    gore_r, gore_c, gore_d = gore_go_2(gore_r, gore_c)

    # 못 간다면
    if gore_d is None:
        break

    print(gore_r+1, gore_c+1)
    visited_sea[gore_r][gore_c] = 1
    gore_d = change2[gore_d]