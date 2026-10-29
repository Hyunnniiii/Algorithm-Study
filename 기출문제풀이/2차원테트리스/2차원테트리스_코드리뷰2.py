
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
    - for-else문 이상하게 씀. 왜냐면 잘 몰랐음 >> 다시 공부를..

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
# 이번엔 빨강/노랑 대칭 이용해서 풀어보겠습니다
# yellow (i,j) 입력 == red (j, 2-i) 입력과 같다. 90도 돌려서 생각

## 입력받기
A = int(input().strip())    # 블록 입력 횟수
red = [[0]*4 for _ in range(6)]
yellow = [[0]*4 for _ in range(6)]

# ====
# 함수: 범위 넘어가는지 확인
def in_range(rc):
    return 0 <= rc < 6

# ====
# 함수: 아래로 이동시키기. input에 red/yellow에 맞는 좌표와 배열 입력해주면 됨
def move(block, arr, row, col):
    if block == 1:
        cur_r = row
        while True:
            nxt_r = cur_r + 1

            if not in_range(nxt_r) or arr[nxt_r][col] == 1:
                arr[cur_r][col] = 1
                break
            cur_r = nxt_r

    elif block == 2:
        cur_r = row
        while True:
            nxt_r = cur_r + 1

            if not in_range(nxt_r) or arr[nxt_r][col] == 1 or arr[nxt_r][col+1] == 1:
                arr[cur_r][col] = 1
                arr[cur_r][col+1] = 1
                break
            cur_r = nxt_r

    elif block == 3:
        cur_r = row+1
        while True:
            nxt_r = cur_r + 1

            if not in_range(nxt_r) or arr[nxt_r][col] == 1:
                arr[cur_r-1][col] = 1
                arr[cur_r][col] = 1
                break
            cur_r = nxt_r

# ===
# 함수: 꽉 찬 줄은 삭제한다
def erase(arr):
    score = 0
    check_row = 5

    while check_row >= 2:
        if all(arr[check_row]):
            score += 1

            arr.pop(check_row)      # 전부 1인 행을 삭제: 5행 배열이 됨
            arr.insert(0, [0]*4)    # 맨 윗줄에 0 추가

        else:
            check_row -= 1  # 삭제하면 이전 행이 마지막 행이 되므로 else로
    return score

# ===
# 함수: 연한 부분에 넘어간 만큼 삭제한다
def light(arr):
    cnt = 0

    for r in range(2):
        if any(arr[r]):     # 행 중에 블록이 있는 것이 몇 개인가
            cnt += 1

    for _ in range(cnt):
        arr.pop()           # 마지막 행 삭제
        arr.insert(0, [0]*4)    # 맨 위에 0 삽입


# 실행
ans = 0
for idx in range(A):
    t, x, y = map(int, input().split())

    # [1] 이동, 표시
    move(t, yellow, 0, y)

    if t == 1:
        move(1, red, 0, 3-x)
    if t == 2:
        move(3, red, 0, 3-x)
    if t == 3:
        move(2, red, 0, 2-x)

    # [2] 삭제
    # 1. 행/열에 타일 가득 찬 경우 확인
    ans += erase(yellow)
    ans += erase(red)

    # 2. 연한 칸에 있는지 확인
    light(yellow)
    light(red)


ans_red = sum(sum(row) for row in red)
ans_yellow = sum(sum(row) for row in yellow)

print(ans)
print(ans_red + ans_yellow)

