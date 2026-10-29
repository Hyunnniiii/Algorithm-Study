from collections import deque


# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

# 낮
def chichi_go(cr, cc):
    Q = deque()
    Q.append((cr, cc, -1))
    visit = [[-1]*N for _ in range(N)]
    visit[cr][cc] = 0
    dist = float('inf')
    hubo = []
    mouse_pos = set()
    for idx, r, c in mouse:
        if idx in mouse_alive:
            mouse_pos.add((r, c))

    # 쥐가 그 자리에 있는 경우
    if (cr,cc) in mouse_pos:
        return None

    while Q:
        sr, sc, dir = Q.popleft()

        if visit[sr][sc] >= dist:
            break

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr,nc) or visit[nr][nc] != -1:
                continue
            if arr[nr][nc] == -1:
                continue

            if (nr, nc) in mouse_pos:
                if visit[sr][sc] == 0:
                    visit[nr][nc] = visit[sr][sc] + 1
                    dist = visit[nr][nc]
                    hubo.append((nr,nc,k))
                else:
                    visit[nr][nc] = visit[sr][sc] + 1
                    dist = visit[nr][nc]
                    hubo.append((nr,nc,dir))

            else:
                if visit[sr][sc] == 0:
                    Q.append((nr, nc, k))
                    visit[nr][nc] = visit[sr][sc] + 1
                else:
                    Q.append((nr,nc, dir))
                    visit[nr][nc] = visit[sr][sc] + 1
    if not hubo:
        return None
    hubo.sort(key=lambda x : (-x[0], -x[1]))
    return hubo[0][2]

# 밤
def mouse_go(mr, mc):
    # 내 자리에 낙엽 있으면 안움직일래
    if arr[mr][mc] > 0:
        return None

    Q = deque()
    Q.append((mr, mc))
    visit = [[-2]*N for _ in range(N)]
    visit[mr][mc] = -1
    mouse_pos = set()
    for idx, r, c in mouse:
        if idx in mouse_alive:
            mouse_pos.add((r,c))

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr,nc) or visit[nr][nc] != -2:
                continue
            if (nr, nc) in mouse_pos or (nr==cat_r and nc==cat_c):
                continue

            if arr[nr][nc] > 0:
                if visit[sr][sc] == -1:
                    return k
                else:
                    return visit[sr][sc]

            else:
                if visit[sr][sc] == -1:
                    Q.append((nr, nc))
                    visit[nr][nc] = k
                else:
                    Q.append((nr,nc))
                    visit[nr][nc] = visit[sr][sc]
    return None


# 낙엽 확산
def leaf_spread():
    imsi = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if arr[row][col] <= 0:
                continue

            for k in range(4):
                nr, nc = row + dr[k], col + dc[k]

                if not in_range(nr,nc) or arr[nr][nc] > 0 or arr[nr][nc] == -1:
                    continue
                imsi[nr][nc] += arr[row][col]//5
                imsi[row][col] -= arr[row][col]//5

    for row in range(N):
        for col in range(N):
            arr[row][col] += imsi[row][col]


def debug_print(msg):
    if DEBUG:
        print('===', msg, '===')
        print('쥐들 상황: ', mouse)
        print('현재 살아있는 쥐 목록: ', mouse_alive)
        print('현재 죽은 쥐 목록: ', mouse_dead)
        print()
        print('현재 치치 위치:', cat_r, cat_c)
        print()
        print('현재 배열 상황')
        for row in arr:
            print(row)
        print()


#######################
DEBUG = False

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

TC = int(input().strip())
for test_case in range(1, TC+1):
    N, M, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cat_r, cat_c = map(lambda x : int(x)-1, input().split())
    mouse = []
    mouse_alive = set()
    mouse_dead = []
    for idx in range(1, M+1):
        r, c = map(int, input().split())
        mouse.append([idx, r-1, c-1])
        mouse_alive.add(idx)

    # 실행부
    status = False
    for time in range(1, T+1):
        debug_print('현재 상황')

        # [1] 낮: 치치 활동
        dir = chichi_go(cat_r, cat_c)

        # 안가도 되는 경우 / 못 가는 경우 제외하고 치치 한 칸 이동
        if dir is not None:
            cat_r, cat_c = cat_r + dr[dir], cat_c + dc[dir]

        debug_print('치치 이동')

        # 그 칸에 쥐가 있고 낙엽은 없으면 > 주거
        for idx, r, c in mouse:
            if cat_r == r and cat_c == c and arr[cat_r][cat_c] <= 0:
                if idx in mouse_alive:
                    mouse_alive.remove(idx)
                    mouse_dead.append(idx)

        # 쥐가 다 죽었으면 끝
        if len(mouse_alive) == 0:
            status = True
            print(f'#{test_case}', time, *mouse_dead)
            break

        debug_print('치치 이동 후 쥐 처리')

        # [2] 밤: 쥐 활동
        for idx in range(1, len(mouse)+1):
            if idx in mouse_alive:
                _, r, c = mouse[idx-1]
                dir = mouse_go(r, c)

                if dir is not None:
                    mouse[idx-1] = [mouse[idx-1][0], r+dr[dir], c+dc[dir]]

        debug_print('쥐 활동')

        # [3] 낙엽 확산
        leaf_spread()

        # [4] 바람 불기
        for row in range(N):
            for col in range(N):
                if arr[row][col] > 0:
                    arr[row][col] = max(0, arr[row][col]-5)

    if not status:
        print(f'#{test_case}', -1)
