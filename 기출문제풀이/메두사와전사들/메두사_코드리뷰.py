
''' 메두사와 전사들 / 20260922 / 체감 난이도 : 플레
소요 시간: INF / 시도: 4회 / 실행 시간: 455ms (코드트리) / 메모리: 25MB

[타임라인]
녹화 버튼을 안누름 ...............................
09:00 - 09:40(40분 추정) 문제 읽기 / 입력 받기 / 구상
나머지 시간: 구현하다 끝남

[구상]
- 사실 이 문제 너무 악명 높아서 어려울 것이라는걸 알고 있었다. 근데 체감 난이도는 어제 문제보다 높지 않다고 느꼈다.
다만 구현량이 너무 많을 뿐...

- 요즘 로직 자체를 잘못 생각하는 경우가 너무 많아서 정말 상세히 구상하려고 노력했다.
Ideation 작성, 주석으로 단계 및 함수 모두 작성 후 시작헀다.
그래서 그런건지, 엣지가 별로 없었어서 그런건진 모르겠지만 잘못된 로직으로 고생하진 않았다.

- 내가 꼬였는지 문제가 애매하다고 느꼈다. 이동을 동시에 하는지 순서대로 하는지
왜 안알려주지? 라고 생각했고 그거에 대해 고민을 가장 많이 했다. 결론적으로는 상관이 없었다 ㅎㅎ..


[구현]
- 난 진짜 하드코딩 할 때마다 인덱스나 range 실수가 무조건 나오는듯.
복붙해서 그런 걸지도.. 오늘은 심지어 눈에 힘주고 코드 썼는데 이래됨
다만 내가 최근 그런 실수를 많이 해서 바로 이 부분을 의심하긴 했다. 찾기 힘들어서 그렇지..

- 처음에 자료구조를 3차원 배열에다가 전사(2), 돌전사(3) 중복이어도 전부 집어넣는 식으로 구상을 했는데,
구현을 하다보니 갑자기 팩맨 문제가 떠오르는 바람에..
(팩맨: 알까기 해서 몬스터 수가 거듭제곱으로 늘어남 > 시간초과 issue 있었음)

[(돌인지 여부, 사람 수)]를 매 칸에 표시하는 방법으로 바꿨다.
근데 쉬면서 생각해보니 전사들이 알까기 하는 것도 아니고 그럴 필요가 전혀 없었는데.. 이미 너무 많이 구현을 해놨기도 하고,
내가 하고 있는 방식이 막 잘못되거나 알아보기 극악이었던 것도 아니라 그냥 바꾼 채로 계속 구현했다. (시간이 없기도 했음)

- 아 진짜 인덱스랑 range 실수 너무 싫다


[디버깅]
- 코드가 너무 길어서 정말 디버깅하기 쉽지 않았다.
- 함수 단위 테스트도 직접 배열 만들고 케이스 만드는 게 생각보다 오래 걸려서 정말 쉽지 않았다
- 요즘 디버그 프린트 해보려고 하는데, 그동안 print만 해왔어서 정말 ... 디버그 프린트 함수 만드는 시간 vs print 작성하는
시간 효용을 잘 모르겠다,,, 다만 반복적으로 하나의 배열만 확인해야 하는 문제에서 써보려고 시동 거는중


[첫 제출 때 놓친 것들]
1. max_rock 초기값을 0으로 설정해서 무조건 갱신되지 않고 있었음 > 런타임 오류
2. 시야 계산 인덱싱 오류 무려 3개
3. 전사 이동할 때 배열 처리 중복
(자세히는, 첫번째 이동만 가능한 경우/두번째 이동까지 가능한 경우에 대해 처리를 잘 해줘야 하는데
두가지 케이스를 잘 구분하지 않았음)

---------------------------------------------------------
[개선]
메두사 시야 처리 간략화 (최대한 인덱싱을 덜 하는 쪽으로)

'''
# NxN 마을. 도로 0, 도로 아니면 1
# 메두사 집 > 공원까지 산책. 도로만을 따라 최단 경로로
# 메두사의 집과 공원은 항상 도로 위에
# 전사는 메두사를 잡는다
# 도로/비도로 구분 없이 메두사를 향해 최단 경로로 이동
# 초기에 전사가 메두사의 집에 있는 경우는 없다
# 메두사는 전사들이 움직이기 전에 그들을 바라봐서 돌로 만든다

