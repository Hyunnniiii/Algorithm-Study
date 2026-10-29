# 0 빈 공간 / 1 사무실 / 2345 좌상우하
# [1] 에어컨에서 바람 나온다
# - 에어컨 다음 칸부터 54321
# - 꺾어서 진행. 진행하는 도중 벽이 있으면 막힌다
# - 근데 꺾는 곳에는 시원함 반영 안되고 도착하면 거기서 반영
# - 에어컨 여러대인 경우 이들의 시원함을 모두 합한다 >> 동시에
# - 에어컨이 있는 곳에도 시원함 생길 수 있다

# [2] 시원한 공기 섞기
# - 인접칸에 대해 계산식만큼 전파 >> 동시에
# - 마찬가지로 벽이 있으면 안됨
# - 빈 칸들에 대해서도 적용됨

# [3] 외벽 1 감소
# - 0이 아닐 때 해당

# 구할 것: 모든 사무실의 시원함의 정도가 k 이상이 되는 최초의 시간


# [주의]
# 1번 과정만 잘 처리하면 나머지는 ㄱㅊ음
# 동시에 조건: 바람 나오고, 공기 섞이는 과정
# 빈칸에 대해서도 시원한 공기 섞기 적용됨
# 사무실만 k 이상이면 됨
# 왜 0행부터인지 안알려주냐
# 가정: 매 턴 시작마다 에어컨에서 나오는 바람 추가된다 & 바람은 항상 5~1
# 입력으로 주어지는 벽의 좌표는 1행부터 시작이다 > 1 빼주고 시작
# =====================
from collections import deque

def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 바람 만들기
# BFS 같음
def wind(sr, sc):
    new_wind = [[0]*N for _ in range(N)]
    ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ
    ㅗ
    ㅗ
    ㅗㅗ
    ㅗ
    ㅗㅗㅗ
    ㅗ
    ㅗ
    ㅗ
    ㅗㅗ
    ㅗㅗ
    ㅗ
    ㅗㅗ
    ㅗ
    ㅗㅗ
    ㅗ소
    ㅗㅗ
    ㅗ
    ㅗㅗ
    ㅗ
    ㅗㅗ
    ㅗㅗㅗ
    ㅗㅗ
    ㅗ
    ㅗ
    ㅗㅗ
    ㅗㅗㅗㅗ
    ㅗ
    ㅗ
    ㅗㅗㅗ
    ㅗㅗ
    ㅗㅗㅗ
    ㅗㅗ
    ㅗ
    ㅗㅗ
    ㅗ
    ㅗ
    이거 걍 나중에 다시 처음부터 풀게 굿바이
    # 오른쪽(2)이라고 가정
    # 확인할 방향: 2 / 1 2 / 3 2
    Q = deque([(sr,sc+1)])
    new_wind[sr][sc+1] = 5
    first_wind_row = sr

    while Q:
        sr, sc = Q.popleft()

        nr1, nc1 = sr, sc+1     # 직진
        nr2, nc2 = sr-1, sc     # 상
        nr3, nc3 = sr+1, sc     # 하

        # 3개 방향을 확인: 벽이 있는가?
        # 직진(우)
        if in_range(nr1, nc1):
            if (nr1, nc1) not in wall or 1 not in wall[(nr1, nc1)]:
                Q.append((nr1, nc1))
                new_wind[nr1][nc1] += (nc1 - first_wind_row)

        # 상
        if in_range(nr2, nc2):
            if (nr2, nc2) not in wall or 0 not in wall[(nr2+1, nc2)]:
                Q.append((nr2, nc2))

        # 하
        if in_range(nr3, nc3):
            if (nr3, nc3) not in wall or 0 not in wall[(nr3, nc3)]:
                Q.append((nr3, nc3))








# 좌상우하
di = [0,-1,0,1]
dj = [-1,0,1,0]



if __name__ == '__main__':

    ## 입력 받기
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    wall = {}
    for _ in range(M):
        x, y, s = map(int, input().split())
        if (x-1, y-1) in wall.keys():
            wall[(x-1, y-1)].append(s-2)
        else:
            wall[(x-1, y-1)] = [s-2]


    ## 매 턴마다 추가되는 시원함 미리 만들어두기
    # 1. 배열을 돌다가 에어컨 위치가 있으면 시작
    for r in range(N):
        for c in range(N):
            if arr[r][c] > 1:

                # 2. 에어컨의 방향을 확인한다


