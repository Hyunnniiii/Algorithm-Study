
""" 아기 거부기 / 20261008 / 체감 난이도: 골드5
소요 시간 70분 / 시도 2회 / 실행 시간 88ms (코드트리) / 메모리 18MB (코드트리)

첫 제출 틀린 이유: range(1, M+1)인데 M이라고 씀
ㅋㅋ
거부기 화이팅

"""

# 10:15 ~
# 구할 것: ID 순서대로 바다거북이 도착한 턴 번호
# ==============================
from collections import deque


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


def turtle_move(idx):
    r, c = turtle[idx]

    Q = deque()
    Q.append((r, c))
    visit = [[-1]*N for _ in range(N)]
    visit[r][c] = -2
    turtle_pos = {tuple(coord) for coord in turtle.values()}

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr, nc) or visit[nr][nc] != -1 or visit[nr][nc] == -2:
                continue
            if arr[nr][nc] == 1 or arr[nr][nc] == -1:
                continue
            if (nr, nc) in turtle_pos:
                continue

            if nr == N-1 and nc == N-1:
                if visit[sr][sc] == -2:
                    return k
                else:
                    return visit[sr][sc]

            if visit[sr][sc] == -2:
                Q.append((nr, nc))
                visit[nr][nc] = k

            else:
                Q.append((nr, nc))
                visit[nr][nc] = visit[sr][sc]

    return None


def debug_print(msg):
    if DEBUG:
        print('===', msg, '===')
        print('거부기 위치')
        print(turtle)
        print()
        print('압력')
        for row in brr:
            print(row)
        print()


################################
DEBUG = True
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
brr = [[0]*N for _ in range(N)]
turtle = {}     # {idx : [r, c, P]}
for idx in range(1, M+1):
    r, c = map(int, input().split())
    turtle[idx] = [r, c]
volcano = []
for _ in range(K):
    r, c, P = map(int, input().split())
    volcano.append([r,c,P])
ans = [-1]*(M+1)

debug_print('입력 확인')

# 우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 실행
finish = set()  # 이미 도착했거나 화석이 된 거부기
for turn in range(1, 100):
    #print('======', turn,'턴 시작', '========')

    # [1] 거부기 순서대로 이동
    for idx in range(1, M+1):
        # 이미 끝난 거부기 제외
        if idx in finish:
            continue

        r, c = turtle[idx]
        d = turtle_move(idx)

        # 경로가 없으면 > 스킵
        if d is None:
            continue

        # 안식처면 finish에 넣기
        nr, nc = r + dr[d], c + dc[d]

        if nr==N-1 and nc==N-1:
            ans[idx] = turn
            finish.add(idx)
            continue

        # 아니면 거부기 딕 수정
        turtle[idx] = [nr, nc]

    debug_print('거부기 이동 완')

    # [2] 화산 압력 증가
    for r, c, _ in volcano:
        brr[r][c] += 10

    debug_print('압력 증가')

    # [3] 화산 분출
    imsi = [[0]*N for _ in range(N)]
    done = set()
    while True:
        cnt = 0
        for r, c, p in volcano:
            if (r,c,p) in done:
                continue

            if brr[r][c] + imsi[r][c] < p:
                continue

            cnt += 1
            done.add((r,c,p))
            imsi[r][c] += p
            for k in range(4):
                sr, sc = r, c
                fire = p
                while True:
                    fire = fire // 2
                    nr, nc = sr + dr[k], sc + dc[k]

                    if fire == 0:
                        break
                    if not in_range(nr, nc):
                        break
                    if arr[nr][nc] == 1:
                        break

                    imsi[nr][nc] += fire
                    sr, sc = nr, nc

        if cnt == 0:
            break

    debug_print('화산 분출 완료')
    for row in imsi:
        print(row)
    print()


    # [4] 화석화
    for idx in range(1,M+1):
        if idx in finish:
            continue

        r, c = turtle[idx]

        print(imsi[r][c] + brr[r][c])
        if imsi[r][c] + brr[r][c] >= 20:
            arr[r][c] = -1
            finish.add(idx)

    debug_print('화석화 완료')

    # [5] 초기화
    for r, c, _ in done:
        brr[r][c] = 0

    debug_print('초기화 완료')

    # [6] 조기 종료 확인
    if len(finish) == M:
        break

for x in ans[1:]:
    print(x)