# 최단 거리 = 맨해튼 거리

# [1] 메두사 이동
# 도로를 따라 한 칸 이동, 공원까지 최단 경로로
# 이동한 칸에 전사가 있을 때 전사 사망
# 여러 최단 경로가 가능하다면 상하좌우 우선순위
# 집 > 공원까지 경로가 없을 수도 있다

# [2] 메두사 시선
# 상하좌우 중 전사를 가장 많이 볼 수 있는 방향을 바라본다
# 여러 명이라면 상하좌우 우선순위
# 바라보는 방향으로 90도의 시야각 범위 안에 있는 전사들을 볼 수 있다
# 다른 전사에게 가려진 경우 보이지 않는다
# 메두사가 본 전사들은 돌로 변해서 해당 턴까지 움직일 수 없다

# [3] 전사 이동
# 돌로 변하지 않은 전사 메두사를 향해 2칸 이동
# 상하좌우 > 좌우상하 우선순위
# 메두사의 시야에 들어오는 곳으론 이동할 수 없다

# [4] 전사 공격
# 메두사와 같은 칸이면 공격하지만 전사 사망

# 구할 것: 매 턴마다 모든 전사가 이동한 거리의 합 / 메두사로 인해 돌이 된 전사의 수 /
#       메두사를 공격한 전사의 수

# 첫 번째 이동한 곳도 메두사가 보면 안되는 곳
# 그러면 다른 전사에게 가려져 있는 상태라면?
# 다른 전사한테 가려져서 갈 수 있었는데. 그 전사가 움직여서 보이게 되면 어캄
# > 이건 안되는게 가린 애는 이미 돌 됨
# 이동해도 가려지는 곳이 없으면?
# 전사 이동 동시에 하는건가?
# 경로가 없을 수 있는데 어떻게 종료? > 전사가 다 사망? or -1 출력
# 전사 사망은 따로 처리할 필요 X

# 가정 1. 2번 시점을 기준으로 갈 수 있는 곳만 간다
# 가정 2. 전사는 본인이 이동했을 때만 공격한다
# 가정 3. 전사들은 동시에 움직인다
# 가정 4. 주변에 가까워지면서 가려진 곳이 없으면 움직이지 않는다
# 종료 조건: 경로X, 메두사 도착
# =============================
from collections import deque

# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

# [1] 메두사 이동
def medu_move(mr,mc,pr,pc):
    Q = deque([[mr,mc]])
    visit = [[-1]*N for _ in range(N)]
    visit[mr][mc] = -2

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr+dr[k], sc+dc[k]

            # 범위, 미방문 확인
            if not in_range(nr,nc) or visit[nr][nc]!=-1:
                continue
            # 길이어야 갈 수 있음
            if arr[nr][nc]==1:
                continue

            # 다음칸 집이면 > 방향 리턴
            if nr==pr and nc==pc:
                return visit[sr][sc]  # 갈 수 있음, 다음으로 갈 방향

            # 처음 가는거면 > 첫 방향 기록
            if visit[sr][sc]==-2:
                Q.append([nr,nc])
                visit[nr][nc] = k
            # 아니면 > 기존 방향 기록
            else:
                Q.append([nr,nc])
                visit[nr][nc] = visit[sr][sc]
    return -1

