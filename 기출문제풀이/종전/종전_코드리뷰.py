

''' 종전 / 20260831 / 체감 난이도 : ??? (골드 5 이상으로는 난이도 체감 불가;;)
소요 시간: 2시간 50분 / 시도: 1회 / 실행 시간: 995ms (코드트리) / 메모리: 29MB

[타임라인]
# 15:46 - 16:01(15분) 문제 읽기 / 1차 구상 
# 백트래킹 1차 시도
# 16:09 - 16:22(13분) 2차 구상
# 백트래킹 2차 시도
# 16:32 - 16:50(18분) 3차 구상
# 백트래킹 진짜 최종 시도 및 포기
# 16:50 - 17:45 구현 거의 끝냈는데 시간 다 지남
# 맛있는 토마토계란밥을 먹었당
# 18:50 - 19:38(48분) 인덱싱 지옥 디버깅, 코드 수정 > 제출

[구상]
- (???)
    - 다이아몬드 모양 그냥 어떻게 구현해야 할지 감도 잡히지 않았음. 그냥 정해진 모양 그리라면 
    그릴 수 있는데, 이걸 백트래킹이랑 연관지어서 구현하려니까 그냥 몰겠음..
    지금까지의 경험상 가능한 좌표를 죄다 리턴해서 백트래킹 따로, 부족 숫자 채우고 계산하는거 따로
    하면 100% 시간 초과 날거기 때문에 리턴으로 1번 부족 visit 배열을 받고, 그걸 바탕으로 나머지
    부족 계산을 리턴 전에 하려고 했는데, 그게 구현이 안됨..

[구현]
- (good)
    - 아무튼 무식해도 풀어내긴 했다. 근데 인덱싱이 너무 복잡해서 디버깅 너무 어렵고, 좀만 정신놓고 코드 쓰다보면
    실수하기 좋다. 실제로 row 인덱싱에 col 번호를 써서 계속 다른 답이 나왔는데, 이거 찾는데 너무 오래 걸렸다
- (bad)
    - 레전드 무식한 풀이. 수행시간 995ms 나온거 보니까 정말 간당간당하게 통과함.

[디버깅]
    - 애초에 디버깅이 너무 힘든 코드다.. pprint로 visit 하나하나 확인하면서 체크했다.
    왜냐면 진짜 이 문제 어떻게 접근해야 할지 전혀 감도 안잡힘

[후기]
    - 진짜 난 백트래킹이 너무 싫다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    백트래킹 너무 어려움 ㅜ 너무 어렵고 맨날 시간초과 나고 구현하기 힘들다 
    그래도 친해져야겠지..
    - 어렵다.

---------------------------------------------------------
[개선할 사항]
- 백트래킹 풀이 해보기

'''
# =======================================================

# 구할 것: 인구 수 최대/최소의 차이가 최소일 때의 값

# [1] 기울어진 직사각형 선택
# 반시계 방향 순회, 각 방향으로 최소 1번씩은 진행, 범위 벗어나면 안됨

# [2] 나머지 부족의 인구수 구하기
# 1번: 기울어진 직사각형 경계, 내부
# 2번: 좌측 상단: 위 꼭짓점 열 포함, 좌 꼭짓점 왼쪽 포함 X
# 3번: 우측 상단: 위 꼭짓점 열 포함 X, 우 꼭짓점 오른쪽 포함
# 4번: 좌측 하단: 아래 꼭짓점 열 포함 X, 좌 꼭짓점 왼쪽 포함
# 5번: 우측 하단: 아래 꼭짓점 열 포함, 우 꼭짓점 오른쪽 포함 X

## 입력 받기
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

from itertools import product


# 왼쪽으로 꼭짓점이 될 수 있는 모든 좌표 저장
def possible_l(si, sj, llst):
    while True:
        ni, nj = si + 1, sj - 1
        if 0 <= ni < N and 0 <= nj < N:
            llst.append((ni, nj))
            si, sj = ni, nj
        else:
            break
    return llst


# 오른쪽으로 꼭짓점이 될 수 있는 모든 좌표 저장
def possible_r(si, sj, rlst):
    while True:
        ni, nj = si + 1, sj + 1
        if 0 <= ni < N and 0 <= nj < N:
            rlst.append((ni, nj))
            si, sj = ni, nj
        else:
            break
    return rlst


