
''' 미생물 연구 / 20260928 / 체감 난이도 : 골드 3
소요 시간: 2h 15m / 시도: 1회 / 실행 시간: 197ms (코드트리) / 메모리: 23MB

[타임라인]
09:00 - 09:45(45분) 문제 읽기 / 입력 받기 / 구상
09:45 - 10:53(68분) 구현
10:53 - 11:15(22분) 디버깅, 검증, 제출


[구상]
- 일단 구상이 잘 안떠올랐다.. 보통 문제를 보면 음 이걸 하면 되겠군. 하는데 이 문제는 그렇지 않았음
쪼개진 미생물 판정이나 결과 기록 부분은 bfs로 어떻게 가능하겠다는 생각이 들었는데, 용기 이동 부분이 아주
까다롭게 느껴졌다.

- 특히 그룹의 좌표를 모두 저장해놔야 하는지에 대해 많이 고민했는데, 그냥 저장했다.
이유: 저장하지 않고선 도저히 방법이 떠오르지 않았음.
(내가 생각한 다른 방법들: 원본 배열에 바로 평행이동해서 덮어 씌우기-기존에 있던 미생물 사라져서 안됨,
좌하단 좌표만 가능한 가장 왼쪽 아래에 끼워넣기-그 좌표가 제일 오른쪽 아래에 달려있는 경우만 생각해도 성립이 안됨,
좌표 변환 활용해서 좌상단 ~ 우하단 범위 내만 확인하기 - 안되는 경우가 있음)

- 내 구상을 따르면 bfs를 많이 하고 sort도 매 턴 수행하고 딕셔너리 순회도 많이 해서 시간이 괜찮을까?
걱정했는데 시간제한 5000ms길래 아 이거 어차피 오래 걸리는거구나 하고 진행했다.

- N차 풀이의 덕을 많이 봤다.
미생물을 넣는 위치의 우선순위가 작은 열, 큰 행이었는데 이걸 for문 순회 순서로 구현할 생각을 한 것
 ㄴ> 종전, 디저트카페(자신감 충전 문제) 풀면서 이걸 써먹어서 생각해낼 수 있었음
인접한 그룹 찾기 > 예술성에서 비슷한거 있었음

- (bad)
좌표 변환 정도는 그냥 알고 있자.. 구상 때 계산하려니 현타가


[구현]
- 역시나 구상 단계에서 가장 감이 잡히지 않았던 배양용기 이동 단계에서 많이 고전했다.
 아마 가능한지 따져야 하는 여부가 많아서 그랬던 것 같은데
 1. 그룹의 모든 좌표가 범위 내에 들어오는지
 2. 다른 미생물과 겹치지 않는지
 3. 그러면서 우선순위를 만족하는지
 다 고려해야 했기 때문에 코드가 좀 복잡해졌다.. status 쓰는거 개인적으로 좋아하지 않는디

- 구현하면 할 수록 주석으로 투두리스트 적어두기, continue로 안되는 조건 쳐내고 시작하기 넘 좋다
- 하도 오타 때문에 고생을 많이 해서 r, c, nr, nc 눈에 불을 켜고 구현했더니 다행히 그런 실수는 하지 않았다


[디버깅]
- 저번에 디버깅 콘테스트??에서 예은님이 하는 디버깅 + 디버깅 프린트 루틴화 (by 회수정)
진짜 잘 써먹었다!!!!!!!! 다만 이제 짬뽕됨. 프린트도 하고 디버거도 쓰고 디버깅 프린트도 씀;; 좋지 뭐


[후기]
N차 풀이를 열심히 하자
기본적인 것들은 좀 알아두자 (좌표 변환, 달팽이, 회전, 중력, 주사위, ..)
난 잘 까먹으니까. 자주 다시 공부하자

---------------------------------------------------------
[개선]
인접 쌍 찾기 bfs 없이 할 수 있음
배양 용기 옮기기 부분 코드를 덜 복잡하게 바꾸기

[번외]
문제 읽다가 컴퓨터 에러나서 블루스크린 뜨는 대참사가 일어났다.
뭐임? 강제종료하긴 했는데 좀 웃김

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
                group_coord[arr[r][c]] = [(0,0)]

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
                        group_coord[arr[r][c]].append((nr-r,nc-c))

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
                    nr, nc = row+r, col+c

                    if not in_range(nr,nc):
                        status = False
                        break

                    if imsi[nr][nc] > 0:
                        status = False
                        break

                if not status:
                    continue

                # 여기로 오면 가능하다는 것
                for r, c in group_coord[idx]:
                    imsi[row+r][col+c] = idx

                status = True
                break

            if status:
                break

    arr = imsi


# [3] 정산
def score():
    global ans
    near_group = set()

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue

            # 오른쪽
            if c+1 < N:
                other = arr[r][c+1]

                if other != 0 and other != arr[r][c]:
                    near_group.add(tuple(sorted((arr[r][c], other))))

            # 아래
            if r+1 < N:
                other = arr[r+1][c]

                if other != 0 and other != arr[r][c]:
                    near_group.add(tuple(sorted((arr[r][c], other))))

    for g1, g2 in near_group:
        ans += len(group_coord[g1])*len(group_coord[g2])


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

    # 그룹 정보 리스트 sort
    group_info.sort(key = lambda x : (-x[0], x[1]))

    # 배양 용기 이동
    move_cell()

    # 정산
    score()

    print(ans)
