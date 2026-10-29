
'''
미생물 연구

[선정 사유]
- group_info, group_coord를 활용해 미생물의 크기, 투입 시간, 좌표를 잘 관리함
- 문제의 우선순위(작은 열, 큰 행)를 그대로 for문 순회 순서로 구현
- 정직함

[시간 복잡도]
Q * N^2 + Q*log(Q)

[엣지 케이스]
첨부

'''
from collections import deque

# [0] 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

# [1] BFS로 그룹 정보 확인하기
def get_cell_group_info():
    visit = [[0]*N for _ in range(N)]
    group_info = []     # (그룹 크기, 그룹 idx)
    group_coord = {}    # {idx: (그룹 좌표)}
    many_group = set()  # 2번 이상 나타난 그룹 idx 넣을거임

    for r in range(N):
        for c in range(N):
            if visit[r][c]:
                continue

            if arr[r][c] in group_coord.keys():
                many_group.add(arr[r][c])
                continue

            if arr[r][c] > 0:
                Q = deque()
                Q.append((r, c))
                visit[r][c] = 1
                group_coord[arr[r][c]] = [(r,c)]

                while Q:
                    sr, sc = Q.popleft()

                    for k in range(4):
                        nr, nc = sr+dr[k], sc+dc[k]

                        if not in_range(nr,nc) or visit[nr][nc]:
                            continue
                        if arr[nr][nc] != arr[r][c]:
                            continue

                        Q.append((nr,nc))
                        visit[nr][nc] = 1
                        group_coord[arr[r][c]].append((nr,nc))

                group_info.append((len(group_coord[arr[r][c]]), arr[r][c]))
    return group_info, group_coord, many_group


# [2] 배양 용기 이동
def move_cell():
    global arr
    imsi = [[0]*N for _ in range(N)]

    # 모든 그룹에 대해 순서대로 수행
    for size, idx in group_info:
        if idx in many_group:
            continue

        # 배열 좌하단부터 탐색
        status = True
        for col in range(N):
            for row in range(N-1,-1,-1):
                status = True

                # 모든 좌표가 들어갈 수 있는지 확인
                for r, c in group_coord[idx]:
                    r, c = r-group_coord[idx][0][0], c-group_coord[idx][0][1]
                    r, c = row+r, col+c

                    if not in_range(r,c):
                        status = False
                        break

                    if imsi[r][c] > 0:
                        status = False
                        break

                if not status:
                    continue

                # 여기로 오면 가능하다는 것
                for r, c in group_coord[idx]:
                    r, c = r-group_coord[idx][0][0], c-group_coord[idx][0][1]
                    r, c = row+r, col+c

                    imsi[r][c] = idx

                status = True
                break

            if status:
                break

    arr = imsi


# [3] 정산
def score():
    global ans

    near_group = set()  # 인접한 그룹쌍 저장용
    visit = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue

            if visit[r][c]:
                continue

            Q = deque()
            Q.append((r,c))
            visit[r][c] = 1

            while Q:
                sr, sc = Q.popleft()

                for k in range(4):
                    nr, nc = sr+dr[k], sc+dc[k]

                    if not in_range(nr,nc) or visit[nr][nc]:
                        continue
                    if arr[nr][nc] == 0:
                        continue

                    if arr[nr][nc] == arr[r][c]:
                        Q.append((nr,nc))
                        visit[nr][nc] = 1

                    if arr[nr][nc] != arr[r][c]:
                        near_group.add((min(arr[r][c], arr[nr][nc]), max(arr[r][c], arr[nr][nc])))

    for g1, g2 in near_group:
        ans += len(group_coord[g1]) * len(group_coord[g2])


def debug_print_arr(word):
    if DEBUG:
        print(word)
        print('현재 배열 상황')
        for row in arr:
            print(row)
        print()
DEBUG = False

###########################
N, Q = map(int, input().split())
arr = [[0]*N for _ in range(N)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for time in range(1, Q+1):
    r1, c1, r2, c2 = map(int, input().split())
    ans = 0     # 이번 턴의 점수

    # 새로 들어온 미생물 표시
    for row in range(N-c2, N-c1):
        for col in range(r1, r2):
            arr[row][col] = time

    # BFS로 그룹 정보 확인하기
    group_info, group_coord, many_group = get_cell_group_info()

    # 그룹 좌표 sort
    for coords in group_coord.values():
        coords.sort(key = lambda x : (-x[0], x[1]))

    # 그룹 정보 리스트 sort
    group_info.sort(key = lambda x : (-x[0], x[1]))

    # 배양 용기 이동
    move_cell()

    # 정산
    score()

    print(ans)
