
# ============================
# 첫트에 잘못했던 거: N, M 행열 바꿔씀 ㅡㅡ 진짜 뭐하냐
# 공격 당할 사람 선정할 때 공격자 제외안함 ㅎㅎ..
# 포탑 딱 1개 남았을 때 조기 종료 처리 안함

# ======================='''

# [1] 공격자 기준에 따라 선정 > 공격력 N+M 증가
# 공격력 가장 낮은 포탑 > 가장 최근에 공격한 포탑 > 행+열 합이 가장 큰 포탑 > 열이 가장 큰 포탑

# [2] 공격 대상 기준에 따라 선정 > 1의 반대
# 공격력 가장 높은 > 공격한지 가장 오래된 > 행+열 가장 작은 > 열 가장 작은

# [3-1] 레이저 공격
# 부서진 포탑(공격력 0)은 못 지나감
# 상하좌우로 이동 가능, 가장자리에서 진행하면 반대편으로 나옴
# 방향 우선순위 우하좌상
# 최단 경로로 공격, 경로가 없다면 포탄 공격
# 경로 상에 있는 포탑들도 공격력 절반의 피해

# [3-2] 포탄 공격
# 공격 받은 사람 주위 8개 방향 포탑 모두 절반의 피해
# 가장자리 > 반대편에도 영향

# [4] 포탑 정비
# 공격하지 않고, 공격받지도 않은 포탑 공격력 +1

# 구할 것: 모든 턴 종료 후 남아있는 포탑 중 가장 강한 포탑의 공격력
# ==========================================
from collections import deque

# 범위
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < M

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


# 1. 공격자 선정하기
def choose_attacker():
    # 1) 공격력이 가장 낮은 포탑 (0은 제외)
    min_power = float('inf')
    hubo1 = []

    for r in range(N):
        for c in range(M):
            # 공격력 0은 제외임
            if arr[r][c] == 0:
                continue
            # 공격력 낮은 게 나타나면 후보 리스트 갱신
            if arr[r][c] < min_power:
                hubo1 = [(r, c)]
                min_power = arr[r][c]
            # 같으면 후보 리스트에 추가
            elif arr[r][c] == min_power:
                hubo1.append((r, c))
    # 만약 리스트에 딱 하나만 있으면 여기서 바로 결정
    if len(hubo1) == 1:
        return hubo1[0][0], hubo1[0][1]

    # 2) 후보 여러개면 > 최근에 공격했는지 확인
    hubo2 = []
    recent = 0  # 값이 클 수록 최근에 공격한 것
    for r, c in hubo1:
        # 더 최근에 공격했다면 후보 리스트 갱신
        if attack_time[r][c] > recent:
            recent = attack_time[r][c]
            hubo2 = [(r, c)]
        # 같으면 후보 리스트에 추가
        if attack_time[r][c] == recent:
            hubo2.append((r, c))
    # 1개면 바로 결정
    if len(hubo2) == 1:
        return hubo2[0][0], hubo2[0][1]

    # 3) 후보 여러개면 > 행+열 확인
    hubo3 = []
    max_row_col_sum = -1
    for r, c in hubo2:
        # 더 크면 갱신
        if r + c > max_row_col_sum:
            max_row_col_sum = r + c
            hubo3 = [(r, c)]
        # 같으면 추가
        elif r + c == max_row_col_sum:
            hubo3.append((r, c))
    # 1개면 바로 결정
    if len(hubo3) == 1:
        return hubo3[0][0], hubo3[0][1]

    # 4) 후보 아직도 여러개면 > 열 값 확인
    hubo4 = (0, 0)
    max_col = -1
    for r, c in hubo3:
        # 여기까지 왔으면 열 값 같을 수가 없음 > 가장 큰 값 골라
        if c > max_col:
            max_col = c
            hubo4 = (r, c)
    return hubo4[0], hubo4[1]


