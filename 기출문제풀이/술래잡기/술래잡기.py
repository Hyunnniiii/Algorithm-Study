# 술래는 정중앙에서 시작. NxN에서 정중앙의 인덱스? > N//2
# 도망자 m명. 좌우/상하로 움직인다. 초기) 좌우: 오른쪽, 상하: 아래쪽
# 나무 h개

# 1. 술래와의 거리가 3 이내인 도망자가 "동시에" 움직인다
# 거리 3은 어떻게 처리? > BFS로 거리 3 이내에 존재하는 사람들 구하기?
# 움직인다는 것은??
# - 현재 바라보는 방향으로 갔을 때
# 격자를 벗어나면 > 반대로 전환, 그 반대 방향에 술래 없으면 이동
# 격자 안벗어나면 > 술래 없으면 이동

# 2. 술래가 움직인다
# 달팽이 모양. 초기에 위로 진행. (0,0) 도달하면 다시 반대로
# **이동방향이 틀어지는 지점에 가면, 방향을 바로 틀어준다 > 도망자 파악할 때 중요

# 3. 도망자를 잡는다
# 술래가 현재 위치한 칸을 포함해서 3칸을 본다
# 나무가 놓여있는 칸에 있는 도망자는 못 잡음.
# 잡은 도망자는 사라지고, 점수 계산

# k번 진행. 도망자&술래 모두 끝나야 1번.

# 나무와 도망자가 초기에 겹쳐져 주어질 수 있다 > 그러면 나무랑 술래가 같이 잇으면..?
# 도망자들은 동시에 움직임. 모두 처리하고 다음 단계.
# 한 칸에 여러 도망자가 있을 수 있으므로 입력받을 때 리스트로

# 술래랑 도망자랑 같은 칸이면 그냥 잡는건가? 했는데 그게 아님

# 1. 도망자 여러명 담겨있을 때 따로 담아줘야 하는데 *써서 도망자들 배열이 이상하게 됨.
# 2. 술래가 잡을 때 범위체크 안함
# 3. BFS 1+4+9 = 13번 하면... 않되.
# 4. 오타남. 왜이러니?
# 5. 술래 자리에 도망자가 있을 수 있음. 왜냐면 그 자리에 나무가 있으면.. 진짜 그지같네

# ==========
from collections import deque

## 입력 받기
N, M, H, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]

# 술래의 초기 인덱스, 방향 설정
sulle_r, sulle_c = N//2, N//2
sulle_mode, sulle_dir = 0, 0    # 술래모드: 발산 0, 수렴 1 / 술래의 방향

# 설정: 상우하좌 순서대로 1234를 부여하겠음. 달팽이에도 써먹기 위해
for _ in range(M):
    x, y, d = map(int, input().split())
    if d == 1:    # 초기 방향 오른쪽
        arr[x-1][y-1].append(2)
    elif d == 2:    # 초기 방향 아래쪽
        arr[x-1][y-1].append(3)

# 인덱싱이 편하도록 1번 인덱스부터
di = [-100, -1,0,1,0]
dj = [-100, 0,1,0,-1]

# 나무) 그냥 배열에 표시
tree = [[0]*N for _ in range(N)]
for _ in range(H):
    x, y = map(int, input().split())
    tree[x-1][y-1] = 1

## 필요한 것들 생성
# 범위 체크
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 방향 반대로 바꿔주기
change = [-100, 3,4,1,2]

# 거리 3 이내 BFS 함수
# 진짜 알아냄. 이거 무조건 13번이 아닌가봐. 그리고 술래 자리에 사람 있을 수도 있음
def bfs3(sr, sc):  # 술래의 좌표를 입력한다
    Q = deque([[sr, sc]])

    visit = [[-1] * N for _ in range(N)]
    visit[sr][sc] = 0
    domang = []  # 도망가야하는 사람들 저장

    # 술래의 현 위치에 도망자가 위치하는 경우 처리
    if len(arr[sr][sc]) > 0:
        for domangja in arr[sr][sc]:
            domang.append((sr, sc, domangja))

    while Q:
        sr, sc = Q.popleft()

        for k in range(1, 5):
            nr, nc = sr + di[k], sc + dj[k]

            if in_range(nr, nc) and visit[nr][nc] == -1:
                visit[nr][nc] = visit[sr][sc] + 1
                if 0 <= visit[nr][nc] < 3:
                    Q.append([nr, nc])

                # 도망자가 있으면? > 도망 리스트에 추가
                if len(arr[nr][nc]) > 0:
                    for domangja in arr[nr][nc]:
                        domang.append((nr, nc, domangja))    # 도망자의 위치와 방향 저장
    return domang


