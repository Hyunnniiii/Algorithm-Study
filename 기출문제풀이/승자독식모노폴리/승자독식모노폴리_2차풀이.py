
""" 승자독식 모노폴리 / 20260929 허리 아픔 / 체감 난이도: 골드5
소요 시간 68분 / 시도 1회 / 실행 시간 298ms (코드트리) / 메모리 23MB (코드트리)



"""

# 19:12~ 손구상 19:24 ~ 주석 구상 19:35 ~ 20:20 제출

# 구할 것: 1번 플레이어만 남기까지 걸리는 턴 수 (1000 이상이면 -1)
# 방향은 플레이어 번호 순으로 주어진다고 가정

def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

def debug_print():
    if DEBUG:
        print('플레이어 위치 확인')
        for row in arr:
            print(row)
        print()
        print('독점 계약 확인')
        for row in brr:
            print(row)
        print()

#####################
DEBUG = False
N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
brr = [[[] for _ in range(N)] for _ in range(N)]    # [계약자, 계약일] 표시
player = {}     # {idx : [행, 열, 현재 방향]}
for row in range(N):
    for col in range(N):
        if arr[row][col] != 0:
            player[arr[row][col]] = [row, col]
            brr[row][col] = [arr[row][col], -Q]

d_lst = [0] + list(map(int, input().split()))
for idx in range(1, M+1):
    player[idx].append(d_lst[idx])

# priority[idx][현재 방향] = [우선순위 4개]
dir_priority = [None] * (M+1)
for idx in range(1, M+1):
    dir_priority[idx] = [None]

    for _ in range(4):
        dir_priority[idx].append(list(map(int, input().split())))


# 상하좌우
dr = [None, -1,1,0,0]
dc = [None, 0,0,-1,1]


dead_player = set()
for time in range(1, 1001):
    # 시간 1000되면 종료 처리
    if time == 1000:
        print(-1)
        break

    # 임시 배열 만들기
    imsi = [[0]*N for _ in range(N)]

    # 플레이어 딕 순회하면서 해당 위치에서 4개 방향 본인 현재 방향과 우선순위에 따라 탐색
    for idx in player.keys():
        if idx in dead_player:
            continue

        sr, sc, sd = player[idx]
        status = False  # 옮길 위치 정했는가?

        for nd in dir_priority[idx][sd]:
            nr, nc = sr + dr[nd], sc+dc[nd]

            if not in_range(nr,nc):
                continue
            if brr[nr][nc] != []:
                continue

            # 여기까지 오면 갈 수 있는거
            player[idx] = [nr, nc, nd]
            # brr[nr][nc] = [idx, -Q]
            status = True
            break

        if not status:
            for nd in dir_priority[idx][sd]:
                nr, nc = sr + dr[nd], sc+dc[nd]

                if not in_range(nr, nc):
                    continue
                if brr[nr][nc][0] != idx:
                    continue

                player[idx] = [nr, nc, nd]
                break

        # 이러면 일단 정보는 다 변경함. 이제 그 자리에 다른 사람 있는지 확인
        if imsi[nr][nc] == 0:
            imsi[nr][nc] = idx

        elif imsi[nr][nc] != 0:
            # 내가 더 크다면
            if idx < imsi[nr][nc]:
                dead_player.add(imsi[nr][nc])
                imsi[nr][nc] = idx

            # 원래 있던 사람이 더 작으면
            elif idx > imsi[nr][nc]:
                dead_player.add(idx)

    arr = imsi

    # 독점 일수 갱신
    for row in range(N):
        for col in range(N):
            if not brr[row][col]:
                continue

            if brr[row][col][1] < -1:
                brr[row][col][1] += 1

            elif brr[row][col][1] == -1:
                brr[row][col] = []

    # 신규 독점 계약 반영
    for idx, val in player.items():
        if idx in dead_player:
            continue
        brr[val[0]][val[1]] = [idx, -Q]

    # 종료 조건 확인: 합이 1
    if sum(map(sum, arr)) == 1:
        print(time)
        break

    debug_print()
