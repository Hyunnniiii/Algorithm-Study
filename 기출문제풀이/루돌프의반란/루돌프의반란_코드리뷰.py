
''' 루돌프의 반란 / 20260916 / 체감 난이도 : 골드 3
소요 시간: 4h+ / 시도: 3회 / 실행 시간: 98ms (코드트리) / 메모리: 19MB

[타임라인]
09:00 - 09:36(36분) 문제 읽기 / 입력 받기 / 구상
09:36 - 12:01 (140분) 구현, 디버깅, 1차 제출 (중간에 5분 휴식)
12:01 - 디버깅

[구상]
- 일단 제목과 본문을 보고 호감이었다. 왜냐면 재미있음. 뭔가 기분 좋고 풀 수 있을 것만 같은 산뜻한 느낌으로 시작했다
- 구상을 평소에 비해 오래했다. 왜냐면 뭔가 이전에 비해 큰그림이 조금 그려졌다. 그리고 주의해야 할 것들을 이미
인지하고 있음에도 일부러 빨간펜으로 또 썼다. 난 까먹으니까
- 자료구조 선택은 잘한 것 같다.

[구현]
- 구현하면서 느낌 좋았다.
왜냐면 지금 내가 쓰고 있는 변수명: 직관적이라 좋음, 함수: 단계 딱 나눠져서 좋음,
오픈 테케와 똑같이 내가 원하는 대로 중간 결과 다 잘나오고 구현하면서 막히는 부분도 딱히 없었다
- 진심 풀면서 난 오늘 이거 무조건 풀겠다~~ 라는 생각이 들었음.
싸움땅, 포탑 부수기 풀 때의 느낌이 왔다.
- 솔직히 구현 자체는 나쁘지 않았음. 완성한 내 코드 정말 맘에 듦. 튜플 비교도 활용해봤고, 디버깅하기에도
어렵지 않은 코드
- 근데.. 왜저렇게 오래걸렸지? .. 영상으로 확인할거임

[디버깅]
- 일단 1차 틀림에서 내가 방향에 대한 것을 혼동하고 있음을 빠르게 파악할 수 있었다.
산타가 움직여서 부딫히면 그 방향의 반대로 튕겨나가고, 루돌프가 움직여서 부딫히면 그 방향 그대로 튕겨 나가는건데,
그거에 대한 처리는 괜찮았으나 튕겨나간 뒤 산타끼리 또 부딫힐 때의 함수를 내가 상황에 따라 분리하지 않고
interaction이라는 함수 하나로 통합했기 때문에 방향 정보에 대해 조금 더 신경 썼어야 했는데 그러지 않았다.
- 근데 뭔가 풀 수 있을거라는 욕심과 시간이 얼마 남지 않는 그 상황에서 정말 풀고 싶었기 때문에
방향 수정에서 한참 헤맸다.
- 아무튼 다 고치고 진짜 다 맞았다는 생각으로 제출했는데??? 또 틀림
여기서 뭐 틀렸는지 찾는데 정말 오래 걸렸다. 알고보니 내가 기절한 시간을 유지하지 않고 계속 바꾸고 있었다.
쩝...... 열받음

[후기]
- 돌아보니 나의 모든 실수가 interaction 함수에서 나왔다. 구현 막바지에 지친건지 흥분해서 그런건지 모르겠지만..
(본좌는 문제가 풀릴 것 같으면 심장이 두근댐) 마지막까지 정말 방심하지 말고, 투두리스트 제대로 체크하고,
내가 상태 변경하는 값이 정말 바꿔야 하는건지.. 내가 무슨 값을 다루고 있는지 체크 잘 해라

---------------------------------------------------------
[개선]
다른 사람들 코드 공부하기


> 1차 제출에서 놓친 것
: 산타가 움직여서 충돌했을 때 vs 루돌프가 움직여서 충돌했을 때 튕겨져나가는 방향이 반대인데, 이걸 생각 안했음
그리고 상호작용 함수에서 밀려나가다가 튕겨나간 산타를 죽음 처리 안함
interaction 함수에서 nr, nc = r, c 이 쥐 랄 함

> 2차 제출에서 놓친 것
interaction 함수에서 산타들 밀칠 때 기절한 사람들의 상태를 유지하지 않고 0으로 초기화하고 있었음!!!

'''

# [1] 루돌프 움직임
# 가장 가까운 산타를 향해 1칸 (8방향 중 하나 선택)
# 격자 안에 있는 산타에 대해서만 (기절 포함)
# 거리 작은 > 행이 큰 > 열이 큰

