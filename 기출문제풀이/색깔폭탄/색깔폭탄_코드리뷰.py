
''' 색깔 폭탄 / 20260908 / 체감 난이도 : 골드 3
소요 시간: 3시간+ / 시도: 3회 / 실행 시간: 187ms (코드트리) / 메모리: 22MB

[타임라인]
14:02 - 14:18(16분) 문제 읽기 / 입력 받기 / 구상
14:48 - 16:30 (102분) 구현, 디버깅
16:30 - ... 디버깅, 갈아엎기, 화참기

[구상]
    - 문제가 너무 길어서 당황함. 왜냐면 딱 봐도 구현량이 너무 많아서.
    - 어쩜 이렇게 한 문제 안에 할 것들이 이리 많나?? 근데 반대로 생각하면 내가 이런 문제도 풀 수준이 된거임
    나 한달 전에 프린트밖에 못했는데 지금 이러고 있음. 푸하하 시간 많으니 쫄지마르
    - 애매하다고 생각되는 부분은 없었는데, 우선순위 처리하는 방식이 되게 새롭고 까다롭다고 느꼈다.
    보통 행 > 열 작은 순서인데 이 문제는 꼬아놨고 기준칸이라는 개념도 있어서..
    신경써서 구현해야겠다고 생각했음 >> 진짜 대박인게 이렇게 생각해놓고도 기준칸 조건 놓침

[구현]
- (good)
    - 꾸역꾸역 구현하니까 되긴 함. 점점 느낌이 산넘어산..
    - 그냥 화내지 말고 하라는거 잘 하다보면.. 끝은 온다

- (bad)
    - 나는 중력 함수에서 오래 걸릴거라고 생각했는데 생각보다 묶음 고르고, 우선순위 따지는 함수에서
    엄청 오래 걸렸음. 그리고 점점 구상 단계에서 생각치 못했던 요소들을 코드에 반영하려다 보니 복잡해지고
    나중 가서는 나도 이 변수가 뭐였는지 기억이 안나기 시작함;;
    - 솔직히 구현하면서 쫄았음. 왜냐면 중력 << 뭔가 자주 들어본 코딩 테스트 유형 단어(?)라서 어렵겠지? 생각했고,
    막상 구현하다 보니 중력 함수 구현하기도 전에 막히니까.. 쫄지마!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    어려우면 뒷부분 먼저 구현하고 다시 돌아와
    - 진짜 내가 화가 이렇게 많았나 싶음 구현이 끝이 안나니까 화가남. 겨우 하나 다 했더니 또 다른거 해야돼 인내심 테스트도 같이 하고 있음 나는

[디버깅]
    - 디버깅이고 뭐고 변수가 뭐였는지 기억이 안나길래 첫번째 함수 엎고 시작함
    - 틀리고 나서 중력 함수를 처음에 의심했는데, 내가 틀린 테케가 너무 사이즈가 크고 10번 넘어가는 테케이기도 해서
    그냥 내가 작은 테케 만들어서 돌려봤다. 여기서 틀린 부분 찾아냄!! 작은 테케를 자주 만들어봅시다

---------------------------------------------------------
[코드 개선]
1. find 함수 너무 복잡함. 나누는게 더 깔끔할지도
ㄴ> 묶음 찾는 함수 / 우선순위 따지는 함수 로 분리해보겠음
2. 중력 함수 다른 방식 없을까? 끝부분 처리가 좀.. 맘에 안듦
3. 우선순위 비교 이상함


187ms > 177ms
시간 상으론 별 차이 없지만 코드가 훨씬 이해하기 쉬워짐
'''
# =======================================================

# -1 돌 / 0 빨강 / 1~N 나머지 색
# 1. 가장 큰 폭탄 묶음 고르기 (상하좌우 인접 그룹)
# - 2개 이상, 같은 색깔로 구성되어야 함. 이때 빨간색 폭탄은 색이 달라도 포함할 수 있음.
# - 돌은 당연히 포함이 아니겠지

# 2. 묶음 고르기 우선순위
# - 크기가 큰 묶음 > 빨간색이 적게 포함 > 기준칸의 행이 큰 묶음 > 기준칸의 열이 작은 묶음
# - 기준칸이란? : 빨강이 아니면서 행이 가장 큰 칸 > 열이 가장 작은 칸

# 3. 선택한 묶음 제거, 중력 작용
# 돌을 제외하고 중력의 작용을 받는다

# 4. 반시계 회전, 중력 작용

# [주의]
# 맨 처음부터 묶음이 없는 경우 (모두 돌이라던가, 모두 빈칸이라던가..)
# 묶음을 정하는 기준이 복잡하다. 정신 차리고 구현할 것

# 아니 나 이거 내가 짜놓고도 헷갈린다. 이럼 안된다고 이거 find 함수 인자 실화냐? 진짜 이렇게 짜지 말라고 > 수정함
# 뭐임? 진짜 뭐 틀렸는지 모르겠음 >> 빨간색은 기준칸 안됨..
# 이거 구현 시간이 길다보니까 조건을 하나씩 내가 빠뜨린다...
# ======================================================

