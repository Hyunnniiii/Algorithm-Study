
# 베이스캠프에서 출발해서 편의점으로 이동. 본인의 출발 시간 전에는 격자 밖에 있음.
# 목표 편의점은 모두 다르다 !!! > 같을 수 있는 것에 대해 생각
# idx초에 idx번 사람이 베이스캠프 결정

# [1] 본인이 목표한 편의점을 향해 1칸 이동
# - 격자에 들어온 사람의 경우임. 최단 거리로 이동. 상좌우하 우선순위 있음
# [2] 편의점에 도착했다면
# - 멈추고, 다른 사람들은 여기 못 지나감
# - 단, 해당 시간의 다른 사람들 다 이동한 뒤에 품절
# [3] idx번째 사람 베이스캠프 선정 (출발은 다음 턴에)
# - 본인이 가고싶은 편의점과 가장 가까운 베캠 들어간다
# - 작은 행 > 작은 열 우선순위
# - 이 과정은 시간 소요 없음
# - 베캠 선점하면, 다른 사람들은 여기 못 지나감. 마찬가지로 해당 턴 이동 완료 후에 품절

# 사람들의 이동은 동시에 이루어지는가?
# 동시에 vs 1번부터 차례로 이동할 때 뭐가 다름? > 해당 턴에 품절 안되니까 노상관
# 만약 1번이 가는 경로 도중에 다른 사람 편의점이 있는데 1번이 먼저 도착하고 그 턴에
# 다른 사람이 그 편의점을 선점하면 어떻게 되는거임? > 어차피 그 턴 지나고 못 지나감. ㄱㅊ
# 이동 도중에 선점하지 않은 베캠을 지나기 가능? > yes?
# 이동 도중 선점하지 않은 남의 편의점 지나기 가능? > yes?
# 사람들의 현재 위치 겹칠 수 있음.
# 가지 못하는 경우는 없다.
# 누가 어떤 편의점을 원하는지 입력에서 주어진게 읎는디?? 입력 순이라고 생각한다??

# 내가 꿈꾸고 있나
# 테케 왜 되는거임?
# 잘못 해석했네. 그 턴이라는게 이동하는 그 턴
# ===================================
from collections import deque

# 범위
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 상좌하우
di = [-1,0,1,0]
dj = [0,-1,0,1]

# [1] 내가 목표한 편의점에서 가장 가까운 베캠 찾기
def find_my_basecamp(idx):
    store_x, store_y = loc_info[idx][2], loc_info[idx][3]
    my_x, my_y = loc_info[idx][0], loc_info[idx][1]

    # 편의점 좌표에서 한 칸씩 뻗어나가면서 찾아
    Q = deque([[store_x, store_y]])
    visit = [[-1]*N for _ in range(N)]
    visit[store_x][store_y] = 0
    dist = float('inf')

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + di[k], c + dj[k]

            # 범위 내에 있고, 선점된 곳이 아니고, 방문한 적 없는 곳이어야 함
            if not in_range(nr, nc):
                continue
            if arr[nr][nc] == 2 or visit[nr][nc] != -1:
                continue
            # 먼 거리가 등장하기 시작하면 > 그만 혀
            if visit[r][c] + 1 > dist:
                Q = []
                break

            # 일단 전진 가능. 만약 베캠이 아니라면 > 다음 칸 진행
            if arr[nr][nc] != 1:
                Q.append([nr, nc])
                visit[nr][nc] = visit[r][c] + 1

            # 베캠을 만났다면 > 이 거리까지는 다 탐색 해주세요 & 행열 비교 후 결정
            if arr[nr][nc] == 1:
                visit[nr][nc] = visit[r][c] + 1
                dist = visit[nr][nc]

                if (my_x, my_y) > (nr, nc):
                    my_x, my_y = nr, nc

    # 골랐으면 사람 좌표 업데이트 (선점 표시는 나중에 턴이 끝나고 진행)
    loc_info[idx][0], loc_info[idx][1] = my_x, my_y
    base_change.append(idx)


# 본인이 목표한 편의점을 향해 1칸 이동
# - 격자에 들어온 사람의 경우임. 최단 거리로 이동. 상좌우하 우선순위 있음
# [2] 편의점까지 최단거리 구하고 한 칸 이동합시다 이거 백트래킹인가? 왜냐면 방향 우선순위 때문에
def move(idx, row, col, route, dist):   # 초기값: (사람 번호, 그 사람의 현 위치, [사람 위치], 0)
    global min_dist, store_x, store_y, to_go

    # 조기 종료: 최단 거리 넘어가버림
    if dist > min_dist:
        return

    # 종료: 내 편의점 찾았다
    if dist < min_dist:
        if row == store_x and col == store_y:
            min_dist = dist
            to_go = [route[1][0], route[1][1]]
            return

    # 경로 찾기
    for k in range(4):
        nr, nc = row + di[k], col + dj[k]

        # 범위 안에 있고, 선점되지 않았고, 지난 적 없다면 갈 수 있음
        if in_range(nr, nc) and arr[nr][nc] != 2 and [nr, nc] not in route:
            move(idx, nr, nc, route + [[nr, nc]], dist+1)


#########################################
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# idx 행 : [사람 위치, 편의점 위치]로 구성. 0행은 안쓸거임.
# 초기값을 100으로 하는 이유는 베이스캠프 선정할 때 작은 행열 비교를 위해
loc_info = [[100] * 4 for _ in range(M + 1)]
for idx in range(1, M+1):
    x, y = map(int, input().split())
    loc_info[idx][2], loc_info[idx][3] = x-1, y-1

## 실행
# 모든 사람이 편의점에 도착할 때까지 수행
turn = 1
cnt = 0
while cnt < M:
    change = False
    base_change = []        # 베캠 선점된 경우
    arrive_change = []      # 편의점 선점된 경우

    # 격자 상 모두가 본인 방향을 향해 1칸 움직이기
    for idx, people in enumerate(loc_info):

        # 격자에 들어와있는 사람이라면 백트래킹으로 최단거리 다음 칸을 구해
        if idx != 0 and people[0] != 100:
            my_x, my_y = people[0], people[1]
            store_x, store_y = people[2], people[3]
            min_dist = float('inf')

            to_go = [-1,-1]
            move(idx, my_x, my_y, [[my_x, my_y]], 0)


            # 그러면 to_go에 내가 갈 다음칸이 나와
            # 이걸 내 정보에 일단 업데이트 해
            # 그리고 만약 편의점 도착했다면 ?? 선점해야한다고 표시하고, 사람은 나가
            if to_go[0] == store_x and to_go[1] == store_y:
                change = True
                arrive_change.append(idx)
                people[0], people[1] = 100, 100
            else:
                people[0], people[1] = to_go[0], to_go[1]

    for p in arrive_change:
        get_x, get_y = loc_info[p][2], loc_info[p][3]
        arr[get_x][get_y] = 2
        cnt += 1

    # 베이스캠프에 신입 들어가
    if turn <= M:
        find_my_basecamp(turn)

    # 선점 표시
    for p in base_change:
        get_x, get_y = loc_info[p][0], loc_info[p][1]
        arr[get_x][get_y] = 2

    # 이게 1초
    turn += 1

print(turn-1)