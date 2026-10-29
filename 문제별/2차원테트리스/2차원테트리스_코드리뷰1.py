
''' 2차원 테트리스 / 20260902 / 체감 난이도 : 골드 4
소요 시간: 2시간 10분 / 시도: 2회 / 실행 시간: 2564ms (코드트리) / 메모리: 31MB

[타임라인]
14:00 - 14:14(14분) 문제 읽기 / 입력 받기 / 구상
14:14 - 14:48 (34분) 구현 중
8분 휴식 =ㅅ=
14:56 - 15:42 (46분) 1차 제출 > fail
            -> 어느 곳이든 한 줄 다 채우면 +1인데 마지막 줄만 계산하고 있었음
15:42 - 16:19 (37분) 2차 제출 > 성공
            -> 한 줄 없애고 밀기 할 때 인덱싱 실수

[구상]
    - 테트리스 하는 판이 특이하게 생겨서 이걸 어디에 담아서 처리할지에 대해 고민을 좀 함.
    이전처럼 말의 개수가 적고, 좌표를 한번씩만 바꾸면 되는 구조는 아니라서 딕셔너리 포기하고 그냥
    10x10 배열을 선택했다.
    - 이번에는 종이에만 구상했는데 그랬더니 중간에서 꽉 찼을 때 제거한다 >> 이걸 까먹음 ㅡ..ㅡ
    그러면서 구현할 때 마지막 줄만 보면 되니까 쉽네~~ >> 이럼. 어이없음
    문제 읽으면서 주석 적는 것도 꼭 해야겠다 나는.......

[구현]
    - 구현하다가 이걸 어떻게 하지? 라는 생각이 많이 줄어든 것 같다
    - 뒷부분 구현할 때 반복되는 부분이 많아서 조금 통일할 순 없을까? 생각하긴 했지만 따로 떠오르는
    아이디어가 없어서 그냥.. 노가다 했다. 사람이 똑똑해야 덜 고생하는 건데 참 나 자신이 안타까울 따름
    아무튼 그러다 보니 빨간색 / 노란색 처리할 때 인덱싱이 다른 부분이 있는데 복붙하다 보니 실수가 나왔다.
    복붙하면서 할 때 정신을 똑바로 잡고 하기!!!!!!!!!!!!
    - for-else문 잘못 이해해서 씀. 근데 나의 for문 내부에 break가 없어서 그냥 while문 한 번 실행하고
    정상적으로 마무리 한 사람 됨. 만약 그렇게 하면 안되는 문제였다면.. 영문도 모르고 디버깅 했을듯 ㅠㅠ

[디버깅]
    - pprint로 단계마다 결과를 찍어보기도 했고 테트리스는 익숙하니까 어디에서 문제가
    발생했는지는 찾기가 쉬웠다
    - 다만 틀린 테케로 디버깅을 했기 때문에 테케 없이 틀린 부분 찾으라고 하면
    못찾았을 것 같다

---------------------------------------------------------
[개선할 사항]
- in_range 함수
- 빨강 / 노랑 한번에 처리하기: 대칭??

'''
# =======================================================
# 여기에선 for-else문 잘못된거 수정하고 복잡한 부분 sum 쓰는 등 간결하게 바꿈
# 실행시간은 오히려 늘어남


## 입력받기
A = int(input().strip())    # 블록 입력 횟수
arr = [[0 for _ in range(10)] for _ in range(10)]

# ====
# 함수: 범위 넘어가는지 확인
def in_range(rc):
    return 0 <= rc < 10

# ====
# 함수: 블록 종류와 위치 인덱스에 따라 파란색 배열에 블록을 표시한다
def color(block, row, col):
    if block == 1:
        arr[row][col] = 1
    elif block == 2:
        arr[row][col], arr[row][col+1] = 1, 1
    elif block == 3:
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

# 실행
ans = 0
for idx in range(A):
    t, x, y = map(int, input().split())

    # [1] 파란색 판에 표시
    color(t, x, y)

    # [2] 이동, 표시
    move(t, x, y)


    # [3] 삭제
    # 1. 행/열에 타일 가득 찬 경우 확인
    # 빨간 영역 확인
    for c in range(6, 10):
        if all(arr[r][c] == 1 for r in range(4)):
            ans += 1

            # 한 칸씩 밀기
            for cc in range(c, 4, -1):
                for rr in range(0,4):
                    arr[rr][cc] = arr[rr][cc-1]

    # 노란 영역 확인
    for r in range(6, 10):
        if all(arr[r][c] == 1 for c in range(4)):
            ans += 1

            # 삭제한 다음에 한 칸씩 밀기
            for rr in range(r, 4, -1):
                for cc in range(0,4):
                    arr[rr][cc] = arr[rr-1][cc]


    # 2. 연한 칸에 있는지 확인
    # 빨간색 연한 칸
    max_yun = 0
    for r in range(4):
        yun = sum(arr[r][4:6])
        max_yun = max(max_yun, yun)

    # 연한칸 넘어간 만큼 지운다
    for _ in range(max_yun):
        for r in range(0, 4):
            arr[r][9] = 0
        for c in range(8, 4, -1):
            for r in range(0, 4):
                arr[r][c+1] = arr[r][c]

    # 연한칸 모두 지우기
    for r in range(4):
        for c in range(4, 6):
            arr[r][c] = 0

    # 노란색 연한 칸
    max_yun = 0
    for c in range(0, 4):
        yun = sum(arr[r][c] for r in range(4,6))
        max_yun = max(max_yun, yun)

    # 연한칸 넘어간 만큼 지운다
    for _ in range(max_yun):
        for c in range(0, 4):
            arr[9][c] = 0
        for r in range(8, 4, -1):
            for c in range(0, 4):
                arr[r+1][c] = arr[r][c]

    # 연한칸 모두 지우기
    for c in range(4):
        for r in range(4, 6):
            arr[r][c] = 0

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

