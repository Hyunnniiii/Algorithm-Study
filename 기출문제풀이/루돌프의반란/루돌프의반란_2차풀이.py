
""" 루돌프의 반란 / 20261006 냐호 / 체감 난이도: 골드 3
소요 시간 약 2시간 / 시도 2회 / 실행 시간 108ms (코드트리) / 메모리 19MB (코드트리)

방향은 주의해서 잘 처리했는데 연쇄작용에서 뇌절 와서 변수 헷갈려서 틀림
이거 처음 풀었을 때 함수화 잘해서 좋아했었는데, 지금 보니 함수화 깔끔하게 한다고 장떙이 아니다옹

루돌프나 산타 이동 방향 처리하는 거에서 짬빠?가 느껴짐
산타 현재 좌표와 기절 상태를 한번에 저장하지 않은 것 칭찬해
근데 연쇄작용을 틀려놨는데 10번 테케까지 틀린게 없는건 좀 너무한거 아닌가

굿바이 산타 앤드 루돌프

"""

# 11:00 ~
# ===================


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


def rudol_move(rr, rc):
    min_dist = float('inf')
    sr, sc = None, None
    for row in range(N-1, -1, -1):
        for col in range(N-1, -1, -1):
            if arr[row][col] == 0:
                continue
            dist = (row-rr)**2 + (col-rc)**2
            if dist < min_dist:
                min_dist = dist
                sr, sc = row, col

    nxt_r, nxt_c, nxt_d = None, None, None
    for k in range(8):
        nr, nc = rr + dr[k], rc + dc[k]

        if not in_range(nr, nc):
            continue
        ddist = (nr-sr)**2 + (nc-sc)**2

        if ddist < min_dist:
            min_dist = ddist
            nxt_r, nxt_c, nxt_d = nr, nc, k

    return nxt_r, nxt_c, nxt_d


def santa_move(idx):
    sr, sc = santa_pos[idx]
    dist = (sr-rudol_r)**2 + (sc-rudol_c)**2

    s_pos = {tuple(coord) for coord in santa_pos.values()}
    nnr, nnc, nd = None, None, None
    for k in range(4):
        nr, nc = sr + dr[k*2], sc + dc[k*2]

        if not in_range(nr, nc):
            continue
        if (nr, nc) in s_pos:
            continue
        if (nr-rudol_r)**2 + (nc-rudol_c)**2 >= dist:
            continue

        dist = (nr-rudol_r)**2 + (nc-rudol_c)**2
        nnr, nnc, nd = nr, nc, k*2

    return nnr, nnc, nd


# 부딫혔을 때
def interaction(r, c, d, type):
    # 루돌프가 부딫혔을 때
    if type == 'rudol':
        idx = arr[r][c]
        point[idx] += rudol_power
        arr[r][c] = 0

        nr, nc = r + dr[d]*rudol_power, c + dc[d]*rudol_power

        if not in_range(nr, nc):
            santa_pos.pop(idx)
            return

        if arr[nr][nc] == 0:
            arr[nr][nc] = idx
            santa_pos[idx] = [nr, nc]
            return

        nxt_idx = arr[nr][nc]   # 이제 밀어야 되는 애
        arr[nr][nc] = idx
        santa_pos[idx] = [nr, nc]
        r, c = nr, nc
        while True:
            nr, nc = r + dr[d], c + dc[d]

            if not in_range(nr, nc):
                santa_pos.pop(nxt_idx)
                break

            if arr[nr][nc] == 0:
                arr[nr][nc] = nxt_idx
                santa_pos[nxt_idx] = [nr, nc]
                break

            temp_idx = arr[nr][nc]
            arr[nr][nc] = nxt_idx
            santa_pos[nxt_idx] = [nr, nc]

            nxt_idx = temp_idx
            r, c = nr, nc

    # 산타가 부딫혔을 때
    elif type == 'santa':
        idx = arr[r][c]
        point[idx] += santa_power
        arr[r][c] = 0

        nr, nc = r - dr[d] * santa_power, c - dc[d] * santa_power

        if not in_range(nr, nc):
            santa_pos.pop(idx)
            return

        if arr[nr][nc] == 0:
            arr[nr][nc] = idx
            santa_pos[idx] = [nr, nc]
            return

        nxt_idx = arr[nr][nc]   # 다음에 밀 애
        arr[nr][nc] = idx
        santa_pos[idx] = [nr, nc]
        r, c = nr, nc
        while True:
            nr, nc = r - dr[d], c - dc[d]

            if not in_range(nr, nc):
                santa_pos.pop(nxt_idx)
                break

            if arr[nr][nc] == 0:
                arr[nr][nc] = nxt_idx
                santa_pos[nxt_idx] = [nr, nc]
                break

            temp_idx = arr[nr][nc]
            arr[nr][nc] = nxt_idx
            santa_pos[nxt_idx] = [nr, nc]

            nxt_idx = temp_idx
            r, c = nr, nc


