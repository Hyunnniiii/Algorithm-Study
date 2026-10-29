
""" AI 로봇청소기 / 20261007 ㅗㅗㅗㅗ / 체감 난이도: 골드5
소요 시간 대략 1시간?? / 시도 7회 / 실행 시간 176ms (코드트리) / 메모리 22MB (코드트리)

슈발 지현아 진짜 뭐하냐

"""

# 16:00 ~
# 출력: 각 턴마다 남아있는 먼지의 양
# ===================
from collections import deque


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


def move_cleaner(idx):
    r, c = cleaner[idx]

    if arr[r][c] > 0:
        return r, c

    Q = deque()
    Q.append((r, c))
    visit = [[0]*N for _ in range(N)]
    visit[r][c] = 1
    dist = float('inf')
    pos_lst = (float('inf'), float('inf'))
    cleaner_pos = {tuple(coord) for coord in cleaner.values()}

    while Q:
        sr, sc = Q.popleft()

        if visit[sr][sc] >= dist:
            break

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr, nc) or visit[nr][nc] != 0:
                continue
            if arr[nr][nc] == -1 or (nr,nc) in cleaner_pos:
                continue

            if arr[nr][nc] > 0:
                dist = visit[sr][sc] + 1
                visit[nr][nc] = visit[sr][sc] + 1
                pos_lst = min(pos_lst, (nr, nc))

            Q.append((nr, nc))
            visit[nr][nc] = visit[sr][sc] + 1

    if pos_lst[0] != float('inf'):
        return pos_lst[0], pos_lst[1]
    return None, None


def clean(idx):
    r, c = cleaner[idx]
    max_clean = -1
    max_dir = None

    for k in range(4):
        clean = arr[r][c]
        for kk in (0,-1,1):
            nr, nc = r + dr[(k+kk)%4], c + dc[(k+kk)%4]

            if not in_range(nr, nc) or arr[nr][nc] == -1:
                continue
            clean += min(20, arr[nr][nc])

        if max_clean < clean:
            max_clean = clean
            max_dir = k
    return max_dir


def debug_print(msg):
    if DEBUG:
        print('===', msg, '===')
        print('먼지 상황')
        for row in arr:
            print(row)
        print()
        print('로청 위치')
        print(cleaner)
        print()

######################
DEBUG = False
N, K, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cleaner = {}
for idx in range(1, K+1):
    r, c = map(int, input().split())
    cleaner[idx] = [r-1, c-1]

# 우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 물건 개수 미리 세두기
mat_cnt = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == -1:
            mat_cnt += 1

# 실행
for _ in range(L):
    # [1] 청소기 이동
    stay = 0
    for idx in range(1, K+1):

        nr, nc = move_cleaner(idx)

        if nr is None:
            stay += 1
            continue

        cleaner[idx] = [nr, nc]

    if stay == len(cleaner):
        pass
    else:
        # [2] 청소
        for idx in range(1, K+1):
            d = clean(idx)

            r, c = cleaner[idx]
            arr[r][c] = max(0, arr[r][c]-20)
            for k in (0,-1,1):
                nr, nc = r + dr[(d+k)%4], c + dc[(d+k)%4]

                if not in_range(nr, nc) or arr[nr][nc] == -1:
                    continue
                arr[nr][nc] = max(0, arr[nr][nc]-20)

        debug_print('청소 완료')

    # [3] 먼지 축적
    for r in range(N):
        for c in range(N):
            if arr[r][c] > 0:
                arr[r][c] += 5

    debug_print('먼지 축적 완료')

    # [4] 먼지 확산
    imsi = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                cnt = 0
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]

                    if not in_range(nr, nc) or arr[nr][nc] <= 0:
                        continue
                    cnt += arr[nr][nc]
                imsi[r][c] += cnt//10

    for r in range(N):
        for c in range(N):
            arr[r][c] += imsi[r][c]

    debug_print('먼지 확산')

    # [5] 출력
    ans = sum(map(sum, arr))+mat_cnt
    print(ans)
    if ans == 0:
        break
