# 14:48 잠시 휴식좀... 14:56 복귀
# 15:34 일단 구현 완
# 15:42 어느 곳이든 한 줄 다 채우면 +1인데 마지막줄만 계산하고 있었음!
# 16:19 밀기 할 때 인덱싱 1씩 잘못한듯

## 입력받기
A = int(input().strip())    # 블록 입력 횟수
arr = [[0 for _ in range(10)] for _ in range(10)]

# ====
# 함수: 범위 넘어가는지 확인
def in_range(rc):
    if 0 <= rc < 10:
        return 0 <= rc < 10

# ====
# 함수: 블록 종류와 위치 인덱스에 따라 파란색 배열에 블록을 표시한다
def color(block, row, col):
    if block == 1:
        arr[row][col] = 1
    if block == 2:
        arr[row][col], arr[row][col+1] = 1, 1
    if block == 3:
        arr[row][col], arr[row+1][col] = 1, 1

# ====
# 함수: 오른쪽/아래로 이동시키고, 파란색에서는 제거
def move(block, row, col):

    if block == 1:
        cur_r, cur_c = row, col
        # 오른쪽 이동: 열만 확인
        while True:
            nxt_c = cur_c + 1

            if not in_range(nxt_c) or arr[row][nxt_c] == 1:
                arr[row][cur_c] = 1
                break
            else:
                cur_c = nxt_c

        # 아래 이동: 행만 확인
        while True:
            nxt_r = cur_r + 1

            if not in_range(nxt_r) or arr[nxt_r][col] == 1:
                arr[cur_r][col] = 1
                break
            else:
                cur_r = nxt_r

        # 다 하면 파란색에서 표시 제거
        arr[row][col] = 0

    if block == 2:
        cur_r, cur_c = row, col + 1
        # 오른쪽 이동: 열만 확인
        while True:
            nxt_c = cur_c + 1

            if not in_range(nxt_c) or arr[row][nxt_c] == 1:
                arr[row][cur_c] = 1
                arr[row][cur_c-1] = 1
                break
            else:
                cur_c = nxt_c

        # 아래 이동: 행만 확인
        cur_r, cur_c = row, col
        status = True
        while status:
            nxt_r = cur_r + 1

            for cols in (col, col+1):
                if not in_range(nxt_r) or arr[nxt_r][cols] == 1:
                    arr[cur_r][col] = 1
                    arr[cur_r][col+1] = 1
                    status = False
                    break
            else:
                cur_r = nxt_r

        # 다 하면 파란색에서 표시 제거
        arr[row][col] = 0
        arr[row][col+1] = 0

    if block == 3:
        # 오른쪽 이동: 열만 확인
        cur_r, cur_c = row, col
        status = True
        while status:
            nxt_c = cur_c + 1

            for rows in (row, row+1):
                if not in_range(nxt_c) or arr[rows][nxt_c] == 1:
                    arr[row][cur_c] = 1
                    arr[row + 1][cur_c] = 1
                    status = False
                    break
            else:
                cur_c = nxt_c

        # 아래 이동: 행만 확인
        cur_r, cur_c = row+1, col
        while True:
            nxt_r = cur_r + 1

            if not in_range(nxt_r) or arr[nxt_r][col] == 1:
                arr[cur_r-1][col] = 1
                arr[cur_r][col] = 1
                break
            else:
                cur_r = nxt_r

        # 다 하면 파란색에서 표시 제거
        arr[row][col] = 0
        arr[row+1][col] = 0

# import pprint
# 실행
ans = 0
for idx in range(A):
    t, x, y = map(int, input().split())
    # print(idx+1, '번째 블록')

    # [1] 파란색 판에 표시
    color(t, x, y)
    # print('놓기')
    # pprint.pprint(arr)

    # [2] 이동, 표시
    move(t, x, y)
    # print('이동 완료')
    # pprint.pprint(arr)

    # [3] 삭제
    # 1. 행/열에 타일 가득 찬 경우 확인
    # 빨간 영역 확인
    go = True
    while go:
        for c in range(6, 10):
            cnt = 0
            for r in range(0, 4):
                if arr[r][c] == 1:
                    cnt += 1

            # 만약 가득 찬 곳이 있으면 점수 반영하고, 삭제
            if cnt == 4:
                ans += 1
                for r in range(0,4):
                    arr[r][c] = 0

                # 삭제한 다음에 한 칸씩 밀기
                for cc in range(c, 4, -1):
                    for rr in range(0,4):
                        arr[rr][cc] = arr[rr][cc-1]

        # 가득 찬 곳이 더이상 없으면 넘어가기
        else:
            go = False
            break

    # print('빨간 영역 확인')
    # pprint.pprint(arr)

    # 노란 영역 확인
    go = True
    while go:
        for r in range(6, 10):
            cnt = 0
            for c in range(0, 4):
                if arr[r][c] == 1:
                    cnt += 1

            # 만약 가득 찬 곳이 있으면 점수 반영하고, 삭제
            if cnt == 4:
                ans += 1
                for c in range(0, 4):
                    arr[r][c] = 0

                # 삭제한 다음에 한 칸씩 밀기
                for rr in range(r, 4, -1):
                    for cc in range(0,4):
                        arr[rr][cc] = arr[rr-1][cc]


        # 가득 찬 곳이 더이상 없으면 넘어가기
        else:
            go = False
            break

    # print('노란 영역 확인')
    # pprint.pprint(arr)

    # 2. 연한 칸에 있는지 확인
    # 빨간색 연한 칸
    max_yun = 0
    for r in range(0,4):
        yun = 0
        for c in range(4,6):
            if arr[r][c] == 1:
                yun += 1
        max_yun = max(max_yun, yun)

    # 연한칸 넘어간 만큼 지운다
    for _ in range(max_yun):
        for r in range(0, 4):
            arr[r][9] = 0
        for c in range(8, 4, -1):
            for r in range(0, 4):
                arr[r][c+1] = arr[r][c]

    # 연한칸 모두 지우기
    for r in range(0, 4):
        for c in range(4, 6):
            arr[r][c] = 0

    # print('빨간 연한 영역 확인')
    # pprint.pprint(arr)

    # 노란색 연한 칸
    max_yun = 0
    for c in range(0, 4):
        yun = 0
        for r in range(4, 6):
            if arr[r][c] == 1:
                yun += 1
        max_yun = max(max_yun, yun)

    # 연한칸 넘어간 만큼 지운다
    for _ in range(max_yun):
        for c in range(0, 4):
            arr[9][c] = 0
        for r in range(8, 4, -1):
            for c in range(0, 4):
                arr[r+1][c] = arr[r][c]

    # 연한칸 모두 지우기
    for c in range(0, 4):
        for r in range(4, 6):
            arr[r][c] = 0

    # print('노란 연한 영역 확인')
    # pprint.pprint(arr)


ans_red = 0
ans_yellow = 0
for row in range(0,4):
    for col in range(6, 10):
        if arr[row][col] == 1:
            ans_red += 1
for row in range(6,10):
    for col in range(0, 4):
        if arr[row][col] == 1:
            ans_yellow += 1

print(ans)
print(ans_red + ans_yellow)