def debug_print(msg):
    if DEBUG:
        print('===', msg, '===')
        print('산타 위치')
        for row in arr:
            print(row)
        print()
        print('루돌프 위치: ', rudol_r, rudol_c)
        print()

####################
DEBUG = True
N, T, P, rudol_power, santa_power = map(int, input().split())
rudol_r, rudol_c = map(lambda x : int(x)-1, input().split())
arr = [[0]*N for _ in range(N)]
stun = [0]*(P+1)
santa_pos = {}
for _ in range(P):
    idx, r, c = map(int, input().split())
    santa_pos[idx] = [r-1, c-1]
    arr[r-1][c-1] = idx

point = [0]*(P+1)

# 8방향
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]


for turn in range(1, T+1):
    #print(f'{turn}번쨰 턴 시작==================')
    debug_print('현재 상황')

    # [1] 루돌프 움직이기
    rudol_r, rudol_c, rudol_d = rudol_move(rudol_r, rudol_c)

    #print('루돌프 이동: ', rudol_r, rudol_c)

    s_pos = {tuple(coord) for coord in santa_pos.values()}

    # 산타랑 충돌했으면 > 밀려나기
    if (rudol_r, rudol_c) in s_pos:
        stun[arr[rudol_r][rudol_c]] = 2
        interaction(rudol_r, rudol_c, rudol_d, 'rudol')

        debug_print('루돌프 충돌로 산타 밀려남 처리 완료')

    # 종료 확인 > 산타 모두 탈락?
    if len(santa_pos) == 0:
        break

    # [2] 산타 움직이기
    for idx in range(1, P+1):
        # 탈락 산타 제외
        if idx not in santa_pos.keys():
            continue

        # 기절 산타 제외
        sr, sc = santa_pos[idx]
        if stun[idx] > 0:
            continue

        nsr, nsc, sd = santa_move(idx)
        print(idx, '번째 산타 이동: ', nsr, nsc, sd)

        if nsr is None:
            continue

        arr[sr][sc] = 0
        arr[nsr][nsc] = idx
        santa_pos[idx] = [nsr, nsc]

        #print(idx, '번쨰 산타 이동:', nsr, nsc)

        # 루돌프랑 충돌했으면 > 밀려나기
        if nsr==rudol_r and nsc==rudol_c:
            stun[idx] = 2
            interaction(nsr, nsc, sd, 'santa')

            debug_print('산타 충돌로 산타 밀려남 처리 완료')

    # 종료 확인 > 산타 모두 탈락?
    if len(santa_pos) == 0:
        break

    # [3] 기절 -1
    for idx in range(1, P+1):
        if stun[idx] > 0:
            stun[idx] -= 1

    # [4] 살아남은 산타 +1
    for s in santa_pos.keys():
        point[s] += 1

print(*point[1:])