
# 구할 것: 하차되는 택배 번호 순서대로 출력하기
# ==================================


# 택배 쌓기, 택배 행 정보 저장
def put_gravity(idx, sero, garo, col):
    put_row = 0
    for row in range(N):
        if sum(arr[row][col: col + garo]) != 0:
            break
        elif sum(arr[row][col: col + garo]) == 0:
            put_row = row

    box_col[idx] = []
    for row in range(put_row-sero+1, put_row+1):
        box_col[idx].append(row)
        for col in range(c-1, c+garo-1):
            arr[row][col] = idx


# 시계/반시계로 돌린 행렬에서 하차할 수 있는 택배 idx를 반환
def out_gravity(clock):     # clock=0 : 반시계 / clock=1 : 시계
    remove_lst = set()
    for col in range(N):
        for row in range(N-1, -1, -1):
            if imsi[row][col] == 0:
                continue

            idx = imsi[row][col]

            if clock == 0:  # 반시계면 c = r
                s, e = min(box_col[idx]), max(box_col[idx])
                for r in range(row, N):
                    if sum(imsi[r][s:e+1]) != 0 and not sum(imsi[r][s:e+1]) == idx * (e-s+1):
                        break
                    if sum(imsi[r][s:e+1]) == 0 or sum(imsi[r][s:e+1]) == idx * (e-s+1):
                        if r == N-1:
                            remove_lst.add(idx)
                            break

            elif clock == 1:  # 시계면 c = N-r-1
                s, e = N-max(box_col[idx])-1, N-min(box_col[idx])-1
                for r in range(row, N):
                    if sum(imsi[r][s:e+1]) != 0 and not sum(imsi[r][s:e+1]) == idx * (e-s+1):
                        break
                    if sum(imsi[r][s:e+1]) == 0 or sum(imsi[r][s:e+1]) == idx * (e-s+1):
                        if r == N-1:
                            remove_lst.add(idx)
                            break

    return remove_lst


def gravity_ver3():
    ok = set()  # 이미 한번 처리한 숫자는 다시 X
    for col in range(N):
        for row in range(N - 1, -1, -1):
            if arr[row][col] == 0:
                continue
            if arr[row][col] in ok:
                continue

            idx = arr[row][col]
            garo, sero = box_row[idx], len(box_col[idx])
            ok.add(idx)
            put_row = -1    # 주의
            for rr in range(row+1, N):
                if sum(arr[rr][col : col+garo]) != 0:
                    break
                elif sum(arr[rr][col : col+garo]) == 0:
                    put_row = rr

            if put_row != -1:
                for r in range(N):
                    for c in range(N):
                        if arr[r][c] == idx:
                            arr[r][c] = 0
                box_col[idx] = []
                for r in range(put_row-sero+1, put_row+1):
                    box_col[idx].append(r)
                    for c in range(col, col+garo):
                        arr[r][c] = idx


def debug_print(word):
    if DEBUG:
        print(word)
        for row in arr:
            print(row)
        print()

#############################
DEBUG = False
N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
box_col = {}    # {idx : [택배가 현재 배열에서 차지하는 행]}
box_row = {}    # {idx : 가로 길이}

# [1] 택배 투입
for _ in range(M):
    idx, sero, garo, c = map(int, input().split())

    # 가로 길이 저장
    box_row[idx] = garo

    # 중력 함수로 내리기
    put_gravity(idx, sero, garo, c-1)

debug_print('투입 완료')


# [2] 택배 하차
while True:
    debug_print('현재 상태')

    # 좌측
    imsi = [list(row[:][::-1]) for row in zip(*arr[::-1])][::-1]   # 반시계 회전

    rlst = out_gravity(0)
    rlst = list(rlst)
    rlst.sort()

    # print('좌측 후보:', rlst)
    if rlst:
        print(rlst[0])
        for r in range(N):
            for c in range(N):
                if arr[r][c] == rlst[0]:
                    arr[r][c] = 0
        box_col.pop(rlst[0])

    if sum(map(sum, arr)) == 0:
        break

    debug_print('제거 완')

    # 중력
    gravity_ver3()
    debug_print('중력')

    # 우측
    imsi = [list(row[:]) for row in zip(*arr[::-1])]  # 시계

    rlst = out_gravity(1)
    rlst = list(rlst)
    rlst.sort()

    # print('우측 후보:', rlst)
    if rlst:
        print(rlst[0])
        for r in range(N):
            for c in range(N):
                if arr[r][c] == rlst[0]:
                    arr[r][c] = 0
        box_col.pop(rlst[0])

    debug_print('제거 완')

    if sum(map(sum, arr)) == 0:
        break

    # 중력
    gravity_ver3()
    debug_print('중력')
