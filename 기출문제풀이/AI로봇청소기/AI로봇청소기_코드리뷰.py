
''' AI 로봇청소기 / 20260930 / 체감 난이도 : 골드 5
소요 시간: 2시간 42분 / 시도: 3회 / 실행 시간: 168ms (코드트리) / 메모리: 23MB

[타임라인]
09:00 - 09:32(32분) 문제 읽기 / 입력 받기 / 구상
09:32 - 10:20(48분) 구현
10:20 - 11:00(40분) 검증 (같이 제출하기로 했음)
11:04 - 11:25(21분) 수정, 2차 제출 > 실패
11:25 - 11:42(17분) 수정, 3차 제출 > 성공


[구상]
- 애매하다고 생각되는게 좀 많았다.
1. 순서대로 이동 > 무슨 순서??
2. 이동거리 가까운 오염 격자로 이동 > 이동하는 과정동안은 아무 일도 안일어나나?
    로봇끼리 경로 겹친다거나, 지나가는 경로는 다 청소한다거나.. >> 이건 그냥 내가 너무 많이 생각한거임
3. 갈 수 있는 곳이 없으면? > 어떻게 해야하는지 안나와있었음

- 그럼에도.. 문제를 읽는데 음 아는 맛 > 아는 맛 > 아는 맛이어서
  방심하지 말아야겠다고 생각했다

- 내 방향 기준 엿 모양(?)을 어떻게 구현할지 조금 고민했는데, 냉방 시스템에서 했던 것처럼
방향 인덱스 잘 활용하면 되겠다 라고 생각하고 들어갔다.

[구현]
- 구현은 쉽게 했다. 최대한 묘수 안쓰고 정직하게 구현 가능한 부분은 그대로 하려고 했다.
- 최단거리 bfs도 나름 오랜만에 해서.. 함수 작성하고 나서 제대로 돌아가는지 케이스 만들어서
  직접 돌려가면서 확인했다

* 첫 구현에서 빼먹었던 점
: bfs 시작점 처리. 내 자리에 먼지가 남아있는 경우 거리 0으로 제자리 처리를 안함
진짜 bfs 시작점 맨날 당하는데 좀 기억해라 >> 체크리스트에 추가

- 첫 제출 > 실패 (시간초과)
3번 테케를 바로 틀렸는데, 디버깅 프린트 찍어보니까 너무 대형 테케라서..
정답 비교해보니 값은 다 맞았고, 검증도 나름 40분 동안 해서 코드에 문제는 없을 것 같았고
내가 방만하게 한 부분이 문제일거라 생각했다

-첫 의심: min/max 너무 자주 썼나? -> time 찍어보니까 아니었음
-두번째 의심: 대왕 태케 디버깅 프린트로 찍어서 대충 보는데, 이미 다 빈 배열에 로봇청소기가 제자리에
그대로 남아있는 똑같은 상태 그대로 몇백회 반복되는 걸 확인했다. 그래서 알아챘다.. 조기 종료 처리를
해줘야 하는구나..
> 그래서 처음에는 bfs 이전/이후 로봇 좌표 변했는지 확인하는 식으로 했더니,
제자리에 먼지가 있어서 안움직이는 경우까지 못 가는걸로 판별해버려서 2차 제출 때 틀렸다

> 제대로 수정해서 통과하긴 했는데,
조금 공부하다보니 딕셔너리 value에다가 in 때린게 문제였다.


[검증]
- 최소 케이스, 로봇이 못 가는 경우 전부 다 확인했다
- 하다하다 시간도 확인했었는데.. 대형 테케로 돌려보지 않아서 시간 초과에 대한 생각이 많이 없었다
- 그리고 어제는 나름 효율 추구한다고 묘수 썼다가 얻어맞아서 방만(=정직?)하게 한 것도 있는데, 바로
이렇게 당할 줄이야 ㅎㅎ..


[후기]
- 안하던 짓 하지 말자. 지금까지 단 한번도 딕셔너리 value에 in 쓴 적 없는데 썼다가 바로 문제가..
- 틀려도 당황하지 말고 침착하기.. 제일 중요한듯
- ㅎㅎ.. 단 한 문제도 편히 넘어가는 법이 없지 ^^ 오히려 좋아~~ 시험 전에 다 당해버려 그냥

---------------------------------------------------------
[개선]
방향 처리하는거 그냥 내 반대방향은 안보는걸로 하면 정말 편함

'''

# 구할 것: 각 테스트마다 공간에 있는 총 먼지의 합

# 청소기 순서대로 > 뭔 순서? > 입력 순서인감
# 청소기는 한번에 제일 인접한 먼지칸으로 간다. 그 경로는 청소 안하는걸로
# 청소기가 물건에 가로막히거나 더이상 청소할 곳이 없으면 어캄? > 일단 가만 있는걸로 간주
# 설마. 물건 자리에 청소기 주어지는건 아니겠지?
# ================================================
from collections import deque


# 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


