
""" 민트 초코 우유 / 20261007 배고프다 / 체감 난이도: 골드4
소요 시간 54분 / 시도 1회 / 실행 시간 539ms (코드트리) / 메모리 26MB (코드트리)

일부러 집합 안써봄
in 연산이 너무 많아서 구현하는 내내 찝찝했는데.. set 썼을 때랑 많이 차이 안났음
최대 3개라 그런듯

* 리스트 비교는 순서까지 완전 같아야 같은 리스트로 판정해준다

"""

# 09:45 ~
# 구할 것: 일자별로, 음식 순서대로 신봉자들의 신앙심 총합
# ===========================
from collections import deque


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


def find_group():
    zzang_lst = []
    visit = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visit[r][c]:
                continue
            Q = deque()
            Q.append((r,c))
            visit[r][c] = 1
            group_lst = [(believe[r][c], r, c)]

            while Q:
                sr, sc = Q.popleft()

                for k in range(4):
                    nr, nc = sr + dr[k], sc + dc[k]

                    if not in_range(nr, nc) or visit[nr][nc]:
                        continue
                    if arr[r][c] != arr[nr][nc]:
                        continue

                    Q.append((nr, nc))
                    visit[nr][nc] = 1
                    group_lst.append((believe[nr][nc], nr, nc))

            group_lst.sort(key = lambda x : (-x[0], x[1], x[2]))

            # 대표자한테 신앙심 넘겨주기
            for _, x, y in group_lst:
                if x == group_lst[0][1] and y == group_lst[0][2]:
                    believe[x][y] += len(group_lst)-1
                else:
                    believe[x][y] -= 1

            zzang_lst.append((len(arr[group_lst[0][1]][group_lst[0][2]]),
                              believe[group_lst[0][1]][group_lst[0][2]],
                              group_lst[0][1], group_lst[0][2]))
    return zzang_lst


# 저녁
def dinner():
    for _, B, r, c in zzang_lst:
        if stun[r][c]:
            continue

        believe[r][c] = 1
        please = B-1
        d = B%4
        food_lst = arr[r][c]

        while True:
            nr, nc = r + dr[d], c + dc[d]

            if please <= 0:
                break
            if not in_range(nr, nc):
                break

            # 나와 같은 음식
            if food_lst == arr[nr][nc]:
                r, c = nr, nc
                continue

            # 강한 전파
            if please > believe[nr][nc]:
                please -= (believe[nr][nc]+1)
                believe[nr][nc] += 1
                arr[nr][nc] = []
                stun[nr][nc] = 1
                for f in food_lst:
                    arr[nr][nc].append(f)
                arr[nr][nc].sort()

            # 약한 전파
            else:
                believe[nr][nc] += please
                please = 0
                stun[nr][nc] = 1
                for f in food_lst:
                    if f not in arr[nr][nc]:
                        arr[nr][nc].append(f)
                arr[nr][nc].sort()

            r, c = nr, nc


def debug_print(msg):
    if DEBUG:
        print(msg)
        print('신봉 음식')
        for row in arr:
            print(row)
        print()
        print('신앙심')
        for row in believe:
            print(row)
        print()


###################
DEBUG = True
N, T = map(int, input().split())
arr = [list(map(lambda x : [x], input())) for _ in range(N)]
believe = [list(map(int, input().split())) for _ in range(N)]   # 신앙심
stun = [[0]*N for _ in range(N)]    # 방어 모드

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 실행
for time in range(T):
    # [1] 아침
    for r in range(N):
        for c in range(N):
            believe[r][c] += 1

    # [2] 점심
    zzang_lst = find_group()

    # 대표자 정렬
    zzang_lst.sort(key = lambda x : (x[0], -x[1], x[2], x[3]))

    debug_print('점심 완료')
    print('대표자 선정: ', zzang_lst)

    # [3] 저녁
    dinner()

    debug_print('저녁 완료')

    # [4] 방어 모드 처리, 정산
    point = [0]*7
    for r in range(N):
        for c in range(N):
            if stun[r][c] > 0:
                stun[r][c] -= 1

            # 민초우
            if len(arr[r][c]) == 3:
                point[0] += believe[r][c]

            # 이중 조합
            if len(arr[r][c]) == 2:
                # 민초
                if 'M' not in arr[r][c]:
                    point[1] += believe[r][c]
                # 민우
                elif 'C' not in arr[r][c]:
                    point[2] += believe[r][c]
                # 초우
                elif 'T' not in arr[r][c]:
                    point[3] += believe[r][c]

            # 단일 조합
            if len(arr[r][c]) == 1:
                # 우
                if 'M' in arr[r][c]:
                    point[4] += believe[r][c]
                # 초
                elif 'C' in arr[r][c]:
                    point[5] += believe[r][c]
                # 민
                elif 'T' in arr[r][c]:
                    point[6] += believe[r][c]

    print(*point)