# ====
# 만드려다 실패한 함수 첨부
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
wall = {}
for _ in range(M):
    x, y, s = map(int, input().split())
    if (x - 1, y - 1) in wall.keys():
        wall[(x - 1, y - 1)].append(s)
    else:
        wall[(x - 1, y - 1)] = [s]


def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N


# 좌상우하
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

from collections import deque


def wind(sr, sc, air_d):
    new_wind = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    if air_d == 0:  # 왼쪽
        # 확인할 방향: 0 / 1 0 / 3 0
        Q = deque([(sr, sc - 1)])
        visit[sr][sc - 1] = 1
        new_wind[sr][sc - 1] = 5
        first_wind_row = sr
        first_wind_col = sc

        while Q:
            sr, sc = Q.popleft()

            nr1, nc1 = sr, sc - 1  # 직진
            nr2, nc2 = sr - 1, sc  # 상
            nr3, nc3 = sr + 1, sc  # 하

            # 3개 방향을 확인: 벽이 있는가?
            # 직진(좌)
            if in_range(nr1, nc1) and not visit[nr1][nc1]:
                if (nr1, nc1 + 1) not in wall or 1 not in wall[(nr1, nc1 + 1)]:

                    # 직진해도 되는지 확인
                    # 위
                    if nr1 < first_wind_row:
                        if not (in_range(nr1 + 1, nc1 + 1) and new_wind[nr1 + 1][nc1 + 1]):
                            visit[nr1][nc1] = 1
                            continue
                    # 아래
                    if nr1 > first_wind_row:
                        if not (in_range(nr1 - 1, nc1 + 1) and new_wind[nr1 - 1][nc1 + 1]):
                            visit[nr1][nc1] = 1
                            continue

                    # 위에서 걸러지지 않았다면 직진
                    Q.append((nr1, nc1))
                    if 6 - (nc1 - first_wind_col) >= 0:
                        new_wind[nr1][nc1] += 6 - (first_wind_col - nc1)
                    visit[nr1][nc1] = 1

            # 상
            if in_range(nr2, nc2) and not visit[nr2][nc2]:
                if (nr2 + 1, nc2) not in wall or 0 not in wall[(nr2 + 1, nc2)]:
                    Q.append((nr2, nc2))

            # 하
            if in_range(nr3, nc3) and not visit[nr3][nc3]:
                if (nr3, nc3) not in wall or 0 not in wall[(nr3, nc3)]:
                    Q.append((nr3, nc3))

    if air_d == 2:  # 오른쪽
        # 확인할 방향: 2 / 1 2 / 3 2
        Q = deque([(sr, sc + 1)])
        visit[sr][sc + 1] = 1
        new_wind[sr][sc + 1] = 5
        first_wind_row = sr
        first_wind_col = sc

        while Q:
            sr, sc = Q.popleft()

            nr1, nc1 = sr, sc + 1  # 직진
            nr2, nc2 = sr - 1, sc  # 상
            nr3, nc3 = sr + 1, sc  # 하

            # 3개 방향을 확인: 벽이 있는가?
            # 직진(우)
            if in_range(nr1, nc1) and not visit[nr1][nc1]:
                if (nr1, nc1) not in wall or 1 not in wall[(nr1, nc1)]:

                    # 직진해도 되는지 확인
                    # 위
                    if nr1 < first_wind_row:
                        if not in_range(nr1 + 1, nc1 - 1) or new_wind[nr1 + 1][nc1 - 1] == 0:
                            continue
                    # 아래
                    if nr1 > first_wind_row:
                        if not in_range(nr1 - 1, nc1 - 1) or new_wind[nr1 - 1][nc1 - 1] == 0:
                            continue

                    # 위에서 걸러지지 않았다면 직진
                    Q.append((nr1, nc1))
                    if 6 - (nc1 - first_wind_col) >= 0:
                        new_wind[nr1][nc1] += 6 - (nc1 - first_wind_col)
                    visit[nr1][nc1] = 1

            # 상
            if in_range(nr2, nc2) and not visit[nr2][nc2]:
                if (nr2 + 1, nc2) not in wall or 0 not in wall[(nr2 + 1, nc2)]:
                    Q.append((nr2, nc2))
            # 하
            if in_range(nr3, nc3) and not visit[nr3][nc3]:
                if (nr3, nc3) not in wall or 0 not in wall[(nr3, nc3)]:
                    Q.append((nr3, nc3))

    if air_d == 1:  # 위
        # 확인할 방향: 1 / 1 0 / 1 2
        Q = deque([(sr - 1, sc)])
        visit[sr - 1][sc] = 1
        new_wind[sr - 1][sc] = 5
        first_wind_row = sr
        first_wind_col = sc

        while Q:
            sr, sc = Q.popleft()

            nr1, nc1 = sr - 1, sc  # 직진
            nr2, nc2 = sr, sc + 1  # 우
            nr3, nc3 = sr, sc - 1  # 좌

            # 3개 방향을 확인: 벽이 있는가?
            # 직진(상)
            if in_range(nr1, nc1) and not visit[nr1][nc1]:
                if (nr1 + 1, nc1) not in wall or 0 not in wall[(nr1 + 1, nc1)]:

                    # 직진해도 되는지 확인
                    # 우
                    if nc1 > first_wind_col:
                        if not (in_range(nr1 + 1, nc1 - 1) and new_wind[nr1 + 1][nc1 - 1]):
                            continue
                    # 좌
                    if nc1 < first_wind_col:
                        if not (in_range(nr1 + 1, nc1 + 1) and new_wind[nr1 + 1][nc1 + 1]):
                            continue

                    # 위에서 걸러지지 않았다면 직진
                    Q.append((nr1, nc1))
                    if 6 - (nr1 - first_wind_row) >= 0:
                        new_wind[nr1][nc1] += 6 - (nr1 - first_wind_row)
                    visit[nr1][nc1] = 1

            # 우
            if in_range(nr2, nc2) and not visit[nr2][nc2]:
                if (nr2, nc2) not in wall or 1 not in wall[(nr2, nc2)]:
                    Q.append((nr2, nc2))
            # 좌
            if in_range(nr3, nc3) and not visit[nr3][nc3]:
                if (nr3, nc3 + 1) not in wall or 1 not in wall[(nr3, nc3 + 1)]:
                    Q.append((nr3, nc3))

    if air_d == 3:  # 아래
        # 확인할 방향: 3 / 3 0 / 3 2
        Q = deque([(sr + 1, sc)])
        visit[sr + 1][sc] = 1
        new_wind[sr + 1][sc] = 5
        first_wind_row = sr
        first_wind_col = sc

        while Q:
            sr, sc = Q.popleft()

            nr1, nc1 = sr + 1, sc  # 직진
            nr2, nc2 = sr, sc + 1  # 우
            nr3, nc3 = sr, sc - 1  # 좌

            # 3개 방향을 확인: 벽이 있는가?
            # 직진(하)
            if in_range(nr1, nc1) and not visit[nr1][nc1]:
                if (nr1, nc1) not in wall or 0 not in wall[(nr1, nc1)]:

                    # 직진해도 되는지 확인
                    # 우
                    if nc1 > first_wind_col:
                        if not (in_range(nr1 - 1, nc1 - 1) and new_wind[nr1 - 1][nc1 - 1]):
                            continue
                    # 좌
                    if nc1 < first_wind_col:
                        if not (in_range(nr1 - 1, nc1 + 1) and new_wind[nr1 - 1][nc1 + 1]):
                            continue

                    # 위에서 걸러지지 않았다면 직진
                    Q.append((nr1, nc1))
                    if 6 - (nr1 - first_wind_row) >= 0:
                        new_wind[nr1][nc1] += 6 - (nr1 - first_wind_row)
                    visit[nr1][nc1] = 1

            # 우
            if in_range(nr2, nc2) and not visit[nr2][nc2]:
                if (nr2, nc2) not in wall or 1 not in wall[(nr2, nc2)]:
                    Q.append((nr2, nc2))
            # 좌
            if in_range(nr3, nc3) and not visit[nr3][nc3]:
                if (nr3, nc3 + 1) not in wall or 1 not in wall[(nr3, nc3 + 1)]:
                    Q.append((nr3, nc3))
    for row in new_wind:
        print(*row)


wind(3, 3, 0)




