
# ======================
from collections import deque

# 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


# 플레이어 이동
def player_move(idx):
    r, c = player_loc[idx]
    tower_pos = {loc for loc in tower}

    # 이미 포탑에 있는 플레이어는 제외
    if (r,c) in tower_pos:
        return [(r,c)]

    Q = deque()
    Q.append((r,c,[(r,c)]))
    visit = [[0]*N for _ in range(N)]
    visit[r][c] = 1

    while Q:
        sr, sc, route = Q.popleft()

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr, nc) or visit[nr][nc]:
                continue
            if arr[nr][nc] == -1:
                continue

            if (nr,nc) in tower_pos:
                route = route + [(nr, nc)]
                return route

            else:
                Q.append((nr, nc, route + [(nr, nc)]))
                visit[nr][nc] = 1
    return None


# 난투극
def player_fight():
    for row, col in tower:
        if len(brr[row][col]) == 1:
            p = brr[row][col][0]
            team = player_info[p][0]
            arr[row][col] = team

        elif len(brr[row][col]) > 1:
            hubo = []
            for p in brr[row][col]:
                hubo.append((player_info[p][2], p))
            hubo.sort(key = lambda x : -x[0])

            winner = hubo[0][1]
            team = player_info[winner][0]
            arr[row][col] = team
            ans[team] += len(hubo)-1

            for _, p in hubo[1:]:
                r, c = player_loc[p]
                brr[r][c].remove(p)
                player_loc.pop(p)


# 포탑 공격
def tower_attack(tr,tc):
    min_dist = float('inf')
    hubo = []
    tower_pos = set(tower)
    for idx, [pr, pc] in player_loc.items():
        if (pr,pc) in tower_pos:
            continue

        if player_info[idx][0] == arr[tr][tc]:
            continue

        dist = abs(tr-pr) + abs(tc-pc)
        if dist !=0 and dist == min_dist:
            hubo.append((player_info[idx][2], idx))

        elif dist != 0 and dist < min_dist:
            min_dist = dist
            hubo = [(player_info[idx][2], idx)]

    if not hubo:
        return

    hubo.sort(key = lambda x : x[0])
    attack = hubo[0][1]

    ans[arr[tr][tc]] += 10
    return attack


def debug_print(msg):
    if DEBUG:
        print('===', msg, '===')
        print('포탑 상황')
        for row in arr:
            print(row)
        print()
        print('플레이어 위치')
        for row in brr:
            print(row)
        print()
        print('현재까지 점수: ', ans)

#####################################
DEBUG = False
TC = int(input().strip())

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for test_case in range(1, TC+1):

    N, M, K, P, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    brr = [[[] for _ in range(N)] for _ in range(N)]
    tower = []
    for _ in range(M):
        r, c = map(int, input().split())
        arr[r][c] = -2
        tower.append((r, c))

    for row in range(N):
        for col in range(N):
            if arr[row][col] == 1:
                arr[row][col] = -1

    player_info = {}
    player_loc = {}
    for idx in range(1, P + 1):
        t, r, c, s, w = map(int, input().split())
        player_loc[idx] = [r, c]
        player_info[idx] = (t, s, w)
        brr[r][c].append(idx)

    ans = [0] * (K + 1)

    # L턴동안 진행
    for _ in range(L):

        # [1] 플레이어 이동
        for idx in range(1, P+1):
            if idx in player_loc:
                my_route = player_move(idx)

                # 못 간다면 > 그대로 있어
                if my_route is None:
                    continue

                sr, sc = player_loc[idx]
                brr[sr][sc].remove(idx)
                velo = player_info[idx][1]

                if velo >= len(my_route)-1:
                    nr, nc = my_route[-1][0], my_route[-1][1]
                    player_loc[idx] = [nr, nc]
                    brr[nr][nc].append(idx)


                else:
                    nr, nc = my_route[velo]
                    player_loc[idx] = [nr, nc]
                    brr[nr][nc].append(idx)

        debug_print('플레이어 이동 완료')

        # [2] 난투극
        player_fight()

        debug_print('난투극 완료')

        # 확인: player_loc 비었는가
        cnt = 0
        tower_pos = {tuple(loc) for loc in tower}
        for coord in player_loc.values():
            if tuple(coord) not in tower_pos:
                cnt +=1

        if cnt==0:
            break

        # [3] 포탑 공격
        attacked = set()
        for row, col in tower:
            if arr[row][col]>0:
                attack = tower_attack(row, col)

                if attack is not None:
                    attacked.add(attack)

        # 플레이어 한번에 제거
        for p in attacked:
            rr, rc = player_loc[p]
            brr[rr][rc].remove(p)
            player_loc.pop(p)
        debug_print('포탑 공격 완료')

        # 확인: player_loc 비었는가
        cnt = 0
        tower_pos = {tuple(loc) for loc in tower}
        for coord in player_loc.values():
            if tuple(coord) not in tower_pos:
                cnt += 1

        if cnt == 0:
            break

    # 종료 전 처리
    for row, col in tower:
        if arr[row][col] > 0:
            ans[arr[row][col]] += 30

    print(f'#{test_case}', *ans[1:])
