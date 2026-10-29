
''' 코드트리빵 / 20260911 / 체감 난이도 : 골드 3
소요 시간: 4시간+ / 시도: 4회 / 실행 시간: 54ms (코드트리) / 메모리: 16MB

[타임라인]
09:00 - 09:34(34분) 문제 읽기 / 입력 받기 / 구상
09:43 - 11:21 (98분) 구현
11:21 - 시간 초과 계속 떠서 백트래킹에 뭔가 잘못된 부분이 있는줄 알고 계속 디버깅하다가 끝남

[구상]
    - 최근 문제에 '동시에' or '순차적'이라는 단어가 나오면 의식적으로 주석에도 적는데, 이 문제의 경우
    충분히 신경 썼음에도 편의점 도착 후 언제부터 지나갈 수 없는지에 대해 결국 착각했다.
    (자세히는 편의점에 도착하면, 편의점으로 한 칸 이동하는 그 턴이 끝난 뒤 바로 못 지나가게 처리를 해야하는데
    나는 해당 턴 모두 끝난 뒤에. 그니까 베이스캠프도 선정한 뒤에 못 지나간다로 해석했다. 틀리고 나서 문제 다시
    읽고 설마 했는데 그거였음)
    - 동은 피드백 받고 자료구조 어떻게 할지, 내가 선언한 변수에 어떤 정보 들어가는지 종이에 적어두고 시작하는데
    확실히 도움된다.

[구현]
- (good)
    - 회수 피드백 > 모든 조건 다 주석에 써놓고 단계별로 구현하기 이거 아주 좋음!!
    코드가 더 깔끔해지고, 확실히 조건을 놓치지 않게 된다
    안되는 조건부터 continue로 처리하고 들어가는거 좋다
    - 너무 함수화에 집착하지 않기로 했다. 함수 밖에서 처리할 수 있는건 밖에서 해야지, 하나의 함수 안에서 모든 것을
    처리하려고 하면 오히려 복잡해진다.
    - 변수명 조금 길더라도 한눈에 알아보기 쉽게 쓰는게 좋다. 최근 변수명 잘못 써서 틀린 뒤로
    예전같으면 px, sx로 썼을 것들을 people_x, store_x 이렇게 길게 쓰기 시작했는데 구현할 때 실수가 적다

- (bad)
    - 이 문제에서 내가 제일 잘못한 점.
    1. 백트래킹 당연히 안되는데 애초에 시도함.
    2^(15*15) 선택지니까 당연히 시간초과가 나겠지? 근데 이러한 기본적인 가능 여부조차 생각치 않고 진입함.
    그리고 너 백트래킹 싫어하면서 왜 완탐인 것 같으면 백트부터 생각해?

    2. 오답노트 불성실하게 수행
    예전에 모노폴리 문제에서 행열 작은 순 우선으로 선택하는 거에서 방향 설정만으로 될거라 생각하고 구현했다가
    실패한 경험이 있는데, 이걸 오늘 문제랑 헷갈림.
    예전에는 행열 작은 순서니까 같은 거리끼리는 다 모아놓고 행열 정렬 해야되는거였고,
    이번 문제는 최단경로 중 방향 우선순위가 있는 것이었기 때문에 애초에 방향만 잘 설정하면 알아서 최초 방문시 우선순위가
    보장되는 거였다.
    근데 예전에 뭔가 안됐던 것 같은 생각이 들어서 BFS 바로 스킵해버림.. 백트 지옥으로 빠졌다.
    이전에 실수한 것은 제대로 정리하고 가야지 안그러면 이런 참사가 일어난다..

[디버깅]
    - 커스텀 프린트를 어서 빨리 활용해보란 말이야..
    - 디버깅을 싫어하지 말자

---------------------------------------------------------
[코드 개선]
1. '동시에' 이동하는거 동은처럼 구현해보기
2. 거리제한 BFS 노션 참고해서 구현해보기

'''
# =======================================================

# ===============
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

# ===================================
import sys
sys.stdin = open('../input.txt', 'r')

from collections import deque

# 범위
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 상좌우하
di = [-1,0,0,1]
dj = [0,-1,1,0]

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
# BFS로..
# [2] 편의점까지 최단거리 구하고 한 칸 이동하시오~~
def move(people_r, people_c, store_r, store_c):   # 초기값: (사람 좌표, 편의점 좌표)
    visit = [[-1]*N for _ in range(N)]

    Q = deque([[people_r, people_c]])
    visit[people_r][people_c] = 100     # 시작점 제외하고는 첫 방향의 인덱스 넣을거임

    while Q:
        r, c = Q.popleft()

        # 편의점에 도착했다면, 첫 방향 뭐였는지 반환해
        if r == store_r and c == store_c:
            return visit[r][c]

        for k in range(4):
            nr, nc = r + di[k], c + dj[k]

            # 범위내, 미방문, 선점된 곳 못 가
            if not in_range(nr, nc) or visit[nr][nc] != -1 or arr[nr][nc] == 2:
                continue

            # 첫 방향이라면 표시
            if r == people_r and c == people_c:
                visit[nr][nc] = k

            # 그 다음부터는 내가 어느 첫 방향으로부터 왔는지 표시
            else:
                visit[nr][nc] = visit[r][c]

            # 아무튼 갔죠? 큐에 더해
            Q.append([nr, nc])


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

        # 격자에 들어와있는 사람이라면 bfs로^^.. 최단거리 다음 칸을 구해
        if idx != 0 and people[0] != 100:
            my_x, my_y = people[0], people[1]
            store_x, store_y = people[2], people[3]

            my_dir = move(my_x, my_y, store_x, store_y)

            # 그러면 내가 갈 다음 방향의 인덱스: my_dir가 나와
            # 이걸 내 정보에 일단 업데이트 해
            # 그리고 만약 편의점 도착했다면 ?? 선점해야한다고 표시하고, 사람은 나가
            if my_x + di[my_dir] == store_x and my_y + dj[my_dir] == store_y:
                change = True
                arrive_change.append(idx)
                people[0], people[1] = 100, 100
            else:
                people[0], people[1] = my_x + di[my_dir], my_y + dj[my_dir]

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