# [후기]
# 일단 중력 구하는 함수에서 어떻게 구현할지 고민 겁나 오래 함. 어떻게 구현해내긴 했지만 딱히 맘에 들진 않음..
# 중력 구하기의 경우 제대로 됐는지 작은 테케 만들어서 검증해봤는데 틀린 부분 발견함. 작은 테케 습관화
# 주석에 써놓고도 놓친 조건이 있다.. 빨간칸은 기준칸 안된다는 것. 구현 시간이 길어지니까 내가 써놓고도 까먹는데 이런건 우짜냐 진짜
# 아니 심지어 문제를 다시 읽어도 그게 안보임. 뭐냐 진짜
# find 함수에서 우선순위 처리하는 것도 힘들었던게 그 종료조건. 그룹을 찾지 못했을 때 어떻게 브레이크 걸어야 할지
# 회전은 사실 배운거 써먹어서 쉬웠다. 푸하하


#     - 요즘 드는 생각이, 드래곤 커브 / 피자스쿨 / 미로타워 디펜스같이 뭔가 수학이나 도형에서 규칙을 찾아서 푸는 문제는
#     오히려 풀이 성공 확률이 높은 것 같고,
#     정직하게 구현하는 문제(술래잡기, 색깔폭탄)에서는 오히려 조건을 몇 개 놓치거나 구현 자체를 굳이 너무 어렵게 접근해서
#     따로 처리해야할 엣지가 많아지고, 그에 따라 변수도 너무 많이 생성하면서 코드가 복잡해지고 성공 확률도 좀 낮은 것 같은데 ..
#     이런 경우 그냥 더 꼼꼼하게 문제를 읽고 처리하는 방법밖엔 답이 읎는 것일까

# ===============
## 가즈아
from collections import deque

## 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

## 필요한 요소들 생성
# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 범위 체크
def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < N

## 함수 생성
# 1. 우선순위에 따른 묶음을 찾는 함수.
def find():
    global ans, status
    visit = [[0] * N for _ in range(N)]
    red_cnt = 0  # 묶음 내 빨간색의 개수

    final_coord =  []
    final_red_cnt = 0
    final_real_x, final_real_y = -1, 100
    for r in range(N):
        for c in range(N):
            coord = []      # 한 그룹 내 모든 좌표를 여기에 저장

            # 빨간색이 아닌 곳에서 시작할게. 빨간색만 있는 경우 방지
            if visit[r][c] == 0 and arr[r][c] > 0:
                Q = deque([[r, c]])
                my_color = arr[r][c]
                visit[r][c] = 1
                red_cnt = 0  # 묶음 내 빨간색의 개수

                coord.append([r, c])

                while Q:
                    sr, sc = Q.popleft()

                    for k in range(4):
                        nr, nc = sr + di[k], sc + dj[k]

                        # 범위 내에 있으면서 색이 같거나 빨간색인 경우
                        if in_range(nr, nc) and visit[nr][nc] == 0 and (
                                arr[nr][nc] == 0 or arr[nr][nc] == my_color):

                            Q.append([nr, nc])
                            visit[nr][nc] = 1
                            coord.append([nr, nc])
                            if arr[nr][nc] == 0:
                                red_cnt += 1

            # 못 찾았거나, 1개만 있으면 패스
            if coord == [] or len(coord) == 1:
                continue
            else:
                # 기준칸 찾기
                coord.sort(key = lambda x : (-x[0], x[1]))
                for hubo in coord:
                    if arr[hubo[0]][hubo[1]] != 0:
                        real_x, real_y = hubo[0], hubo[1]
                        break

                if len(coord) > len(final_coord) or (len(coord) == len(final_coord) and red_cnt < final_red_cnt) or \
                        (len(coord) == len(final_coord) and red_cnt == final_red_cnt and real_x > final_real_x) or \
                        (len(coord) == len(final_coord) and red_cnt == final_red_cnt and real_x == final_real_x and real_y < final_real_y):
                    final_coord = coord
                    final_red_cnt = red_cnt
                    final_real_x, final_real_y = real_x, real_y

            # 빨간색은 다른 그룹에도 속할 수 있으니까 초기화
            for row in range(N):
                for col in range(N):
                    if arr[row][col] == 0:
                        visit[row][col] = 0

    if final_coord == []:
        status = False
        return status

    else:
        for coord in final_coord:
            # 제거하고 점수에 추가
            arr[coord[0]][coord[1]] = -7
            ans += len(final_coord)

    return status

# 2. 중력 함수
# 돌을 찾고, 그 돌의 인덱스 기준으로 이전까지 전부 돌쪽으로 민다.
# 돌 없이 마지막이 나오면.. 마지막 기준으로 전부 밀기
def gravity():
    for col in range(N):
        row = N - 1
        lst = []
        last_rock = N
        while row >= 0:
            # 빈칸, 돌 제외 리스트에 담다가
            if arr[row][col] != -7 and arr[row][col] != -1:
                lst.append(arr[row][col])
                arr[row][col] = -7

            # 돌이 나타나면 > 밑에서부터 채우기
            elif arr[row][col] == -1:
                for put_r in range(len(lst)):
                    arr[last_rock - 1 - put_r][col] = lst[put_r]
                lst = []
                last_rock = row
            row -= 1

        # 돌 윗부분 처리 안 된 경우
        if len(lst) > 0:
            for put_r in range(len(lst)):
                arr[last_rock - 1 - put_r][col] = lst[put_r]

# 3. 반시계 회전하기
def rotation():
    global arr

    new_arr = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_arr[row][col] = arr[col][N-1-row]

    arr = new_arr


## 실행
ans = 0
status = True
while status:
    status = find()
    gravity()
    rotation()
    gravity()

print(ans)