# 2. 공격할 포탑 선정하기
def choose_to_kill():
    global attacker_row, attacker_col
    # 1) 공격력이 가장 높은 포탑 (0은 제외)
    max_power = 0
    hubo1 = []

    for r in range(N):
        for c in range(M):
            # 공격력 0은 제외임
            if arr[r][c] == 0:
                continue
            # 하하하 공격자도 제외해야지
            if (r==attacker_row and c==attacker_col):
                continue

            # 공격력 높은 게 나타나면 후보 리스트 갱신
            if arr[r][c] > max_power:
                hubo1 = [(r, c)]
                max_power = arr[r][c]
            # 같으면 후보 리스트에 추가
            elif arr[r][c] == max_power:
                hubo1.append((r, c))
    # 만약 리스트에 딱 하나만 있으면 여기서 바로 결정
    if len(hubo1) == 1:
        return hubo1[0][0], hubo1[0][1]

    # 2) 후보 여러개면 > 오래전에 공격했는지 확인
    hubo2 = []
    recent = float('inf')  # 값이 작을 수록 예전에 공격한 것
    for r, c in hubo1:
        # 더 최근에 공격했다면 후보 리스트 갱신
        if attack_time[r][c] < recent:
            recent = attack_time[r][c]
            hubo2 = [(r, c)]
        # 같으면 후보 리스트에 추가
        if attack_time[r][c] == recent:
            hubo2.append((r, c))
    # 1개면 바로 결정
    if len(hubo2) == 1:
        return hubo2[0][0], hubo2[0][1]

    # 3) 후보 여러개면 > 행+열 확인
    hubo3 = []
    min_row_col_sum = float('inf')
    for r, c in hubo2:
        # 더 작으면 갱신
        if r + c < min_row_col_sum:
            min_row_col_sum = r + c
            hubo3 = [(r, c)]
        # 같으면 추가
        elif r + c == min_row_col_sum:
            hubo3.append((r, c))
    # 1개면 바로 결정
    if len(hubo3) == 1:
        return hubo3[0][0], hubo3[0][1]

    # 4) 후보 아직도 여러개면 > 열 값 확인
    hubo4 = (0, 0)
    min_col = float('inf')
    for r, c in hubo3:
        # 여기까지 왔으면 열 값 같을 수가 없음 > 가장 작은 값 골라
        if c < min_col:
            min_col = c
            hubo4 = (r, c)
    return hubo4[0], hubo4[1]


# 3. 레이저 공격
def laser(sr, sc, er, ec):  # (공격자 좌표, 공격 대상자 좌표)
    Q = deque([(sr,sc)])
    visit[sr][sc] = [100,100]   # 출발지도 아무튼 방문처리를 하긴 해야함
    find = False    # 경로가 존재하는감?

    while Q:
        cr, cc = Q.popleft()

        for k in range(4):
            nr, nc = (cr+di[k])%N, (cc+dj[k])%M

            # 범위 내(사실상 항상 범위 내긴 함), 미방문, 포탑 not 0
            if in_range(nr, nc) and arr[nr][nc] != 0 and visit[nr][nc] == [-1, -1]:

                # 만약 도착했다면 > 종료
                if nr == er and nc == ec:
                    visit[er][ec] = [visit[cr][cc][0], k]
                    find = True
                    return find

                # 만약 첫 출발이라면 > 방향 표시 해주세요
                if visit[cr][cc] == [100,100]:
                    visit[nr][nc] = [k, k]
                # 아니라면 > 내가 따라온 경로 번호 표시 해주세요
                else:
                    visit[nr][nc] = [visit[cr][cc][0], k]
                Q.append((nr, nc))

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

for time in range(1, K+1):
    # [1] 공격자 선정, 공격력 증가
    attacker_row, attacker_col = choose_attacker()
    arr[attacker_row][attacker_col] += (N + M)
    attack_time[attacker_row][attacker_col] = time  # 마지막으로 공격한 시간

    # [2] 공격 대상 선정
    to_kill_row, to_kill_col = choose_to_kill()

    # [3-1] 레이저 공격
    visit = [[[-1,-1] for _ in range(M)] for _ in range(N)]   # (경로 번호, 이전 칸에서 선택한 방향)
    find = laser(attacker_row, attacker_col, to_kill_row, to_kill_col)

    # 만약 경로를 찾았다면 > 바로 피해 입히기
    if find:
        # visit으로 경로 찾고
        er, ec = to_kill_row, to_kill_col
        attack_route = set()  # 공격 경로 넣을거임 (출발지, 목적지 제외)
        while True:
            dir_from = visit[er][ec][1]
            prev_r, prev_c = (er-di[dir_from])%N, (ec-dj[dir_from])%M
            er, ec = prev_r, prev_c

            # 공격 지점이 나오면 끝
            if er == attacker_row and ec == attacker_col:
                break

            # 아니면 루트에 추가하고 계속
            attack_route.add((prev_r, prev_c))

        # 피해 입히기
        arr[to_kill_row][to_kill_col] -= arr[attacker_row][attacker_col]
        for coord in attack_route:
            arr[coord[0]][coord[1]] -= arr[attacker_row][attacker_col]//2


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