# [1] 청소기 이동
def robot_bfs(idx):
    global stay
    sr, sc = robot[idx]

    # 만약 내 자리에 먼지가 남아있다면 > 그냥 거기 있으삼
    if arr[sr][sc] > 0:
        return

    Q = deque()
    Q.append((sr,sc))
    visit = [[-1] * N for _ in range(N)]
    visit[sr][sc] = 0
    hubo = []
    dist = float('inf')
    robot_pos = {tuple(coord) for coord in robot.values()}

    while Q:
        r, c = Q.popleft()

        # 만약 먼지 거리보다 큰 거리가 나오면 > 끝
        if visit[r][c] >= dist:
            break

        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]

            if not in_range(nr,nc) or visit[nr][nc] != -1:
                continue
            if arr[nr][nc] == -1 or (nr, nc) in robot_pos:
                continue

            # 먼지 있으면 > 이 거리까지만
            if arr[nr][nc] > 0:
                dist = visit[r][c] + 1
                visit[nr][nc] = visit[r][c] + 1
                hubo.append((nr,nc))

            # 빈칸이면 > 그냥 추가
            elif arr[nr][nc] == 0:
                Q.append((nr,nc))
                visit[nr][nc] = visit[r][c] + 1

    # 갈 수 있는 곳이 없으면 움직이지 않는다고 간주
    if not hubo:
        return

    # 후보 다 나왔으면 정렬 후 고르기
    hubo.sort(key = lambda x : (x[0], x[1]))
    robot[idx] = [hubo[0][0], hubo[0][1]]


# [2] 청소
def robot_clean(idx):
    r, c = robot[idx]
    max_clean = -1
    max_clean_dir = None

    for k in range(4):
        clean = min(20, arr[r][c])
        nr1, nc1 = r+dr[k], c+dc[k]
        nr2, nc2 = r+dr[(k-1)%4], c+dc[(k-1)%4]
        nr3, nc3 = r+dr[(k+1)%4], c+dc[(k+1)%4]

        if in_range(nr1, nc1) and arr[nr1][nc1]!=-1:
            clean += min(20, arr[nr1][nc1])
        if in_range(nr2, nc2) and arr[nr2][nc2] != -1:
            clean += min(20, arr[nr2][nc2])
        if in_range(nr3, nc3) and arr[nr3][nc3] != -1:
            clean += min(20, arr[nr3][nc3])

        if clean > max_clean:
            max_clean = clean
            max_clean_dir = k

    # 방향 확정 안되면 > 못 치우는건데 이런 경우가 있나?
    if max_clean_dir is None:
        return

    # 이제 k 방향이라고 확정됐으니까 배열에서 먼지 치우기
    nr1, nc1 = r + dr[max_clean_dir], c + dc[max_clean_dir]
    nr2, nc2 = r + dr[(max_clean_dir - 1) % 4], c + dc[(max_clean_dir - 1) % 4]
    nr3, nc3 = r + dr[(max_clean_dir + 1) % 4], c + dc[(max_clean_dir + 1) % 4]

    arr[r][c] = max(arr[r][c]-20, 0)
    if in_range(nr1, nc1) and arr[nr1][nc1] != -1:
        arr[nr1][nc1] = max(arr[nr1][nc1]-20, 0)
    if in_range(nr2, nc2) and arr[nr2][nc2] != -1:
        arr[nr2][nc2] = max(arr[nr2][nc2] - 20, 0)
    if in_range(nr3, nc3) and arr[nr3][nc3] != -1:
        arr[nr3][nc3] = max(arr[nr3][nc3] - 20, 0)


# [3] 먼지 확산
def hwaksan():
    imsi = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] > 0 or arr[r][c]==-1:
                continue

            munji_sum = 0
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]

                if not in_range(nr,nc) or arr[nr][nc] == -1:
                    continue
                munji_sum += arr[nr][nc]

            imsi[r][c] += munji_sum//10

    for r in range(N):
        for c in range(N):
            arr[r][c] += imsi[r][c]

def debug_print(word):
    if DEBUG:
        print(word)
        print('현재 먼지 상황')
        for row in arr:
            print(row)
        print()
        print('현재 로봇청소기 현황')
        print(robot)

########################
DEBUG = False
N, K, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
robot = {}
for idx in range(1, K+1):
    robot[idx] = list(map(lambda x : int(x)-1, input().split()))

# 우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 물건 개수 세기
mat = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == -1:
            mat += 1

# T턴 동안 진행
for _ in range(T):

    # [1] 청소기 이동
    for idx in range(1, K+1):
        robot_bfs(idx)

    debug_print('청소기 이동 완료')

    # [2] 청소
    for idx in range(1, K+1):
        robot_clean(idx)

    debug_print('청소 진행 완료')

    # [3] 먼지 축적
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 0:
                arr[row][col] += 5

    debug_print('먼지 축적')

    # [4] 먼지 확산
    hwaksan()

    debug_print('먼지 확산 완료')

    # [5] 출력
    print(sum(map(sum, arr)) + mat)
