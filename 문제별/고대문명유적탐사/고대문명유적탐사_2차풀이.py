
""" 고대 문명 유적 탐사 / 20261006 찹쌀떡 맛있다 / 체감 난이도: 골드 4
소요 시간 70분 / 시도 2회 / 실행 시간 170ms (코드트리) / 메모리 22MB (코드트리)

첫 제출 때 틀린 이유는 열 > 행 우선인데 행 > 열로 적어서

부분 배열 나와서 쫄았는데 응 내가 해냈다
어떻게 풀어야 좋았던건지 기억이 나서.. 그대로 구현했다 (for문 순서로 우선순위 반영, 배열 상태 저장)
1차 풀이 때 90도 회전 노가다 3번 돌린게 좀 웃기고 슬프다 후기 끝

"""

# 15:00 ~ 11분 중단 20분 시작 ~ 16:15

# 구할 것: 각 턴마다 획득한 유물 가치의 총합
# =======================================
from collections import deque

def in_range(nr, nc):
    return 0<=nr<5 and 0<=nc<5


def rotate_arr(imsi):
    new_imsi = [list(row[:]) for row in zip(*imsi[::-1])]
    return new_imsi


def bfs(arr):
    visit = [[0]*5 for _ in range(5)]
    final_route = []
    for r in range(5):
        for c in range(5):
            if visit[r][c]:
                continue

            Q = deque()
            Q.append((r, c))
            visit[r][c] = 1
            my_idx = arr[r][c]
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
                    route.append((nr, nc))
            if len(route) >= 3:
                for coord in route:
                    final_route.append(coord)
    return final_route



def debug_print(msg):
    if DEBUG:
        print(msg)
        for row in final_arr:
            print(row)
        print()

#####################
DEBUG = True
K, M = map(int, input().split())
real_arr = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 실행부
lst = []    # 포인트 넣을거임
for turn in range(K):
    # [0] 이번 턴에서 최고의 선택 찾기
    final_route = []
    final_arr = None
    point = 0

    # [1] 회전 각도 정하기
    for angle in range(1, 4):

        # [2] 정사각형 중심 정하기
        for col in range(1, 4):
            for row in range(1, 4):
                arr = [r[:] for r in real_arr]

                # [3] 이걸 중심으로 하는 3x3 정사각형 선택, 선택 각도만큼 돌리기
                imsi = [r[col-1:col+2] for r in arr[row-1:row+2]]
                for _ in range(angle):
                    imsi = rotate_arr(imsi)

                # [4] 돌린거 원본 배열에 넣어주기
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        arr[r][c] = imsi[r-row+1][c-col+1]

                # [5] 이제 여기에서 유물 1차 획득
                route = bfs(arr)

                if len(route) > len(final_route):
                    final_route = route
                    final_arr = [row[:] for row in arr]

    # 조기 종료 확인
    if not final_route:
        break

    debug_print('최적의 선택 완료')

    # [6] 점수 추가
    point += len(final_route)

    # [7] 벽면 숫자 넣어주기
    final_route.sort(key = lambda x : (x[1], -x[0]))
    for x, y in final_route:
        num = wall.pop(0)
        final_arr[x][y] = num

    debug_print('벽면 숫자 추가')

    # [8] 유물 연쇄 획득
    while True:
        route = bfs(final_arr)

        if not route:
            break

        point += len(route)
        route.sort(key = lambda x : (x[1], -x[0]))
        for x, y in route:
            num = wall.pop(0)
            final_arr[x][y] = num

    debug_print('유물 연쇄 획득')

    # [9] 이제 이 배열로 다음 턴 시작
    real_arr = [row[:] for row in final_arr]
    lst.append(point)

print(*lst)







