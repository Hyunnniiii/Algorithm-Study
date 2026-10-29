
""" 미생물 연구 / 20261007 0+0 노래 좋다 / 체감 난이도: 골드4
소요 시간 63분 / 시도 1회 / 실행 시간 199ms (코드트리) / 메모리 23MB (코드트리)

괄호 잘못 써서 디버깅 한참 했음
노래 들으면서 구현해서 그랬나봄 진짜 안보인다..
근데 조건문 전체 괄호로 감싼거 왜 True 처리 됨?
 ㄴ>  if ((a, b) in paired): 이래놔서 if tuple:이라 항상 True 처리됨 ㄷㄷ

"""

# 14:20~15:23
# 구할 것: 각 턴마다 실험 결과 출력
# ============================
from collections import deque


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

def find_cell_coord():
    group_info = []
    exclude = set()    # 중복돼서 제거할 cell idx
    find = set()    # 찾은 그룹 넣기
    visit = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0 or visit[r][c]:
                continue
            if arr[r][c] in find:
                exclude.add(arr[r][c])
                continue

            my_idx = arr[r][c]
            find.add(arr[r][c])

            Q = deque()
            Q.append((r, c))
            visit[r][c] = 1
            route = [(r,c)]

            while Q:
                sr, sc = Q.popleft()

                for k in range(4):
                    nr, nc = sr + dr[k], sc + dc[k]

                    if not in_range(nr, nc) or visit[nr][nc]:
                        continue
                    if arr[nr][nc] != my_idx:
                        continue
                    Q.append((nr, nc))
                    visit[nr][nc] = 1
                    route += [(nr, nc)]

            group_info.append((my_idx, len(route), route))
    return exclude, group_info


def score():
    res = 0
    paired = set()  # 이미 찾은 쌍
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue

            me = arr[r][c]

            for k in (1,3):
                nr, nc = r + dr[k], c + dc[k]

                if not in_range(nr,nc):
                    continue
                if arr[nr][nc] == me or arr[nr][nc] == 0:
                    continue
                if (min(me, arr[nr][nc]), max(me, arr[nr][nc])) in paired:
                    continue

                other = arr[nr][nc]
                paired.add((min(me, other), max(me, other)))

                a, b = None, None
                for idx, size, _ in cell_info:
                    if idx == me:
                        a = size
                    elif idx == other:
                        b = size
                res += (a*b)
    return res


####################
N, Q = map(int, input().split())
arr = [[0]*N for _ in range(N)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


for time in range(1, Q+1):
    # [1] 미생물 투입
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1 = N-c1-1, r1
    r2, c2 = N-c2-1, r2
    for row in range(r2+1, r1+1):
        for col in range(c1, c2):
            arr[row][col] = time

    # print('미생물 투입')
    # for row in arr:
    #     print(row)
    # print()

    # [2] 배양 용기 이동
    exclude, cell_info = find_cell_coord()
    cell_info.sort(key = lambda x:(-x[1], x[0]))

    new_arr = [[0]*N for _ in range(N)]
    for cell_idx, _, coord in cell_info:
        if cell_idx in exclude:
            continue

        coord.sort(key = lambda x : (-x[0], x[1]))
        sx, sy = coord[0][0], coord[0][1]

        done = False
        for col in range(N):
            for row in range(N-1,-1,-1):
                status = False
                for x, y in coord:
                    nx, ny = row+x-sx, col+y-sy

                    if not in_range(nx,ny):
                        status = False
                        break
                    if new_arr[nx][ny] > 0:
                        status = False
                        break
                    status = True

                # 되는 선택지 여기로
                if status:
                    for x, y in coord:
                        nx, ny = row+x-sx, col+y-sy
                        new_arr[nx][ny] = cell_idx
                    done = True
                    break
                if done:
                    break
            if done:
                break
    arr = [row[:] for row in new_arr]

    # print('미생물 이동')
    # for row in arr:
    #     print(row)
    # print()

    # [3] 실험 결과
    res = score()
    print(res)