ans = float('inf')
for row in range(N - 2):
    for col in range(1, N - 1):

        # 해당 배열에서 시작해서 갈 수 있는 모든 꼭짓점의 좌표 조합 반환
        for square in product(possible_l(row, col, []), possible_r(row, col, [])):

            status = True  # 맨 밑 꼭짓점 범위 넘어가는지 확인용

            # 1번 부족
            # visit에 표시하기
            visit[row][col] = 1

            # 왼쪽으로 꼭짓점까지 가면서 1 체크
            lrow, lcol = row, col
            lcnt = 0
            while lrow < square[0][0] and lcol > square[0][1]:
                lrow, lcol = lrow + 1, lcol - 1
                visit[lrow][lcol] = 1
                lcnt += 1

            # 오른쪽으로 가면서 1 체크
            rrow, rcol = row, col
            rcnt = 0
            while rrow < square[1][0] and rcol < square[1][1]:
                rrow, rcol = rrow + 1, rcol + 1
                visit[rrow][rcol] = 1
                rcnt += 1

            # 왼쪽 꼭짓점에서 밑 꼭짓점까지 1 기록
            for left in range(1, rcnt + 1):
                lrow, lcol = lrow + 1, lcol + 1
                if not (0 <= lrow < N and 0 <= lcol < N):
                    status = False
                    break
                visit[lrow][lcol] = 1

            # 오른쪽 꼭짓점에서 밑 꼭짓점까지 1 기록
            for right in range(1, lcnt + 1):
                rrow, rcol = rrow + 1, rcol - 1
                if not (0 <= rrow < N and 0 <= rcol < N):
                    status = False
                    break
                visit[rrow][rcol] = 1

            # 밑 꼭짓점 기록하다가 범위를 넘었다면 불가능
            if not status:
                visit = [[0] * N for _ in range(N)]
                continue

            # 사각형 내부까지 1로 채우기
            for row1 in range(row, row + lcnt + rcnt + 1):
                boundary = []  # 행마다 1 채울 시작/끝좌표 기록

                for col1 in range(N):
                    if visit[row1][col1] == 1:
                        boundary.append(col1)

                if len(boundary) >= 2:
                    for cc in range(boundary[0], boundary[-1] + 1):
                        visit[row1][cc] = 1

            ## 다른 부족 표시하기
            # 2번 부족
            for row2 in range(0, square[0][0]):
                for col2 in range(0, col + 1):
                    if visit[row2][col2] == 1:
                        break
                    visit[row2][col2] = 2

            # 3번 부족
            for row3 in range(0, square[1][0] + 1):
                for col3 in range(row, N):
                    if visit[row3][col3] == 0:
                        visit[row3][col3] = 3

            # 4번 부족
            for row4 in range(square[0][0], N):
                for col4 in range(0, square[0][1] + rcnt):
                    if visit[row4][col4] == 1:
                        break
                    visit[row4][col4] = 4

            # 5번 부족
            for row5 in range(square[1][0] + 1, N):
                for col5 in range(square[0][1] + rcnt, N):
                    if visit[row5][col5] == 1:
                        continue
                    visit[row5][col5] = 5

            # pprint.pprint(visit)

            # 정산하기
            one, two, three, four, five = 0, 0, 0, 0, 0
            for frow in range(N):
                for fcol in range(N):
                    if visit[frow][fcol] == 1:
                        one += arr[frow][fcol]
                    if visit[frow][fcol] == 2:
                        two += arr[frow][fcol]
                    if visit[frow][fcol] == 3:
                        three += arr[frow][fcol]
                    if visit[frow][fcol] == 4:
                        four += arr[frow][fcol]
                    if visit[frow][fcol] == 5:
                        five += arr[frow][fcol]
            find = max(one, two, three, four, five) - min(one, two, three, four, five)
            ans = min(ans, find)

            square = []
            visit = [[0] * N for _ in range(N)]

print(ans)

# square 갱신 필요없고 visit에 그냥 처리하면 더 빨라질 수 있음