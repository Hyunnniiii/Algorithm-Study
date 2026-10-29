

# 1. 플레이어들 한 칸씩 이동.
# 이동했을 때 해당 칸을 독점계약. 계약은 k만큼의 턴 동안만 유효
# 각 플레이어마다 이동 우선순위가 있다.
# 인접 상하좌우 중 아무도 계약하지 않은 곳 선택 > 없다면 내가 계약한 곳으로
# 갈 수 있는 곳이 여러 곳이면, 이동 우선순위를 따른다
# 2. 내가 이동한 방향이 그 다음 보는 방향이 된다.
# (상하좌우 다 다른 사람이 계약하는 경우? 없음 왜냐면 내가 그 전에 있던 곳이 무조건 하나 있음)
# 3. 모두 이동한 뒤에 한 칸에 여러명이 오면, 작은 번호의 사람만 살아남는다
# 구할 것: 1번 플레이어만 살아남을 때까지 걸리는 시간. 답이 1000 이상이면 -1

# 입력으로 주는 것: n, m, k / 플레이어 위치 포함된 arr / 플레이어별 초기 방향 / 플레이어 이동 순위

# 플레이어들 모두 이동시킨 뒤에, 그 다음 단계 진행
# 사라진 플레이어에 대한 계약도 계속 유지되는가? -> yes
# 이동과 계약일수 갱신을 따로 해야하는데 같이 하고 있었음
# 1차 제출 > 틀림. 왜지? 혹시.. 계약 시간 갱신 시점이 틀린건가 > 아님. 모르겠음
# 설마.. 이거 기존 방향으로 가는게 아니라 무조건 우선순위 빙향 탐색?

# import pprint

## 입력 받기
N, M, K = map(int, input().split())
arr = [list(map(lambda x : [int(x)], input().split())) for _ in range(N)]     # 플레이어들의 격자상 위치
player = {}     # 플레이어 별 위치
contract = [[[0,0] for _ in range(N)] for _ in range(N)]    # 계약자, 유효한 일수 표시
cur_d = list(map(lambda x: int(x)-1, input().split()))    # 플레이어들의 방향 정보
dir_like = [list(map(lambda x:int(x)-1, input().split())) for _ in range(4*M)]  # 방향 우선순위

# 초기 위치 설정
for r in range(N):
    for c in range(N):
        if arr[r][c][0] != 0:
            contract[r][c] = [arr[r][c][0], -K]
            player[arr[r][c][0]] = [r, c]
        if arr[r][c][0] == 0:
            arr[r][c].remove(0)

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 함수: 범위 체크
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 함수: 어떤 사람의 좌표와 번호가 주어지면, 이동을 수행한다
def move():
    for p in player:
        if player[p] != [-1, -1]:
            si, sj, idx = player[p][0], player[p][1], p

            # 탐색할 방향의 순서: 4*(idx-1) + cur_d 행임
            woosun = dir_like[4*(idx-1) + cur_d[idx-1]][:]
            cnt = 0
            for k in woosun:
                ni, nj = si + di[k], sj + dj[k]

                if in_range(ni, nj) and contract[ni][nj] == [0,0]:
                    arr[ni][nj].append(idx)
                    arr[si][sj].remove(idx)
                    player[idx] = [ni, nj]
                    cur_d[idx-1] = k
                    break

                else:
                    cnt += 1

            # 4개 방향 모두 안되면 > 그냥 내 칸으로 가야함
            if cnt == 4:
                for k in woosun:
                    ni, nj = si + di[k], sj + dj[k]

                    if in_range(ni, nj) and contract[ni][nj][0] == idx:
                        arr[ni][nj].append(idx)
                        arr[si][sj].remove(idx)
                        player[idx] = [ni, nj]
                        cur_d[idx-1] = k
                        break
    # print('이동완료')
    # pprint.pprint(arr)
    # pprint.pprint(contract)
    # print('==================')

    ## M명 모두 이동한 이후 진행
    # [3] 2명 이상인 칸이 있는지 확인 > 번호 작은 1명만 남긴다
    for row in range(N):
        for col in range(N):
            if len(arr[row][col]) >= 2:
                arr[row][col].sort()
                remove_lst = arr[row][col][1:]      # 없앨 사람들
                arr[row][col] = arr[row][col][:1]   # 최소 번호인 사람만 남긴다

                for people in remove_lst:
                    player[people] = [-1,-1]

    # print('정리완료')
    # pprint.pprint(arr)
    # pprint.pprint(contract)
    # print('==================')

    # [4] 계약 일수 처리하기
    for row in range(N):
        for col in range(N):
            # 이미 계약된 곳들 하루 반영해주고
            if contract[row][col] != [0,0]:
                contract[row][col][1] += 1

                # 0되면 계약 종료
                if contract[row][col][1] == 0:
                    contract[row][col] = [0,0]

            # 새로 옮긴 곳 계약하기
            if arr[row][col] != []:
                contract[row][col] = [arr[row][col][0], -K]

    # print('계약처리완료')
    # pprint.pprint(arr)
    # pprint.pprint(contract)
    # print('==================')

## 실행하기
time = 0
while True:
    # 시간 체크하기
    time += 1

    # 1000번 해도 안되면 포기
    if time >= 1000:
        time = -1
        break

    # 플레이어 움직이고, 계약하기
    move()

    # 1번만 남았는지 확인하기
    ans = 0
    for p in player:
        if player[p] == [-1,-1]:
            ans += 1
    if ans == M-1:
        break

print(time)