# [2] 메두사 시선
def medu_see(mr, mc):
    # 최종 선택할 버전
    max_rock = -1
    real_rock_lst = []
    real_medu_eye = None

    # 4개 방향에 대해 진행
    for d in range(4):
        rock = 0    # 이번 방향에서 돌로 변한 전사 수의 최댓값
        rock_lst = []   # 돌로 변한 전사들의 좌표 모음
        dist = 1    # 메두사로부터 몇 칸 떨어졌는지
        sr, sc = mr, mc
        medu_eye = [[0] * N for _ in range(N)]  # 메두사의 시야 표시 (보이면 1, 안보이면 0)
        # 1. 위/아래로 볼 때
        if d==0 or d==1:
            # 배열 끝에 갈 때까지 반복
            while True:
                nr = sr + dr[d]

                # 범위 넘어가면 끝
                if not 0<=nr<N:
                    break
                for col in range(max(0,sc-dist), min(N, sc+dist+1)):
                    medu_eye[nr][col] = 1
                sr = nr
                dist += 1

            # 돌전사 찾기
            for r in range(N):
                for c in range(N):
                    # 모두 돌전사로 만들고, +돌전사 수
                    if medu_eye[r][c]==1 and brr[r][c][0][1] > 0:
                        # 내 뒤로 다 살려
                        junsa_hide(medu_r, medu_c, r, c, d, medu_eye)

            # 다 하면 전사 수 세기
            for r in range(N):
                for c in range(N):
                    if medu_eye[r][c] ==1 and brr[r][c][0][1]>0:
                        rock += brr[r][c][0][1]
                        rock_lst.append((r,c, brr[r][c][0][1]))


        # 2. 왼/오로 볼 때
        if d==2 or d==3:
            # 배열 끝에 갈 때까지 반복
            while True:
                nc = sc + dc[d]

                # 범위 넘어가면 끝
                if not 0<=nc<N:
                    break
                for row in range(max(0, sr-dist), min(N, sr+dist+1)):
                    medu_eye[row][nc] = 1
                sc = nc
                dist += 1

            # 돌전사 찾기
            for r in range(N):
                for c in range(N):
                    if medu_eye[r][c] == 1 and brr[r][c][0][1]>0:
                        # 내 뒤로 다 살려
                        junsa_hide(medu_r, medu_c, r, c, d, medu_eye)

            # 다 하면 전사 수 세기
            for r in range(N):
                for c in range(N):
                    if medu_eye[r][c] ==1 and brr[r][c][0][1]>0:
                        rock += brr[r][c][0][1]
                        rock_lst.append((r,c, brr[r][c][0][1]))
        # 정산
        if rock > max_rock:
            max_rock = rock
            real_rock_lst = rock_lst
            real_medu_eye = medu_eye

    return max_rock, real_rock_lst, real_medu_eye


# 전사와 메두사의 위치에 따라 가려지는 곳 배열에 표시
def junsa_hide(mr, mc, jr, jc, d, medu_eye):
    # 위 / 아래
    if d == 0 or d == 1:
        dist = 1
        sr, sc = jr, jc
        if sc < mc:
            while True:
                nr = sr + dr[d]
                # 범위 넘어가면 끝
                if not 0 <= nr < N:
                    break
                for col in range(max(0, sc - dist), sc + 1):
                    medu_eye[nr][col] = 0
                sr = nr
                dist += 1
        elif sc == mc:
            if d == 0:
                for row in range(sr-1, -1, -1):
                    medu_eye[row][sc] = 0
            elif d == 1:
                for row in range(sr+1, N):
                    medu_eye[row][sc] = 0
        elif sc > mc:
            while True:
                nr = sr + dr[d]
                # 범위 넘어가면 끝
                if not 0 <= nr < N:
                    break
                for col in range(sc, min(N, sc + dist + 1)):
                    medu_eye[nr][col] = 0
                sr = nr
                dist += 1

    # 왼/오
    if d == 2 or d == 3:
        dist = 1
        sr, sc = jr, jc
        if sr < mr:
            while True:
                nc = sc + dc[d]
                # 범위 넘어가면 끝
                if not 0 <= nc < N:
                    break
                for row in range(sr, max(-1, sr - dist - 1), -1):
                    medu_eye[row][nc] = 0
                sc = nc
                dist += 1
        elif sr == mr:
            if d == 2:
                for col in range(sc-1, -1, -1):
                    medu_eye[sr][col] = 0
            elif d == 3:
                for col in range(sc+1, N):
                    medu_eye[sr][col] = 0

        elif sr > mr:
            while True:
                nc = sc + dc[d]
                # 범위 넘어가면 끝
                if not 0 <= nc < N:
                    break
                for row in range(sr, min(N, sr + dist + 1)):
                    medu_eye[row][nc] = 0
                sc = nc
                dist += 1


