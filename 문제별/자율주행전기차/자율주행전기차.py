
# 최단거리의 승객을 우선적으로 태우고, 그 승객의 목적지로 간다.
# 작은 행 > 작은 열 우선!! 이거 주의할 것. 무조건 작은 행으로 비교 다 한 다음에 열 비교
# 목적지로 가면, (이 승객을 태우러 가는 비용 + 태우고 목적지로 간 비용)의 2배를 충전한다
# 종료되는 경우: 이동 중 배터리 모두 소모. 단, 목적지에서 0이 되면 충전된다.
# 마지막 승객을 태워주고 운행 종료하는 순간에도 충전

# 구할 것: 모든 사람을 이동시킨 뒤 남은 연료의 양. (모두 이동 불가하면 -1)
# 근데.. 만약 어떤 승객의 사방이 벽으로 막혀있으면 어카지
# 문제에서 관련 내용 언급한 것 있나? >> 없음 >> 애초에 갈 수 있는지 먼저 확인할까

# 중요
# 작은 행, 작은 열 순서 >> 이거 그냥 방향 설정으로 안되고, 같은 거리 다 모아둔 뒤에 비교해라
# 목적지에서 0이면 충전, 마지막 승객 완료 후 충전
# 한 승객의 출발지와 다른 승객의 목적지가 같을 수 있다 > 어떻게 처리?
# 승객이 벽으로 둘러싸인 경우?

# 나의 실수 리스트
# 1. 승객 찾는 BFS를 복붙해서 도착지 찾기 BFS에 써먹었더니 조건 다른 부분에서 수정 안해서 틀림.
#   승객은 그냥 벽이나 빈칸이 아니면 바로 찾은거고, 도착지는 정확한 그 숫자를 찾아야 끝인건데
#   도착지도 벽이나 빈칸 아니면 종료되게 하고 제출함 스튜핏
# 2. 불가능한 조건 생각 못함. 사방이 막혀서 못 가는건 생각했는데, 그냥 일렬 벽으로 막혀있을 수
#  있다는걸 생각 못함.
# 3. ㅎ ㅏ.................. 서로 다른 플레이어의 도착점이 같을 수 있다는 걸 전혀 생각 못하고
#   도착점 그냥 배열에 숫자로 받음. 그래서 특정 번호의 도착점이 사라지는 이상한 사건 발생
#   진짜 열받네. 생각해야 될게 이렇게 많다고?

# ===================
## 제출할 때 지워라
# import pprint

from collections import deque
from copy import deepcopy
## 입력 받기
N, M, battery = map(int, input().split())

# arr: 벽, 빈칸, 승객 출발지 저장
arr = [list(map(int, input().split())) for _ in range(N)]
brr = [[[] for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            arr[x][y] = -1  # 승객번호 입력을 위해 벽은 -1로 변경
        if arr[x][y] == -1:
            brr[x][y].append(-1)

car_x, car_y = map(lambda x : int(x)-1, input().split())    # 전기차의 위치
for idx in range(1, M+1):
    sx, sy, ex, ey = map(lambda x : int(x)-1, input().split())
    arr[sx][sy] = idx
    brr[ex][ey].append(idx)

## 필요한 요소 생성
# 0. 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 1. 범위 체크 함수
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 2. 가장 가까운 거리의 승객 찾기
def find(sr, sc):       # 이거 입력 차 좌표로 해야함
    global battery, car_x, car_y
    Q = deque([[sr,sc]])
    lst = []    # 같은 거리의 승객 담을 리스트
    visit = [[-1]*N for _ in range(N)]
    visit[sr][sc] = 0
    remember1 = float('inf')    # 승객을 찾았다면, 이 거리까지만 찾으라는 표시

    # 만약 출발점에 승객이 있다면
    if arr[sr][sc] > 0:
        remember1 = 0
        lst.append((sr, sc))
        Q = []

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr + di[k], sc + dj[k]

            # 승객 찾으면 > 그 거리까지만 탐색
            if in_range(nr, nc) and arr[nr][nc] > 0 and visit[nr][nc] == -1:
                visit[nr][nc] = visit[sr][sc] + 1
                if visit[nr][nc] <= remember1:
                    remember1 = visit[nr][nc]
                    lst.append((nr, nc))

            # 승객이 없으면 > 그 다음 진행
            if in_range(nr, nc) and arr[nr][nc] == 0 and visit[nr][nc] == -1:
                # 승객을 찾았다면, 그 거리까지만 진행해야함
                visit[nr][nc] = visit[sr][sc] + 1
                if visit[nr][nc] > remember1:
                    Q = []
                    break

                else:
                    Q.append([nr, nc])

    # 막혀서 못 가는 경우가 있었네..
    if not lst:
        print(-1)
        exit()

    # 여기서 우선순위에 따른 승객을 정한다
    lst.sort(key = lambda x : (x[0], x[1]))
    car_x, car_y = lst[0][0], lst[0][1]     # 차 위치 갱신
    goal = arr[car_x][car_y]    # 목적지 승객 번호 설정
    arr[car_x][car_y] = 0   # 승객 태웠으므로 배열에서 삭제

    # 배터리 체크. 이제 막 태운거니까 여기서 배터리 고갈되면 끝
    battery -= remember1
    if battery <= 0:
        print(-1)
        exit()

    # 다음 함수를 위해 목적지 idx를 반환
    return goal

# 3. 목적지로 가는 함수
def letsgo(goal, sr, sc):     # 입력: 차 좌표
    global battery, car_x, car_y
    Q = deque([[sr,sc]])
    visit = [[-1]*N for _ in range(N)]
    visit[sr][sc] = 0
    remember2 = 0
    ok = False

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr + di[k], sc + dj[k]

            # 목적지 찾으면 > 끝
            if in_range(nr, nc) and goal in brr[nr][nc]:
                visit[nr][nc] = visit[sr][sc] + 1
                remember2 = visit[nr][nc]
                car_x, car_y = nr, nc   # 차 좌표 업데이트
                Q = []
                ok = True
                break

            # 없으면 > 그 다음 진행
            if in_range(nr, nc) and brr[nr][nc] != [-1] and visit[nr][nc] == -1:
                visit[nr][nc] = visit[sr][sc] + 1
                Q.append([nr, nc])

    # 목적지로 가는 길이 없다면
    if not ok:
        print(-1)
        exit()

    # 배터리 부족했는지 확인
    if battery - remember2 < 0:
        print(-1)
        exit()

    # 배터리 갱신
    battery -= remember2
    battery += remember2 * 2
    return

## 실행
cnt = 0
while cnt < M:
    goal = find(car_x, car_y)
    letsgo(goal, car_x, car_y)

    cnt += 1
print(battery)