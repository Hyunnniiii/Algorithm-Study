
''' 포탑 부수기 / 20260907 / 체감 난이도 : 골드 4
소요 시간: 127분 / 시도: 2회 / 실행 시간: 279ms (코드트리) / 메모리: 24MB

<선정 이유>
- 막내의 성장 ( >< 푸하하 >< )
- 깔끔한 코드와 실행부, 직관적인 변수명
- 튜플 비교를 활용한 간단한 공격자/공격대상자 선정 과정

<에지 케이스>
5 10 704
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 2186
0 0 0 0 4346 0 0 0 0 0
0 0 0 0 3889 3148 1500 0 0 0
0 3440 0 0 17 0 0 0 0 0

선정 사유: 격자 크기(N*M)를 반영하지 않은 지구별(어린왕자)를 할 경우 오답 출력
정답: 36
오답: 27 ( N*N으로 지구별을 한 경우 )

<시간 복잡도>
O(N * M * K)
N: 행 크기, M: 열 크기, K: 라운드 수

# ======================='''

from collections import deque

# 1. 공격자 선정하기
def choose_attacker():
    hubo = []

    # 0이 아닌 곳에 대해 공격력, 최근 공격일, 행열 합, 열, 좌표 저장
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                hubo.append((arr[r][c], -attack_time[r][c], -(r+c), -c, r, c))

    # 정렬해서 맨 처음에 있는게 공격자
    hubo.sort()
    return hubo[0][4], hubo[0][5]


# 2. 공격할 포탑 선정하기
def choose_to_kill():
    global attacker_row, attacker_col
    hubo = []

    for r in range(N):
        for c in range(M):
            # 공격력 0이거나, 공격자이면 제외
            if arr[r][c] == 0 or (r, c) == (attacker_row, attacker_col):
                continue

            hubo.append((-arr[r][c], attack_time[r][c], r+c, c, r, c))

    # 정렬해서 맨 처음에 있는거 선택
    hubo.sort()
    return hubo[0][4], hubo[0][5]


# 3. 레이저 공격
def laser(sr, sc, er, ec):  # (공격자 좌표, 공격 대상자 좌표)
    Q = deque([(sr,sc, [])])    # (현재 좌표, 지금까지 지나온 경로 리스트)
    visit[sr][sc] = 1

    while Q:
        cr, cc, route = Q.popleft()

        for k in range(4):
            nr, nc = (cr+di[k])%N, (cc+dj[k])%M

            # 범위 내(사실상 항상 범위 내긴 함), 미방문, 포탑 not 0
            if arr[nr][nc] != 0 and visit[nr][nc] == -1:

                # 만약 도착했다면 > 종료
                if nr == er and nc == ec:
                    return True, route

                # 아니라면 > 계속 진행
                else:
                    visit[nr][nc] = 1
                    Q.append((nr, nc, route + [(nr, nc)]))

    # 만약 경로가 없다면 빈 리스트 반환
    return False, []


# 4. 포탄 공격
def bomb(sr, sc, er, ec):   # 공격자, 공격 대상의 좌표 입력
    global attack_route
    for row in range(er-1, er+2):
        for col in range(ec-1, ec+2):
            row, col = row%N, col%M

            # 공격력 0이 아니고, 공격자가 아니면 피해 주기
            if arr[row][col] != 0 and not (row==sr and col==sc):
                # 공격 대상은 따로
                if (row==er and col==ec):
                    arr[row][col] -= arr[sr][sc]
                else:
                    arr[row][col] -= arr[sr][sc]//2
                    attack_route.add((row, col))


# =======================================
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack_time = [[0] * M for _ in range(N)]  # 마지막으로 공격한 시간을 넣을 것

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for time in range(1, K+1):
    # [1] 공격자 선정, 공격력 증가
    attacker_row, attacker_col = choose_attacker()
    arr[attacker_row][attacker_col] += (N + M)
    attack_time[attacker_row][attacker_col] = time  # 마지막으로 공격한 시간

    # [2] 공격 대상 선정
    to_kill_row, to_kill_col = choose_to_kill()

    # [3-1] 레이저 공격
    visit = [[-1]*M for _ in range(N)]   # (경로 번호, 이전 칸에서 선택한 방향)
    find, attack_route = laser(attacker_row, attacker_col, to_kill_row, to_kill_col)

    # 만약 경로를 찾았다면 > 바로 피해 입히기
    if find:
        for coord in attack_route:
            arr[coord[0]][coord[1]] -= arr[attacker_row][attacker_col]//2
        arr[to_kill_row][to_kill_col] -= arr[attacker_row][attacker_col]

    # [3-2] 경로가 없다면 > 포탑 공격으로
    else:
        attack_route = set()   # 공격 경로 (출발지, 목적지 제외)
        bomb(attacker_row, attacker_col, to_kill_row, to_kill_col)

    # [4] 포탑 부서짐, 포탑 정비
    cnt = 0
    for r in range(N):
        for c in range(M):
            # 부서진 포탑 처리
            if arr[r][c] <= 0:
                arr[r][c] = 0
                cnt +=1
                continue

            # 공격과 무관했던 포탑 공격력 1 증가 (공격자와 대상자도 제외)
            if ((r,c) not in attack_route) and not (r==attacker_row and c==attacker_col) and \
                    not (r==to_kill_row and c==to_kill_col):
                arr[r][c] +=1

    # [5] 만약 하나만 남았다면 > 조기 종료
    if cnt == N*M-1:
        break

# 정산
print(max(map(max, arr)))