# [2] 산타 움직임
# 순서대로!! 움직인다
# 기절하지 않고, 격자 밖으로 나가지 않은 산타만 이동 가능
# 루돌프에게 가까워지는 방향으로 1칸
# 움직일 수 없거나, 루돌프와 가까워질 수 있는 방향 없다면 움직이지 않음
# 같은 거리에 대해서는 상우하좌 우선순위

# [3] 충돌
# 산타와 루돌프가 만나면 충돌.
# 루돌이 움직여서 충돌: 산타+C, 산타 C칸 밀려남
# 산타가 움직여서 충돌: 산타+D, 산타 D칸 밀려남
# 밀려난 위치 격자 밖이면 산타 탈락

# [4] 상호작용
# 방해물 없이 정확히 밀려나는 칸에 갈 수 있다
# 밀려난 칸에 산타가 있으면 연쇄적으로 1칸씩 밀려난다
# 이때 격자 밖으로 나가는 산타 탈락

# [5] 기절
# 산타는 루돌프와 충돌하면 기절, 그 다음 턴까지 기절 상태 유지
# 움직일 수 없으나, 충돌이나 상호작용으로 밀려날 수는 있다
# 기절한 산타도 마지막에 점수 더할 때 포함

# 두 칸 사이의 거리 : 제곱합임에 유의
# 행열 1부터 입력이므로 -1 해서 받기
# 움직일 수 없는 산타
# : 기절하거나 이미 격자 밖으로 나감, 더이상 루돌과 가까워질 수 없음, 이미 산타가 있는 칸, 격자 밖
# 산타 둘 다 루돌프와 충돌할 수 있다면? > 충돌로 밀려나는 것 먼저 처리하고, 그 다음 산타 이동
# ===========================================================
# 범위 쳌
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

# 루돌프 움직이기
def rudol_move():
    global rudol_r, rudol_c

    min_info, min_dist = (-1,-1,-1), float('inf')
    # 1. 가장 가까운 산타 찾기
    for idx, loc in santa_loc.items():
        dist = (rudol_r-loc[0])**2 + (rudol_c-loc[1])**2
        if dist < min_dist:
            min_dist = dist
            min_info = (loc[0], loc[1], idx)
        elif dist == min_dist:
            min_info = max((min_info[0], min_info[1]), (loc[0], loc[1]))

    # 2. 루돌프 인접 8방향 중 산타에게 가장 가까워지는 방향으로 돌진
    min_dist = float('inf')
    rudol_nr, rudol_nc, rudol_d = -1, -1, -1
    for k in range(8):
        nr, nc = rudol_r+dr[k], rudol_c+dc[k]

        # 범위 내면 갈 수 있음
        if in_range(nr, nc):
            dist = (min_info[0]-nr)**2 + (min_info[1]-nc)**2

            if dist < min_dist:
                min_dist = dist
                rudol_nr, rudol_nc, rudol_d = nr, nc, k

    rudol_r, rudol_c = rudol_nr, rudol_nc

    # 만약 충돌한 산타가 있다면 > 처리 해주세요
    if arr[rudol_r][rudol_c] != 0:
        rudol_attack(arr[rudol_r][rudol_c], rudol_d)

    return


# 2. 산타 움직이기
def santa_move(rudol_r, rudol_c):
    # 순서대로 4방향 중 루돌과 가장 가까워지는 곳을 찾아
    for idx in range(1, P+1):
        # 이미 죽은 산타 제외
        if idx not in santa_loc.keys():
            continue

        # 기절한 산타 제외
        if santa_loc[idx][2] != 0:
            continue

        sr, sc = santa_loc[idx][0], santa_loc[idx][1]
        min_dist = (rudol_r-sr)**2+ (rudol_c-sc)**2     # 원래 거리보단 가까워져야 함
        santa_nr, santa_nc, santa_d = sr, sc, -100


        for k in range(4):
            nr, nc = sr+dr[k*2], sc+dc[k*2]

            # 범위 내, 노 산타, 작은 거리
            if in_range(nr, nc) and arr[nr][nc] == 0:
                dist = (rudol_r-nr)**2 + (rudol_c-nc)**2

                if dist < min_dist:
                    min_dist = dist
                    santa_nr, santa_nc, santa_d = nr, nc, k*2

        # not 이동 > 제외
        if santa_d == -100:
            continue

        # 이동 > 정보 변경
        arr[santa_nr][santa_nc] = arr[sr][sc]
        arr[sr][sc] = 0
        santa_loc[idx] = [santa_nr, santa_nc, 0]

        # 만약 충돌했다면 > 처리 해주세요
        if santa_nr==rudol_r and santa_nc==rudol_c:
            santa_attack(idx, santa_d)


