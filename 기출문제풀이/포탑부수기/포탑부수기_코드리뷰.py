
''' 포탑 부수기 / 20260907 / 체감 난이도 : 골드 4
소요 시간: 127분 / 시도: 2회 / 실행 시간: 279ms (코드트리) / 메모리: 24MB

[타임라인]
09:00 - 09:20(20분) 문제 읽기 / 입력 받기 / 구상
09:20 - 10:48 (88분) 구현하면서 함수 단위로 세부적인 구상, 제출
10:48 - 11:00 (12분) 디버깅을 위한 print 작성 및 추적
11:00 - 11:07 강제 휴식 타임
11:07 - 11:14 (7분) 디버깅 및 코드 수정, 제출

[구상]
- (good)
    - 어제 지피띠니랑 상담했을 때 구상 단계에서 다 정하지 못하겠으면 구현할 때 함수 단위로
    입력값, 초기 상태, 함수 처리 후 상태, 아웃풋의 자료 형태 정도 정하고 들어가래서 말 잘 들었다.
    확실히 더 세부적인 구상이 가능했고, 자료형 정할 때도 지금까지는 구상과 구현이 다를 때가 많았는데
    그 차이가 많이 줄었다. 굳
    - 동은의 빨간펜 따라해봤는데 중간에 잊어버릴 만한 것들 다시 리마인드 된다는 점에서 좋았다. 음..
    근데 그렇게 해도 까먹음.. (<- 공격자는 공격 대상 선정에서 제외) 난 진짜 뭘까??
    - visit에 경로 어디서부터 왔는지 처리하는거 좀 아이디어 좋았다고 생각함 ㅎㅎ 근데 이제
    다른 사람들 코드도 봐야지.. 더 좋은 방법이 무조건 있을 것

[구현]
- (good)
    - 주석에 뭐 해야하는지 써놓고 구현하는거 나랑 잘 맞는 듯 하다. 킹회수
- (bad)
    - N행 M열인데 무려 두 군데에서 M행 N열로 처리하는 코드를 작성함.
    근데 이건 정신을 그냥 차리는 수밖엔..

[디버깅]
    - 음.. 내가 틀린 테케에서 내가 한 실수가 잘 보여서 빠르게 고칠 수 있었다고 생각한다.
    - 사실 제출하고 나서 좀만 더 하면 진짜 될 것 같아서 엄청나게 디버깅에 몰두(?)하고 있었는데 오히려
    중간에 강제로 7분 리프레시 하니까 내가 뭘 잘못했을지 떠올랐다.
    앞으로는 첫 제출하고 틀리면 반드시 휴식 시간을 가지도록

[후기]
    - 정신을 똑디 차리고 구현합시다. 구현 시간이 길어서 중간에 나도 모르게 이상한 짓을 하나씩 한다..

---------------------------------------------------------
[개선]
- 일단 후보 고르는 함수 한번에 할 수 있을 것 같음.
- 후보 고를 때 튜플 비교 & sort 활용..
- BFS 방향 우선순위 & 경로 찾는거 분명 방법이 있을 것 >> 동은 코드 공부


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

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


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




