""" 나무 타이쿤 / 20260916 / 체감 난이도: 실버
소요 시간 30분 / 시도 1회 / 실행 시간 98ms (코드트리) / 메모리 19MB (코드트리)

문제에서 많이 낚여본 경험이 날 살렸다.
이 문제에서 제일 중요한 건 영양제 투입 먼저 진행 후 처리한 뒤에,
인접 대각선 한번에 탐색하고, 모아서 처리해야 되는 것이라고 생각한다.
실제로 문제에서 그래야 한다고 이야기를 많이 안하기도 했고..
사실 구상 단계에서 그걸 주의해야 한다는 것을 알아차리지 못했는데;;
구현하다보니 떠올랐다. 이거 이러면 안되지 않나? 라고..
그리고 처음엔 영양제의 위치도 배열에 표시하려 했는데, 생각해보니 그러려면 항상
배열 탐색해야 되니까 비효율적이겠다라는 생각이 들어서 구현 중 리스트에 좌표 담는 형식으로
바꿨다. set으로도 할까 했는데 .. 일단 리스트로 풀었다. set도 해보겠슨
> 엥? set으로 했는데 실행시간 늘어남
   ㄴ> 원소 수가 적어 set의 O(1) 탐색 이득보다 해싱·삽입 비용이 더 커서 오히려 느려질 수 있음.

"""

# [1] 특수 영양제 이동 규칙에 따라 이동
# 초기 위치: 좌하단 4칸
# 격자의 행, 열은 끝이 연결되어 있다

# [2] 특수 영양제 투입 후 사라짐
# 특수 영양제 있는 곳의 높이 +1 (나무가 없어도 +1)
#투입 후 영양제 삭제

# [3] 대각선 살피기
# 2에서 특수영양제 투입한 곳에 한해
# 대각선으로 인접한 곳에 높이가 1 이상인 나무 개수만큼 높이 더 성장
# 여기에선 격자 벗어나면 취급 안함

# [4] 나무 자르기
# 영양제 투입한 땅 제외, 높이 2 이상인 나무는 높이 -2 해주고,
# 그 자리에 영양제 투입

# 구할 것: 모든 턴이 지난 뒤 남아있는 높이의 총합
# ==============================================

# 0. 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

# 1. 영양제 이동
def move(d, p):
    global nutrient

    new_nutrient = []
    # 영양제 리스트에 있는 좌표들을 d방향으로 p칸 이동해서 새 리스트에 넣어준다
    for coord in nutrient:
        nr, nc = (coord[0]+dr[d]*p)%N, (coord[1]+dc[d]*p)%N
        new_nutrient.append((nr, nc))

    nutrient = new_nutrient

# 2. 영양제 투입 & 인접 계산
def give():

    # 일단 영양제 좌표에 해당하는 곳 나무 길이 +1
    for coord in nutrient:
        arr[coord[0]][coord[1]] += 1

    # 대각선에 높이 1 이상인 나무 확인 후 더해주기
    # 위의 과정 마친 후에 진행 (왜냐면 0이었다가 영양제 맞고 1되면 그거 인접으로 칠 수 있음)
    # 그리고 대각선 판정도 바뀔 수 있으니 임시 배열 활용
    imsi = [[0]*N for _ in range(N)]
    for coord in nutrient:
        for k in range(4):
            nr, nc = coord[0] + dr[k*2+1], coord[1] + dc[k*2+1]

            # 여기에선 범위체크
            if in_range(nr, nc) and arr[nr][nc] >= 1:
                imsi[coord[0]][coord[1]] += 1
    # 위의 과정 다 마치면 임시 배열 내 숫자 더해주기
    for r in range(N):
        for c in range(N):
            if imsi[r][c] == 0:
                continue
            arr[r][c] += imsi[r][c]


# 3. 높이 2 이상인 나무 자르기 & 영양제 올리기
def cut():
    global nutrient

    new_nutrient = []
    for r in range(N):
        for c in range(N):
            # 높이 2 이상, 영양제 투입한 땅 제외
            if arr[r][c] >= 2 and (r,c) not in nutrient:    # 이 탐색이 좀 맘에 걸리네
                arr[r][c] -= 2      # 나무 자르고
                new_nutrient.append((r,c))  # 영양제 올리기

    # 새로운 영양제 위치
    nutrient = new_nutrient


# =================================
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
nutrient = []   # 영양제의 좌표 여기에 보관

# 초기에 좌하단 4군데에 영양제 투입
nutrient.append([N-1, 0])
nutrient.append([N-1, 1])
nutrient.append([N-2, 0])
nutrient.append([N-2, 1])

# 8방향
dr = [0,-1,-1,-1,0,1,1,1]
dc = [1,1,0,-1,-1,-1,0,1]

# 실행
for _ in range(M):
    d, p = map(int, input().split())

    # 1. 영양제 이동
    move(d-1, p)

    # 2. 영양제 투입, 인접 나무 살피기
    give()

    # 3. 나무 자르고 영양제 추가
    cut()

print(sum(map(sum, arr)))

