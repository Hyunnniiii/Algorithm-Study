
""" 마법의 숲 탐색 / 20261006 / 체감 난이도: 골드
소요 시간 63분 / 시도 1회 / 실행 시간 369ms (코드트리) / 메모리 25MB (코드트리)

패딩해야 된다는걸 알고 푸니까 금방 풀었다.
그리고.. 진심 다시 읽어도 될 때까지 그 방향으로 내려가라는 것처럼 보임

중간에 bfs하면서 출구 좌표 어케 찾지 생각하다가
중심 좌표도 같이 들고 다녀야 하나? 추가하기 귀찮은데.. (1차 때 그렇게 풀었음)
귀찮아하다가 갑자기 아이디어 생각나서 내가 해냄
중력 마스터가 되는 그날까지

"""

# 09:35 ~
# 구할 것: 정령 최종 행 위치 총합
# ======================
from collections import deque


def in_range(row, col):
    return 0<=row<R+3 and 0<=col<C


def move(r, c):
    Q = deque()
    Q.append((r,c))
    visit = [[0]*C for _ in range(R+3)]
    visit[r][c] = 1
    max_row = -float('inf')

    while Q:
        sr, sc = Q.popleft()
        my_idx = arr[sr][sc]

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if not in_range(nr, nc) or visit[nr][nc]:
                continue
            if arr[nr][nc] == 0:
                continue
            if arr[nr][nc] == my_idx:
                Q.append((nr, nc))
                visit[nr][nc] = 1
                max_row = max(max_row, nr)

            if arr[nr][nc] != my_idx:
                my_exit = exit_info[my_idx]

                hubor = nr + dr[(my_exit+2)%4]
                huboc = nc + dc[(my_exit+2)%4]

                if arr[hubor][huboc] == my_idx:
                    Q.append((nr, nc))
                    visit[nr][nc] = 1
                    max_row = max(max_row, nr)
    return max_row


def debug_print(msg):
    if DEBUG:
        print('==', msg, '==')
        print('배열 상황')
        for row in arr:
            print(row)
        print()
        print('방향 정보')
        print(exit_info)
        print()


####################
DEBUG = True
R, C, K = map(int, input().split())
arr = [[0]*C for _ in range(R+3)]
exit_info = {}  # {idx : d}

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 상대좌표 저장
scan = {'S' : [(2,0), (1,-1), (1,1)],
        'W' : [(-1,-1), (0,-2), (1,-1), (1,-2), (2,-1)],
        'E' : [(-1,1), (0,2), (1,1), (1,2), (2,1)]}

# 실행부
ans = 0
for idx in range(1, K+1):
    col, exit_d = map(int, input().split())
    col -= 1
    exit_info[idx] = exit_d

    # [1] 골렘 이동
    coord = [[0,col], [1, col], [1, col-1], [1, col+1], [2, col]]

    while True:
        # 남쪽
        status = True
        x, y = coord[1][0], coord[1][1]
        for dx, dy in scan['S']:
            nx, ny = x + dx, y + dy
            if nx >= R+3 or not (0<=ny<C):
                status = False
                break
            if arr[nx][ny] > 0:
                status = False
                break

        if status:
            for cnt in range(len(coord)):
                coord[cnt] = [coord[cnt][0]+1, coord[cnt][1]]
            continue

        # 서쪽
        status = True
        x, y = coord[1][0], coord[1][1]
        for dx, dy in scan['W']:
            nx, ny = x + dx, y + dy
            if nx >= R+3 or not (0<=ny<C):
                status = False
                break
            if arr[nx][ny] > 0:
                status = False
                break

        if status:
            for cnt in range(len(coord)):
                coord[cnt] = [coord[cnt][0]+1, coord[cnt][1]-1]
            exit_info[idx] = (exit_info[idx]-1)%4
            continue

        # 동쪽
        status = True
        x, y = coord[1][0], coord[1][1]
        for dx, dy in scan['E']:
            nx, ny = x + dx, y + dy
            if nx >= R+3 or not (0<=ny<C):
                status = False
                break
            if arr[nx][ny] > 0:
                status = False
                break

        if status:
            for cnt in range(len(coord)):
                coord[cnt] = [coord[cnt][0]+1, coord[cnt][1]+1]
            exit_info[idx] = (exit_info[idx] + 1) % 4
            continue

        # 여기까지 온다면 못 움직이는 것
        break

    # 해당 위치에 골렘 표시하기
    for x, y in coord:
        arr[x][y] = idx

    debug_print('골렘 내려오기 완료')

    # 튀어나왔는지 확인
    stop = False
    for row in range(0, 3):
        for col in range(C):
            if arr[row][col] > 0:
                stop = True
                break
        if stop:
            break

    if stop:
        arr = [[0]*C for _ in range(R+3)]
        continue

    # [2] 정령 이동
    max_row = move(coord[1][0], coord[1][1])
    ans += (max_row-2)

    debug_print('정령 이동')
    print('max row는 :', max_row-2)

print(ans)