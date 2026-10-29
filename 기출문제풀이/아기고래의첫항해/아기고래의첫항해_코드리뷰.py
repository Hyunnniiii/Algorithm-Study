
''' 아기 고래의 첫 항해 / 20261002 / 체감 난이도 : 실버
소요 시간: 1h 18m / 시도: 1회 / 실행 시간: 133ms (코드트리) / 메모리: 21MB

[타임라인]
09:00 - 09:38 (38분) 문제 읽기, 손구상, 주석구상, 입력 받기
09:38 - 10:15 (37분) 구현
10:15 - 10:18 (3분) 간단히 검증, 제출


[구상]
- bfs 설명 너무 이상해서 한참 봤다. 그니까 최단거리인데 행열 작아야되는데 좌하우상 순서이고..
가는 동안 거리가 감소해야 한다고?
이 부분에서 5분 정도 고민했는데, 일단 내린 결론은
1. 매 이동마다 거리가 1 줄어드는: 실제 거리 말고, 앞에서 bfs로 구한 거리가 줄어든다고 간주
2. 행열 작은, 좌하우상: 이건.. 그냥 좌하우상으로 탐색해서 방향 저장하고, 같은 거리는 일단 다 모아서
sort도 하는 식으로 안전하게 처리하기로 결정했다.
두 조건을 따로 줘서 행열 작으면서 좌하우상인거를 처리를 따로 해야하나? 했는데 아무리 생각해도
그렇진 않았음


[구현]
- 방향으로 장난을 좀 많이 쳐놔서 구현 중간에 각 단계용 dr/dc를 그냥 만들었다.
좀 더 머리써서 하나로 잘 써먹을까? 했는데 응 절대 묘수 금지 모르면 그냥 써서 해
- 오용하지 않기 위해 주석에 주의하라고 잘 써둠
- 어제 자율주행 자동차 풀었는데 정말 유사하다. 시작/종료 처리를 잘해야 하는 문제였는데,
오늘 문제도 상당히 비슷한 흐름으로 풀이했다.


[디버깅]
- 디버깅 프린트 쓰지도 못했다. 쩝
- 제출 전 N=1인 케이스, 시작점에서 아무곳도 못 가는 케이스 모두 검증해봤는데 정말
드물게도 다 맞게 나와서 고민 좀 하다가 용기내서 제출했다


[후기]
- 묘수 금지
- 방심 금지. 바로 왕실의 기사, 메두사, 루돌프의 반란 풀면서 경각심 가져

'''
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


def debug_print(msg):
    if DEBUG:
        print(msg)
        print('현재 고래 위치: ', gore_r, gore_c)
        print('현재 고래 방향: ', gore_d)
        print()
        print('현재 방문한 칸')
        for row in visited_sea:
            print(row)
        print()

######################
DEBUG = False
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

    # 종료 확인: 모든 바다를 탐험했는가?
    if sum(map(sum, visited_sea)) == N*N:
        break

    # [2] 가장 가까운 바다로 이동
    gore_r, gore_c, gore_d = gore_go_2(gore_r, gore_c)

    # 못 간다면
    if gore_d is None:
        break

    print(gore_r+1, gore_c+1)
    visited_sea[gore_r][gore_c] = 1
    gore_d = change2[gore_d]

    # 종료 확인: 모든 바다를 탐험했는가?
    if sum(map(sum, visited_sea)) == N * N:
        break