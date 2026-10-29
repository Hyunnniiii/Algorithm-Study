
''' 루돌프의 반란 / 20260916 / 체감 난이도 : 골드 3
소요 시간: 4h+ / 시도: 3회 / 실행 시간: 98ms (코드트리) / 메모리: 19MB

[선정 사유]
- 산타가 충돌하는 상황 vs 루돌프가 충돌하는 상황을 명확하게 나눔
- 산타가 연쇄적으로 밀려나는 상황을 하나의 함수로 통합해서 관리
- 딕셔너리를 활용해서 탈락한 산타 관리가 쉬움
- 직관적인 변수명, 깔끔 clean한 함수와 실행부

[시간 복잡도]
- K(P+ P^2 + N^2)
    - K: loop 횟수
    - P: 루돌프의 이동 ~ 살아있는 산타 탐색 시 최악의 경우
    - P^2: 산타의 이동 ~ P명의 산타 이동 시 P번 충돌 발생하는 최악의 경우
    - N^2: 점수 추가

[엣지 케이스]
4 2 2 1 2
1 4
1 3 3
2 4 3

정답: 4 0
사유: 산타가 루돌프를 때려서 튕겨나오고, 다른 산타와 상호작용을 할 때, 반전시킨 방향 벡터를 넘겨주지 않으면 값이 다르게 나옴.

'''

## 범위 쳌
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


## 루돌프 움직이기
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


## 산타 움직이기
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


## 루돌충돌
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


## 산타충돌
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


## 상호작용
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


## 실행
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


















