
# ======================================================
# [코드 개선]
# 1. find 함수 너무 복잡함. 나누는게 더 깔끔할지도
# ㄴ> 묶음 찾는 함수 / 우선순위 따지는 함수 로 분리해보겠음
# 2. 중력 함수 다른 방식 없을까? 끝부분 처리가 좀.. 맘에 안듦
# 3. 우선순위 비교 이상함

## 가즈아
from collections import deque

## 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

## 필요한 요소들 생성
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 범위 체크
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N


## 함수 생성
# 1. 묶음을 찾는 함수.
# 입력된 시작점에서 이루어지는 그룹의 기준점을 반환한다
def find(sr, sc, visit):
    my_color = arr[sr][sc]

    Q = deque([(sr, sc)])
    visit[sr][sc] = True

    normal = [(sr, sc)]  # 빨강이 아닌 폭탄 좌표 저장
    red = []  # 빨강 좌표 저장
    red_visit = set()  # 빨간색은 여러 그룹에 소속될 수 있으므로 따로 방문 처리

    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr, nc = r + di[k], c + dj[k]

            # 범위 체크 먼저
            if not in_range(nr, nc):
                continue

            # 빨간색일 때 처리
            # 이미 방문했던 빨간색이면 제외
            if arr[nr][nc] == 0:
                if (nr, nc) in red_visit:
                    continue

                red_visit.add((nr, nc))
                red.append((nr, nc))
                Q.append((nr, nc))

            # 같은 색상일 때 처리
            elif arr[nr][nc] == my_color and not visit[nr][nc]:
                normal.append((nr, nc))
                visit[nr][nc] = True
                Q.append((nr, nc))

    # 전체 그룹 좌표
    group = normal + red

    # 기준점 찾기: 행이 큰 것, 열이 작은 것을 뽑는다
    # 행은 그대로, 열은 음수로 바꾸면 max니까 알아서 행 큰거, 열 작은 순으로 선택됨
    real_r, real_c = max(normal, key=lambda x: (x[0], -x[1]))

    return group, real_r, real_c, len(red)


# 2. 전체 배열에서 우선순위 가장 높은 그룹 찾고, 반환
def best():
    visit = [[False] * N for _ in range(N)]

    best_group = None
    best_key = None

    for row in range(N):
        for col in range(N):

            # 일반 폭탄에서만 시작. 빨강만 있는 집단 안되므로
            if arr[row][col] <= 0 or visit[row][col]:
                continue

            # 위의 경우가 아니면 그룹 찾기 수행
            group, real_r, real_c, red_cnt = find(row, col, visit)

            # 그룹 크기가 2개보다 적으면 안됨
            if len(group) < 2:
                continue

            # 우선순위: 그룹 크기, 빨간 폭탄, 행, 열
            key = (len(group), -red_cnt, real_r, -real_c)
            if best_key is None or key > best_key:
                best_key = key
                best_group = group

    return best_group


# 3. 중력 함수
# 아래에서 위로 보면서 폭탄을 발견하는 즉시 가능한 가장 아래로 옮겨준다
# 돌을 만나면 내릴 곳 위치 인덱스를 (돌-1)로 변경
# 폭탄 만나면 내릴 곳 인덱스에 폭탄 넣어주고 인덱스는 (내릴 곳 -1) 해주면 됨
def gravity():
    for c in range(N):
        put = N - 1  # 마지막 행부터 쌓는다

        for r in range(N - 1, -1, -1):
            if arr[r][c] == -1:
                put = r - 1

            elif arr[r][c] != -7:

                # 폭탄을 넣을 곳이 본인 자리가 아니면 바꿔준다
                if r != put:
                    arr[put][c] = arr[r][c]
                    arr[r][c] = -7

                # 내려놓을 위치 변경
                put -= 1


# 4. 반시계 회전하기
def rotation():
    global arr

    new_arr = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_arr[row][col] = arr[col][N - 1 - row]

    arr = new_arr


## 실행
ans = 0
while True:
    group = best()

    # 더이상 그룹이 없으면 끝
    if group is None:
        break

    # 그룹 있으면 점수 계산, 폭탄 제거
    ans += len(group) ** 2
    for x, y in group:
        arr[x][y] = -7

    gravity()
    rotation()
    gravity()

print(ans)
