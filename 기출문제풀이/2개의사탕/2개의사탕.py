
# 제출 후 ~10:43 화캉스

# 장애물 / 구멍은 딱 1개
# 상자 기울이면 어딘가에 부딫힐 때까지 기울인 방향으로 내려간다
# 목표: 상자 기울여서 빨간색 사탕 밖으로 빼내기, 파란색은 나오면 안됨 (동시도 인정x)
# 구할 것: 빨간색 밖으로 빼내기 위해 기울여야 하는 최소 횟수

# -----------------
# 4의 10승이면 얼마지? 2^20이니까 1024^2 = 10^6 정도면.. 만초 준거 보니까 다 해보란거네
# 아~~~~~~~~~~~~~~~~gkrltlfxck 아 니 백트래킹 안나온다 하지 않았나?

# 엣지: 사탕이 벽에 갇혀있는 경우 > -1 ..또 있나
# 주의: 사탕 처리 순서 - 기울인 방향에서 봤을 때 가까운 사탕부터 이동 (겹쳐있을 때 혼선 방지)
# R이 O에 갔을 때 B도 확인해야 한다는 점.

# 뭔가 또 백트래킹에서 원복 안한 것 같음

# import time
# start = time.time()
## 입력 받기
# 빈칸(.) / 장애물(#) / 파란색(B) / 빨간색(R) / 출구(O)
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
candy = {}

# 딕에 사탕 좌표 저장, 배열에는 사탕 없애기
for x in range(N):
    for y in range(M):
        if arr[x][y] == 'R':
            candy['red'] = [x, y]
            arr[x][y] = '.'
        if arr[x][y] == 'B':
            candy['blue'] = [x, y]
            arr[x][y] = '.'

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 함수: 빨강 > 파랑 순으로 이동
def red_first(red_r, red_c, blue_r, blue_c, d):
    global status, stop
    # 빨강을 먼저 보낸다
    while True:
        nr, nc = red_r + di[d], red_c + dj[d]

        if arr[nr][nc] == '#':
            candy['red'] = [red_r, red_c]
            break
        elif arr[nr][nc] == 'O':
            candy['red'] = [0, 0]
            red_r, red_c = 0, 0
            status = True   # 빨간색이 들어갔는가?
            break
        else:
            red_r, red_c = nr, nc

    # 파랑을 그 다음에
    while True:
        nr, nc = blue_r + di[d], blue_c + dj[d]

        if arr[nr][nc] == '#' or (nr == red_r and nc == red_c):
            candy['blue'] = [blue_r, blue_c]
            break
        elif arr[nr][nc] == 'O':
            stop = True     # 파란색이 들어갔는가?
            break
        else:
            blue_r, blue_c = nr, nc
    return stop, status

# 함수: 파랑 > 빨강 순으로 이동
def blue_first(red_r, red_c, blue_r, blue_c, d):
    global status, stop
    # 파랑을 먼저 보낸다
    while True:
        nr, nc = blue_r + di[d], blue_c + dj[d]

        if arr[nr][nc] == '#':
            candy['blue'] = [blue_r, blue_c]
            break
        elif arr[nr][nc] == 'O':
            candy['blue'] = [0, 0]
            blue_r, blue_c = 0, 0
            stop = True
            break
        else:
            blue_r, blue_c = nr, nc

    # 빨강을 그 다음에
    while True:
        nr, nc = red_r + di[d], red_c + dj[d]

        if arr[nr][nc] == '#' or (nr == blue_r and nc == blue_c):
            candy['red'] = [red_r, red_c]
            break
        elif arr[nr][nc] == 'O':
            status = True
            break
        else:
            red_r, red_c = nr, nc
    return stop, status

## 실행 함수: 백트래킹
status = False
stop = False
min_time = float('inf')
def ihatebtrk(ans):
    global status, stop, min_time
    # 조기종료: 파란색 들어갔을 때
    if stop:
        stop = False
        status = False
        return
    # 조기종료: 빨간색만 들어갔을 때
    if status:
        status = False
        min_time = min(min_time, ans)
        return
    # 종료: 10번이 지나도 불가능
    if ans == 10:
        return

    # 실행: 굴려
    rr, rc = candy['red'][0], candy['red'][1]
    br, bc = candy['blue'][0], candy['blue'][1]     # 기억해두기
    for direction in range(4):
        red_r, red_c = rr, rc
        blue_r, blue_c = br, bc
        candy['red'][0], candy['red'][1] = rr, rc
        candy['blue'][0], candy['blue'][1] = br, bc

        # 어떤 방향인지에 따라 뭘 먼저 실행하는지가 다르다
        if direction == 0:      # 위로 기울일 때
            if candy['red'][0] <= candy['blue'][0]:
                red_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)
            else:
                blue_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)

        elif direction == 1:    # 아래로 기울일 때
            if candy['red'][0] >= candy['blue'][0]:
                red_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)
            else:
                blue_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)

        elif direction == 2:    # 왼쪽으로 기울일 때
            if candy['red'][1] <= candy['blue'][1]:
                red_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)
            else:
                blue_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)

        elif direction == 3:    # 오른쪽으로 기울일 때
            if candy['red'][1] >= candy['blue'][1]:
                red_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)
            else:
                blue_first(red_r, red_c, blue_r, blue_c, direction)
                ihatebtrk(ans + 1)

ihatebtrk(0)
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)

# end = time.time()
# print(end-start)