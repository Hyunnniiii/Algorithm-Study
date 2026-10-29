
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


def check_left():
    left_lst = []
    checked = set()
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue
            if arr[r][c] in checked:
                continue

            my_idx = arr[r][c]
            checked.add(my_idx)
            sero, garo = box_info[my_idx]

            ok = True
            for row in range(r, r+sero):
                for col in range(c):
                    if arr[row][col] > 0:
                        ok = False
                        break
                if not ok:
                    break

            if not ok:
                continue
            left_lst.append(my_idx)
    return left_lst


def check_right():
    right_lst = []
    checked = set()
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue
            if arr[r][c] in checked:
                continue

            my_idx = arr[r][c]
            checked.add(my_idx)
            sero, garo = box_info[my_idx]

            ok = True
            for row in range(r, r+sero):
                for col in range(c+garo, N):
                    if arr[row][col] > 0:
                        ok = False
                        break
                if not ok:
                    break

            if not ok:
                continue
            right_lst.append(my_idx)
    return right_lst


def gravity():
    checked = set()
    for row in range(N-1,-1,-1):
        for col in range(N-1, -1, -1):
            if arr[row][col] == 0:
                continue
            if arr[row][col] in checked:
                continue

            my_idx = arr[row][col]
            checked.add(my_idx)
            sero, garo = box_info[my_idx]

            coord = []
            for x in range(row, row-sero, -1):
                for y in range(col, col-garo, -1):
                    coord.append((x,y))
                    arr[x][y] = 0

            move = 0
            while True:
                status = True
                for x, y in coord:
                    if not in_range(x+move, y):
                        status = False
                        break
                    if arr[x+move][y] > 0:
                        status = False
                        break
                if not status:
                    break
                move += 1

            move -= 1

            for x, y in coord:
                arr[x+move][y] = my_idx


def debug_print(msg):
    if DEBUG:
        print(msg)
        for row in arr:
            print(row)
        print()


##########################
DEBUG = True
N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
box_info = {}

# 택배 넣기
for _ in range(M):
    idx, sero, garo, col = map(int, input().split())

    box_info[idx] = [sero, garo]

    coord = []
    for r in range(sero):
        for c in range(col-1, col+garo-1):
            coord.append((r,c))

    move = 0
    while True:
        status = True
        for x, y in coord:
            if not in_range(x+move, y):
                status = False
                break
            if arr[x+move][y] > 0:
                status = False
                break
        if not status:
            break
        move += 1

    move -= 1
    for x, y in coord:
        arr[x+move][y] = idx

# 실행
while True:
    # [1] 왼쪽 하차
    left_lst = check_left()
    left_lst.sort()
    getout = left_lst[0]

    # 제일 작은 번호 하차
    print(getout)
    for r in range(N):
        for c in range(N):
            if arr[r][c] == getout:
                arr[r][c] = 0

    debug_print('왼쪽 제거')

    # 종료 확인
    if sum(map(sum, arr)) == 0:
        break

    # [2] 중력
    gravity()

    debug_print('중력')

    # [3] 오른쪽 하차
    right_lst = check_right()
    right_lst.sort()
    getout = right_lst[0]

    # 제일 작은 번호 하차
    print(getout)
    for r in range(N):
        for c in range(N):
            if arr[r][c] == getout:
                arr[r][c] = 0

    debug_print('오른쪽 하차')

    # 종료 확인
    if sum(map(sum, arr)) == 0:
        break

    # [4] 중력
    gravity()

    debug_print('중력')
