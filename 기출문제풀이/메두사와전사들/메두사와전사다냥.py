
''' 메두사와 전사들 / 20260922

[선정이유]
- 중요한 것은 꺾이지 않는 마음
- 문제의 진행 단계를 함수 단위로 명확하게 분리해 전체 흐름이 깔끔함
- 동일 위치 전사를 개수 단위로 관리해 구현과 연산량을 줄임

[시간 복잡도]
최악의 경우 O(N⁶): 한 턴의 medu_see()가 O(N⁴)이고, 메두사 이동이 최대 O(N²)턴 발생함

[엣지 케이스]
7 10
1 3 5 5
4 4 2 2 3 5 2 5 5 3 1 6 3 6 0 5 4 3 3 2
0 1 1 0 0 0 0
0 1 0 0 1 0 0
1 0 0 0 0 0 0
1 1 0 1 0 0 1
1 0 0 0 1 0 0
0 0 0 0 1 0 0
0 0 0 1 1 0 1

정답:
10 4 3
7 3 2
3 2 3
0 2 0
0 2 0
0
사유: 마주친 전사의 수를 계산 시, 해당 좌표의 모든 전사 수를 더해주지 않고
   1만 더할 경우 잘못된 방향으로 시선처리되어 오답출력


'''

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