# 루돌충돌
def rudol_attack(idx, d):   # (충돌한 산타 인덱스, 루돌프가 온 방향)
    # 해당 산타 점수 얻기
    point[idx] += rudol_power

    # 산타 밀려나기
    sr, sc = santa_loc[idx][0], santa_loc[idx][1]
    nr, nc = sr + dr[d]*rudol_power, sc + dc[d]*rudol_power

    # 범위 밖이라면 > 너 삭제
    if not in_range(nr, nc):
        arr[sr][sc] = 0
        santa_loc.pop(idx)
        return

    # 다른 산타가 있다면 > 상호작용, 기절
    if arr[nr][nc] != 0:
        arr[sr][sc] = 0
        interaction(idx, nr, nc, d)
        return

    # 나만 있으면 > 위치 수정, 기절
    arr[nr][nc] = arr[sr][sc]
    arr[sr][sc] = 0
    santa_loc[idx] = [nr, nc, -2]

    return


# 산타충돌
def santa_attack(idx, d):  # (충돌한 산타 인덱스, 산타 온 방향)
    # 해당 산타 점수 얻기
    point[idx] += santa_power

    # 산타 밀려나기
    sr, sc = santa_loc[idx][0], santa_loc[idx][1]
    nr, nc = sr - dr[d]*santa_power, sc - dc[d]*santa_power

    # 범위 밖이라면 > 너 삭제
    if not in_range(nr, nc):
        arr[sr][sc] = 0
        santa_loc.pop(idx)
        return

    # 다른 산타가 있다면 > 상호작용으로 넘기기
    if arr[nr][nc] != 0:
        arr[sr][sc] = 0
        interaction(idx, nr, nc, (d+4)%8)
        return

    # 나만 있으면 > 위치 수정, 기절
    arr[nr][nc] = arr[sr][sc]
    arr[sr][sc] = 0
    santa_loc[idx] = [nr, nc, -2]

    return


# 상호작용
def interaction(idx, r, c, d):    # 날아온 산타 인덱스, 충돌 발생 위치, 방향
    # 처음 충돌한 지점 먼저 처리

    new_santa, ori_santa = idx, arr[r][c]
    santa_loc[new_santa] = [r, c, -2]
    arr[r][c] = new_santa

    # 충돌 발생 지점을 기준으로 d 방향으로 탐색
    # 언제까지? > 0이 나오거나, 경계 넘어갈 때까지
    while True:
        nr, nc = r+dr[d], c+dc[d]

        # 경계 넘어갔으면 > 밀려나간 이 사람은 뒤졌습니다. 끝
        if not in_range(nr, nc):
            santa_loc.pop(ori_santa)
            break

        # 0이면 > 처리해주고 끝
        if arr[nr][nc] == 0:
            santa_loc[ori_santa] = [nr, nc, santa_loc[ori_santa][2]]
            arr[nr][nc] = ori_santa
            break

        # 또다른 산타가 있다면 > 얘도 밀어
        if arr[nr][nc] > 0:
            new_santa, ori_santa = ori_santa, arr[nr][nc]
            santa_loc[new_santa] = [nr, nc, santa_loc[new_santa][2]]
            arr[nr][nc] = new_santa
            r, c = nr, nc

# ======================

N, K, P, rudol_power, santa_power = map(int, input().split())
rudol_r, rudol_c = map(lambda x : int(x)-1, input().split())
arr = [[0]*N for _ in range(N)]
santa_loc = {}  # 산타 위치 저장할 딕
for _ in range(P):
    idx, r, c = map(int, input().split())
    arr[r-1][c-1] = idx               # 산타 번호
    santa_loc[idx] = [r-1, c-1, 0]    # (산타 위치, 기절 유무)
point = [0]*(P+1)

# 방향 (위부터 시계방향으로)
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]


# 실행
for turn in range(1,K+1):

    # [1] 루돌프 이동
    rudol_move()

    # [2] 산타 이동
    santa_move(rudol_r, rudol_c)


    # [3] 산타 전부 탈락했는지 확인
    if sum(map(sum, arr)) == 0:
        break

    # [4] 탈락하지 않은 산타 점수 추가
    for r in range(N):
        for c in range(N):
            if arr[r][c] > 0:
                point[arr[r][c]] += 1

    # [5] 기절한 산타 깨우기
    for info in santa_loc.values():
        if info[2] < 0:
            info[2] += 1

print(*point[1:])


