# [3] 전사 이동
def junsa_move_and_attack(mr,mc):
    global tot_move
    to_move = []
    for r in range(N):
        for c in range(N):
            # 돌이 아닌 전사가 있다면
            if brr[r][c][0][1]>0:
                cur_dist1 = abs(mr-r)+abs(mc-c)
                first_move = -1

                # 첫 번째 이동
                for k in range(4):

                    nr, nc = r+dr[k], c+dc[k]
                    dist = abs(mr-nr)+abs(mc-nc)
                    # 범위 내, no 시야
                    if not in_range(nr,nc) or medu_eye[nr][nc]==1:
                        continue
                    # 거리 줄었는지
                    if dist >= cur_dist1:
                        continue
                    # 정산
                    cur_dist1 = dist
                    first_move = k

                # 이동할 수 있으면 > 반영
                if first_move == -1:
                    continue
                move = brr[r][c][0][1]
                tot_move += move
                brr[r][c][0][1] -= move

                # 두 번째 이동 > 안되면 첫 이동으로 해야 함
                cur_dist2 = cur_dist1
                second_move = -1

                for k in range(4):
                    nnr, nnc = r+dr[first_move]+ ddr[k], c+dc[first_move]+ddc[k]
                    dist = abs(mr - nnr) + abs(mc - nnc)
                    # 범위 내, no 시야
                    if not in_range(nnr, nnc) or medu_eye[nnr][nnc] == 1:
                        continue
                    # 거리 줄었는지
                    if dist >= cur_dist2:
                        continue
                    # 정산
                    cur_dist2 = dist
                    second_move = k

                # 이동할 수 있으면 > 반영
                if second_move == -1:
                    to_move.append((r + dr[first_move], c + dc[first_move], move))  # 두번째 못가면 첫번째로 가면 된다롱
                    continue

                tot_move += move    # 나 또 이동해요
                to_move.append((r+dr[first_move]+ddr[second_move], c+dc[first_move]+ddc[second_move], move))  # 두번째로 갈래롱

    # 다 처리했으면 to_move에 있는 애들에다가 이동 처리
    for row, col, cnt in to_move:
        brr[row][col][0][1] += cnt


#########################
N, M = map(int, input().split())
home_r, home_c, park_r, park_c = map(int, input().split())
medu_r, medu_c = home_r, home_c     # 메두사 위치 정보

junsa = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]   # 도로 정보
brr = [[[[2,0], [3,0]] for _ in range(N)] for _ in range(N)]    # 전사2, 돌전사3 표시

# 전사 2, 돌전사 3
for i in range(M):
    x, y = junsa[2*i], junsa[2*i+1]
    brr[x][y][0][1] += 1

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 좌우상하
ddr = [0,0,-1,1]
ddc = [-1,1,0,0]

## 실행
while True:
    # [0] 각 턴에서 반환할 결과
    tot_move, rock_cnt, attack_cnt = 0, 0, 0

    # [1] 메두사 이동
    d = medu_move(medu_r, medu_c, park_r, park_c)

    if d == -2:
        print(0)
        break

    # 경로가 없으면 > ans = -1, 종료
    if d == -1:
        print(-1)
        break

    # 리턴받은 d에 따라 메두사 이동하기
    medu_r += dr[d]
    medu_c += dc[d]

    # 구한 곳으로 이동했는데 전사가 있으면 > 그 전사 죽이기
    if brr[medu_r][medu_c][0][1] > 0 or brr[medu_r][medu_c][1][1] > 0:
        brr[medu_r][medu_c] = [[2,0], [3,0]]

    # [2] 메두사 시선
    rock, rock_lst, medu_eye = medu_see(medu_r, medu_c)
    if rock > 0:
        rock_cnt += rock
        for r, c, l in rock_lst:
            brr[r][c][1][1] += l
            brr[r][c][0][1] -= l

    # [3] 전사 이동
    junsa_move_and_attack(medu_r, medu_c)

    # [4] 전사 공격
    if brr[medu_r][medu_c][0][1] > 0:
        attack_cnt += brr[medu_r][medu_c][0][1]
        brr[medu_r][medu_c][0][1] = 0

    # [5] 돌전사 해방
    for r in range(N):
        for c in range(N):
            if brr[r][c][1][1] > 0:
                brr[r][c][0][1] += brr[r][c][1][1]
                brr[r][c][1][1] = 0

    # [6] 프린트
    print(tot_move, rock_cnt, attack_cnt)