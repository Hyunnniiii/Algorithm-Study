""" 싸움땅 / 20260910 / 체감 난이도: G5

[선정 사유]
- 깔끔 clean한 분기처리와 실행부
- 변수명이 맘에듦
- 문제에서 시키는 대로 착하게 잘 구현

[시간 복잡도]
- K * M^2 (K: 라운드 수, M: 플레이어 수)

[엣지 케이스]

3 2 2
0 5 12
0 0 0
0 0 0
2 2 0 2
1 1 1 7
에지 사유: 총 공격력과 초기 능력치의 합이 같을 때, 초기 능력치가 높은 사람이 승리하는 로직을 넣지 않은 경우 오답
정답: 9 0

"""

# 상우하좌
di = [-1,0,1,0]
dj = [0,1,0,-1]

# 범위
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 플레이어 이동하기
def move(idx):
    cur_r = player_loc[idx][0]
    cur_c = player_loc[idx][1]
    cur_d = player_info[idx][2]

    nr, nc = cur_r + di[cur_d], cur_c + dj[cur_d]

    # 격자를 벗어나면 방향 반대로 바꾸고, 딕에 반영, nr/nc 수정
    if not in_range(nr, nc):
        cur_d = (cur_d+2)%4
        player_info[idx][2] = cur_d
        nr, nc = cur_r + di[cur_d], cur_c + dj[cur_d]

    # 이동한 곳 일단 딕에 반영
    player_loc[idx] = [nr, nc]

    # 이동한 곳에 플레이어가 있는지, 없는지에 따라 분기
    fight = False   # 싸워야 하는지?
    who_idx = -100  # 누구와 싸워야 하는지?
    for p in player_loc:
        if player_loc[p] == [nr, nc] and p != idx:
            who_idx = p
            fight = True
            break

    return who_idx, fight

# 싸울 일 없을 때
def no_fight(idx):
    cur_r = player_loc[idx][0]
    cur_c = player_loc[idx][1]
    cur_gun = player_info[idx][1]

    # 현재 위치한 칸에 총이 없으면 > 아무 일도 일어나지 않음
    if gun[cur_r][cur_c] == []:
        return

    # 총이 있을 때.
    # 내가 0이었다면 그냥 가질래: 내꺼 딕 업데이트 해주고, 배열에서 해당 총 삭제
    if cur_gun == 0:
        to_see = max(gun[cur_r][cur_c])
        player_info[idx][1] = to_see
        gun[cur_r][cur_c].remove(to_see)

    # 내가 0이 아니었다면: 비교 후 내꺼랑 교체.
    else:
        to_see = max(gun[cur_r][cur_c])
        if cur_gun < to_see:
            gun[cur_r][cur_c].append(cur_gun)
            player_info[idx][1] = to_see
            gun[cur_r][cur_c].remove(to_see)

# 싸워야 할 때
def start_fight(other_idx, my_idx):
    print('====', my_idx, other_idx,'싸워')
    my_strength = player_info[my_idx][0]
    my_gun = player_info[my_idx][1]

    other_strength = player_info[other_idx][0]
    other_gun = player_info[other_idx][1]

    # 상대방의 정보와 비교하기, 포인트 획득
    # 각 플레이어의 초기 능력치 모두 다르므로, 비교 불가한 상황은 발생하지 않음
    if my_strength + my_gun > other_strength + other_gun:
        winner, loser = my_idx, other_idx
        point[winner] += (my_strength + my_gun)-(other_strength + other_gun)
    elif my_strength + my_gun < other_strength + other_gun:
        winner, loser = other_idx, my_idx
        point[winner] += (other_strength + other_gun)-(my_strength + my_gun)
    elif my_strength + my_gun == other_strength + other_gun:
        if my_strength > other_strength:
            winner, loser = my_idx, other_idx
            point[winner] += (my_strength + my_gun) - (other_strength + other_gun)
        else:
            winner, loser = other_idx, my_idx
            point[winner] += (other_strength + other_gun) - (my_strength + my_gun)

    # 패자 먼저 처리
    # 1. 나의 총 반납한다
    cur_r, cur_c, cur_d = player_loc[loser][0], player_loc[loser][1], player_info[loser][2]
    if player_info[loser][1] != 0:
        gun[cur_r][cur_c].append(player_info[loser][1])
    player_info[loser][1] = 0

    # 2. 내 방향대로 이동한다 > 범위 밖이거나 사람이 있으면 회전하면서 빈칸 보이면 간다
    nr, nc = cur_r + di[cur_d], cur_c + dj[cur_d]

    if not in_range(nr, nc) or [nr, nc] in player_loc.values():
        while True:
            cur_d = (cur_d + 1) % 4
            nr, nc = cur_r + di[cur_d], cur_c + dj[cur_d]

            if in_range(nr, nc) and [nr, nc] not in player_loc.values():
                player_info[loser][2] = cur_d
                break

    # 3. 이동한 곳으로 정보 변경, 그 곳에 총 있으면 획득, 아니면 아무일 X
    player_loc[loser] = [nr, nc]
    no_fight(loser)

    # 승자 처리
    no_fight(winner)


# ===========================================
N, M, K = map(int, input().split())
gun = [list(map(lambda x : [int(x)], input().split())) for _ in range(N)]
player_loc = {}     # player: (row, col)
player_info = {}    # player: (능력치, 총 공격력, 방향)
point = [0]*(M+1)   # 1번 인덱스부터 사용

for idx in range(1, M+1):
    x, y, d, s = map(int, input().split())
    player_info[idx] = [s, 0, d]
    player_loc[idx] = [x-1, y-1]

for row in range(N):
    for col in range(N):
        if gun[row][col] == [0]:
            gun[row][col].clear()

for round in range(K):
    for player in player_info:
        # 누구랑 싸울지, 싸우긴 할건지?
        who, fight = move(player)

        # 싸워야 한다면 > 싸워
        if fight:
            start_fight(who, player)

        # 안싸워도 되면 > 싸우지마~~
        else:
            no_fight(player)

    print(point)
