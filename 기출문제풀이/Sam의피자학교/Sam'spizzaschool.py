
''' Sam의 피자학교 / 20260909 / 체감 난이도 : 골드 3
소요 시간:  / 시도: 1회 / 실행 시간: 207ms (코드트리) / 메모리: 20MB

[타임라인]
09:04 - 09:26(22분) 문제 읽기 / 입력 받기 / 구상
09:26 - 11:10 (104분) 구현
11:10 - 11:13 (3분) 주석에 써둔 것 코드에 반영했는지 확인, 제출

[구상]
    - 문제에서 말하는 '인접한 밀가루'라는게 잘 이해되지 않았다. 너무 bfs에 익숙해져서 그런가
    당연히 나 자신의 칸을 기준으로 상하좌우 4개 칸이라고 처음에 해석했다. 물론 문제에서 제시한
    예제를 보면서 아니라는 것을 깨달았다.
    >> 근데 이걸 구현하면서 또 까먹어가지고 문제 또 읽음. 지금 보니 주석에 안적었는데 내가
    헷갈렸던 부분들도 정말 빼놓지 않고 주석에 써야겠다.
    - 문제에서 '두번 반 접기' 이래서 처음에 2.5번 접으라는줄 알았는데 두번 반(으로) 접는거였다. 황당

[구현]
    - 도우 말기에서 가장 많은 시간이 걸렸는데, 내가 찾아낸 규칙으로 구현하려 하다보니 인덱상에서
    너무 헷갈렸다.
    - 구현을 함수 단위로 하다보니 생긴 문제점: 피자 배열의 차원이 계속 1차원 > 2차원을 넘나들다 보니
    함수 실행 후 배열의 차원이 그 다음 함수의 인풋과 달라짐. 함수에서 들어가고 나오는 자료형을 미리 구상단계에서
    정해놔야 겠다
    - 어떤 단계 구현할 때 내가 주석에 적었던 해당 단계의 주의사항들 구현 시작하는 부분에 붙여넣고 보면서 구현하면
    실수를 어느정도 방지할 수 있을 것 같다


---------------------------------------------------------
# [개선]
- 도우 말기 아예 다른 방식으로

# ======================='''

# 1. 밀가루 양이 가장 작은 위치에 1씩 더하기. 여러 위치라면 모두 적용
# 2. 도우 말기
# 제일 왼쪽의 요소를 시계 90도 돌려서 위에 추가
# 바닥보다 위의 너비가 더 넓으면 중단
# 3. 도우 누르기
# 인접한 상하좌우 확인 후 계산, '동시에'
# 1자로 펴기. 열 작은 것 > 행 큰 것 순서대로
# 4. 도우 반으로 2번 접기
# 왼쪽을 180도 회전에서 위에 추가
# 5. 도우 누르기 (3번과 동일)

# 구할 것: 밀가루 양의 최대-최소가 k이하가 되는 최소 연산 횟수

## 입력 받기
N, K = map(int, input().split())
pizza = [list(map(int, input().split()))]

# 인접 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]


# 함수 1: 최소값에 밀가루 1 추가
def put():
    global pizza
    new_pizza = []
    for row in pizza:
        find = min(row)
        for x in row:
            if x == find:
                new_pizza.append(x+1)
            else:
                new_pizza.append(x)
    pizza = new_pizza


# 함수 2: 도우 말기
# 실행 전 1차원에 대한 처리 따로 해줘야 한다
# 0행의 길이만큼 열을 앞에서부터 선택.
# 선택한 열의 개수만큼 앞에 빈 행을 추가
# 선택한 열들에서 열 크고, 행 작은 순으로 선택한 뒤 집어넣기
def roll():
    global pizza

    while True:
        new_pizza = []
        zero_col_len = len(pizza)
        zero_row_len = len(pizza[0])

        # 진행 가능한지 확인
        if zero_col_len > len(pizza[zero_col_len-1]) - zero_row_len:
            break

        for _ in range(zero_row_len+1):
            new_pizza.insert(0, [])

        for col in range(zero_row_len):
            for row in range(zero_col_len-1, -1, -1):
                new_pizza[col].append(pizza[row][col])

        for idx in range(zero_row_len, len(pizza[zero_col_len-1])):
            new_pizza[len(new_pizza)-1].append(pizza[zero_col_len-1][idx])

        pizza = new_pizza


# 함수 3: 도우 누르기
# 빈 공간 0으로 채워주고, 인접한 0이 아닌 숫자들에 대해 계산 진행
def push():
    global pizza

    # 빈 공간 0으로 채우기
    new_pizza = []
    zero_col_len = len(pizza)
    to_fill = len(pizza[zero_col_len - 1])

    for row in pizza:
        new_pizza.append(row + [0] * (to_fill - len(row)))

    pizza = new_pizza

    # 계산 수행 > 동시에
    calculate = [[0] * to_fill for _ in range(zero_col_len)]
    visit = set()

    for row in range(zero_col_len):
        for col in range(to_fill):
            if pizza[row][col] > 0:
                visit.add((row, col))
                imsi_lst = []
                for k in range(4):
                    nr, nc = row + di[k], col + dj[k]

                    if 0 <= nr < zero_col_len and 0 <= nc < to_fill:
                        if pizza[nr][nc] > 0 and ((nr, nc) not in visit):
                            imsi_lst.append((pizza[nr][nc], nr, nc))

                # 임시리스트에 있는 값들로 계산 시작
                for cnt, r, c in imsi_lst:
                    apply = abs(pizza[row][col] - pizza[r][c]) // 5

                    if pizza[row][col] > pizza[r][c]:
                        calculate[row][col] -= apply
                        calculate[r][c] += apply
                    else:
                        calculate[row][col] += apply
                        calculate[r][c] -= apply

    # 모두 계산했으면 반영
    for row in range(zero_col_len):
        for col in range(to_fill):
            pizza[row][col] += calculate[row][col]

    # 1차원으로 펴기
    new_pizza = []

    for col in range(to_fill):
        for row in range(zero_col_len-1, -1, -1):
            if pizza[row][col] != 0:
                new_pizza.append(pizza[row][col])

    pizza = new_pizza


# 함수 4: 도우 두번 반 접기
def fold():
    global pizza

    length = len(pizza)
    new_pizza = [[], []]

    # 첫번째 접기
    for idx in range(length // 2 - 1, -1, -1):
        new_pizza[0].append(pizza[idx])
    for idx in range(length // 2, length):
        new_pizza[1].append(pizza[idx])
    pizza = new_pizza

    new_pizza = [[], [], [], []]
    length = len(pizza[0])
    row_len = len(pizza)

    # 두번째 접기
    for idx in range(length // 2 - 1, -1, -1):
        new_pizza[0].append(pizza[1][idx])
    for idx in range(length // 2 - 1, -1, -1):
        new_pizza[1].append(pizza[0][idx])
    for idx in range(length // 2, length):
        new_pizza[2].append(pizza[0][idx])
    for idx in range(length // 2, length):
        new_pizza[3].append(pizza[1][idx])
    pizza = new_pizza


## 실행
ans = 0
while True:
    ans += 1

    put()

    # 첫번째만 처리 따로
    new_pizza = [[],[]]
    new_pizza[0].append(pizza[0])
    new_pizza[1] = pizza[1:]
    pizza = new_pizza

    roll()
    push()
    fold()
    push()

    # 최대 - 최소 확인
    check = max(pizza) - min(pizza)
    if check <= K:
        print(ans)
        break
    pizza = [pizza]