# 도망 리스트에 있는 사람들 도망가는 함수
def domangga(domang):
    for cur_r, cur_c, cur_d in domang:

        # 나 일단 무조건 이동할거니까 원래 위치에서는 제거
        arr[cur_r][cur_c].remove(cur_d)

        # 기존 방향대로 했을 때 가능한지 확인: 범위, 술래 있는지
        nxt_r, nxt_c = cur_r + di[cur_d], cur_c + dj[cur_d]

        # 범위 내에 없다면 > 방향 바꿔
        if not in_range(nxt_r, nxt_c):
            cur_d = change[cur_d]
            nxt_r, nxt_c = cur_r + di[cur_d], cur_c + dj[cur_d]

        # 다음 칸에 술래 없으면 진행, 없으면 그 자리에 있을래
        if (sulle_r == nxt_r and sulle_c == nxt_c):
            arr[cur_r][cur_c].append(cur_d)
        else:
            arr[nxt_r][nxt_c].append(cur_d)

# 술래를 달팽이 방향으로 이동하는 함수
# 불편해서 그냥 달팽이용 만듦;; 상우하좌
dal_i = [-1,0,1,0]
dal_j = [0,1,0,-1]
dal_visit = [[0]*N for _ in range(N)]

def dalpeng(sr, sc, sd):  # 술래의 좌표, 방향 입력
    global sulle_mode, dal_visit
    dal_visit[sr][sc] = 1

    if sulle_mode == 0:
        # 시작점은 예외임. 하 진짜 나도 이렇게 짜고 싶지 않은데
        if sr == N // 2 and sc == N // 2:
            nr, nc, sd = sr - 1, sc, 1

        else:
            nr, nc = sr + dal_i[(sd + 1) % 4], sc + dal_j[(sd + 1) % 4]

            if dal_visit[nr][nc] == 0:
                dal_visit[nr][nc] = 1

            else:
                nr, nc = sr + dal_i[sd], sc + dal_j[sd]
                dal_visit[nr][nc] = 1

        # 방향 변경 필요하면 바로 틀어주란다
        nxt_r, nxt_c = nr + dal_i[(sd + 1) % 4], nc + dal_j[(sd + 1) % 4]
        if dal_visit[nxt_r][nxt_c] == 0:
            sd = (sd + 1) % 4

    if sulle_mode == 1:
        nr, nc = sr + dal_i[sd], sc + dal_j[sd]

        if not in_range(nr, nc) or dal_visit[nr][nc] == 1:
            sd = (sd - 1) % 4

        # 아무튼 술래 갔구요. 표시 하겠습니다
        nr, nc = sr + dal_i[sd], sc + dal_j[sd]
        dal_visit[nr][nc] = 1

        # 방향 변경 필요하면 바로 틀어주란다
        nxt_r, nxt_c = nr + dal_i[sd], nc + dal_j[sd]
        if not in_range(nxt_r, nxt_c) or dal_visit[nxt_r][nxt_c] == 1:
            sd = (sd - 1) % 4

    # 만약 시작/끝점에 왔다면 모드 변경 해야함
    if nr == 0 and nc == 0:
        dal_visit = [[0] * N for _ in range(N)]
        sulle_mode = 1
        sd = 2
    elif nr == N // 2 and nc == N // 2:
        dal_visit = [[0] * N for _ in range(N)]
        sulle_mode = 0
        sd = 0

    return nr, nc, sd

# 존나 힘들다 이제 하나 남았다
# 도망자 잡기: 술래의 좌표와 방향을 보고 3칸 내에 도망자가 있는지 확인
# 설마 술래 자리에 있으면?
def final(sulle_r, sulle_c, sulle_dir):
    kill = 0  # 잡은 놈들의 수
    for k in range(3):
        nx, ny = sulle_r + dal_i[sulle_dir] * k, sulle_c + dal_j[sulle_dir] * k

        if in_range(nx, ny) and len(arr[nx][ny]) > 0 and tree[nx][ny] == 0:
            kill += len(arr[nx][ny])
            arr[nx][ny].clear()
    return kill

## 정산!!
ans = 0
for idx in range(1, K+1):
    domang = bfs3(sulle_r, sulle_c)
    domangga(domang)
    sulle_r, sulle_c, sulle_dir = dalpeng(sulle_r, sulle_c, sulle_dir)
    kill = final(sulle_r, sulle_c, sulle_dir)

    ans += idx * kill

print(ans)

