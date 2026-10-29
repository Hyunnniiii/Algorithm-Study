
""" 자율주행 전기차 / 20261001 졸리다.... / 체감 난이도: 골드5
소요 시간 46분 / 시도 1회 / 실행 시간 54ms (코드트리) / 메모리 16MB (코드트리)

뭐지?? 이 문제 진짜 신들린 것 마냥 풀었다. 구상을 더 오래한듯
첫 풀이 때 승객들 간 도착지가 겹칠 수 있는데 그걸 반영 안해서 틀렸던 기억이 나서..
그게 나름 함정인 문제인데 알아버려서 그냥 쉽게 푼듯.
그리고 최단거리 bfs도 이미 너무 잘 템플릿화 해버려서 정말 쉽게 풀었다.
ㄹㅈㄷ 성장한거 느껴짐 푸하하

bfs 초기위치 확인, 마지막에 리턴하는 방식 익히기 좋은 문제.

"""

# 15:00 ~ 15:46 끝

# 구할 것: 불가하면 -1 / 다 데려다준 경우 남은 배터리 양
# =================================
from collections import deque

# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


# 가장 가까운 승객 찾기
def find_nearest_passenger(r, c):
    # 초기 위치에 다른 승객 있는 경우
    if passenger_start[r][c]>0:
        return r, c, 0

    # 그게 아니면 bfs 수행
    Q = deque()
    Q.append((r,c))
    visit = [[-1]*N for _ in range(N)]
    visit[r][c] = 0
    min_dist = float('inf')
    hubo = []

    while Q:
        sr, sc = Q.popleft()

        # 먼 거리가 나오기 시작하면 끊기
        if visit[sr][sc] >= min_dist:
            break

        for k in range(4):
            nr,nc = sr+dr[k], sc+dc[k]

            if not in_range(nr,nc) or visit[nr][nc] != -1:
                continue
            if arr[nr][nc] == 1:
                continue

            if passenger_start[nr][nc]:
                min_dist = visit[sr][sc] + 1
                visit[nr][nc] = visit[sr][sc] + 1
                hubo.append((nr,nc))

            Q.append((nr,nc))
            visit[nr][nc] = visit[sr][sc] + 1

    # 도달하지 못한다면
    if not hubo:
        return None, None, None

    # 후보 정렬, 최종 선택
    hubo.sort(key = lambda x : (x[0], x[1]))
    return hubo[0][0], hubo[0][1], min_dist


# 승객 목적지에 데려다주기
def drop_passenger(r, c, idx):
    Q = deque()
    Q.append((r,c))
    visit = [[-1]*N for _ in range(N)]
    visit[r][c] = 0

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr+dr[k], sc+dc[k]

            if not in_range(nr,nc) or visit[nr][nc]!=-1:
                continue
            if arr[nr][nc] == 1:
                continue

            if idx in set(passenger_end[nr][nc]):
                return nr, nc, visit[sr][sc]+1

            Q.append((nr,nc))
            visit[nr][nc] = visit[sr][sc] + 1

    # 목적지에 못 가는 경우
    return None, None, None


def debug_print(msg):
    if DEBUG:
        print(msg)
        print('현재 차 위치', car_r, car_c)
        print()
        print('현재 배터리', battery)
        print()

########################
DEBUG = True
N, M, battery = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]   # 벽, 도로
car_r, car_c = map(lambda x : int(x)-1, input().split())
passenger_start = [[0]*N for _ in range(N)] # 출발지
passenger_end = [[[] for _ in range(N)] for _ in range(N)]  # 목적지
for idx in range(1, M+1):
    sr, sc, er, ec = map(lambda x : int(x)-1, input().split())
    passenger_start[sr][sc] = idx
    passenger_end[er][ec].append(idx)

# debug_print('입력 확인')

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

## 실행
while True:
    # [1] 현재 차 위치에서 가장 가까운 승객 찾기
    car_r, car_c, dist = find_nearest_passenger(car_r, car_c)

    # 갈 수 있는 곳이 없으면 끝
    if dist is None:
        print(-1)
        break

    # 배터리 부족하면 끝
    if dist > battery:
        print(-1)
        break

    # 배터리, start 배열 갱신 / 목적지 번호 설정
    passenger_idx = passenger_start[car_r][car_c]
    battery -= dist
    passenger_start[car_r][car_c] = 0

    # [2] 승객 목적지로 보내기
    car_r, car_c, dist = drop_passenger(car_r, car_c, passenger_idx)

    # 갈 수 있는 곳이 없으면 끝
    if dist is None:
        print(-1)
        break

    # 배터리 부족하면 끝
    if dist > battery:
        print(-1)
        break

    # 배터리 2배 충전
    battery += dist

    # [3] 정산
    if sum(map(sum, passenger_start)) == 0:
        print(battery)
        break