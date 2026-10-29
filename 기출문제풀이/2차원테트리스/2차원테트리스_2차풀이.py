
""" 2차원 테트리스 / 20260927 내 한교동이 박살났다 / 체감 난이도: 골드
소요 시간 100분 / 시도 2회 / 실행 시간 334ms (코드트리) / 메모리 24MB (코드트리)

일단 1차 풀이보다는 훨 낫다.
구상을 좀 하다가 아예 엎었는데, 원래는 10x10 배열 만들어서 오른쪽/아래로 각각 옮기려다가.. (1차와 동일)
생각해보니 난 회전을 배웠잔슴 >> 오른쪽을 회전하면 아래가 아닐까 >> 회전도 아니고 그냥 블록 위치만 잘
맞춰주면 되잖아 >> 걍 배열 2개 만들어서 한번에 하면 되겠네 >> 냐호
그래서 좀 오래걸렸다. 하하하 난 왜 2차 풀이도 초면 같지 분명 풀엇는데

글고 첨에는 중력으로 내릴까? 했는데 (사실 중력 연습하려고 이 문제 고름)
블록이 2개짜리인 것도 있어서 중력이 더 어렵다고 생각했다.
다만 배열 삭제하고 미는 부분이 좀 맘에 안들어서 담에 다시 할듯

"""
# 15:05 ~ 15:30 손구상 ~ 15:40 주석 구상 ~ 16:30 중단 ~ 16:42 재개

# 구할 것: 얻은 점수 / 노랑, 빨강 보드에 타일이 있는 칸의 합
# =============================

import sys
sys.stdin = open('input.txt', 'r')

# 블록 타입을 입력하면 아래/오른쪽에서 확인해야 할 열 리스트를 반환
def find_col(type, x, y):
    if type == 1:
        return [y], [3-x]
    elif type == 2:
        return [y, y+1], [3-x]
    elif type == 3:
        return [y], [3-x, 2-x]


# 확인할 열에 대해 위에서부터 확인, 내려놓을 행 확인
def gravity(arr, col_lst):
    get_row = 5
    for col in col_lst:
        for row in range(6):
            if arr[row][col] == 0:
                continue
            if arr[row][col] == 1:
                find = row-1
                get_row = min(get_row, find)
                break
    return get_row


# 블록 배열에 표시해주기
def color_arr(type, arr, col_lst, row):
    if type == 1:
        for col in col_lst:
            arr[row][col] = 1
    if type == 2:
        if arr is down:
            for col in col_lst:
                arr[row][col] = 1
        if arr is right:
            for col in col_lst:
                arr[row][col] = 1
                arr[row-1][col] = 1
    if type == 3:
        if arr is down:
            for col in col_lst:
                arr[row][col] = 1
                arr[row-1][col] = 1
        if arr is right:
            for col in col_lst:
                arr[row][col] = 1


# 진한 영역에 꽉 찬 블록이 있는지 확인, 밀기
def check_full(arr):
    global ans

    row = 5
    while row >= 2:
        if sum(arr[row][:]) == 4:
            ans += 1

            for cr in range(row, 0, -1):
                arr[cr] = arr[cr-1][:]
            arr[0] = [0]*4
        else:
            row -= 1


# 연한 영역에 블록 있는지 확인하기
def check_light(arr):
    max_cnt = 0
    for col in range(4):
        cnt = 0
        for row in range(2):
            if arr[row][col] == 1:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    if max_cnt > 0:
        for row in range(5, max_cnt-1, -1):
            arr[row] = arr[row-max_cnt][:]
        for row in range(max_cnt):
            arr[row] = [0]*4


def debug_print(word):
    if DEBUG:
        print(word)
        print('아래')
        for row in down:
            print(row)
        print()
        print('오른쪽')
        for row in right:
            print(row)
        print()

#####################
DEBUG = False
k = int(input().strip())
down = [[0]*4 for _ in range(6)]
right = [[0]*4 for _ in range(6)]

# 실행부
ans = 0
for _ in range(k):
    t, x, y = map(int, input().split())

    # 블록 타입에 따라 각 배열에서 확인해야 할 열을 찾는다
    d_col, r_col = find_col(t, x, y)

    # 확인할 열에 대해 아래에서부터 확인, 가장 작은 행을 찾는다
    d_row = gravity(down, d_col)
    r_row = gravity(right, r_col)

    # 그러면 반환받은 행에 블록 타입에 맞게 표시해준다
    color_arr(t, down, d_col, d_row)
    color_arr(t, right, r_col, r_row)
    debug_print('==내리기 완료==')

    # 진한 영역에 꽉 찬 블록이 있는지 확인하고 밀어주기
    check_full(down)
    check_full(right)
    debug_print('==꽉 찬 줄 삭제==')

    # 연한 영역 처리
    check_light(down)
    check_light(right)
    debug_print('==연한 곳 튀어나와서 삭제==')

# 정산
print(ans)
print(sum(map(sum,down)) + sum(map(sum, right)))

