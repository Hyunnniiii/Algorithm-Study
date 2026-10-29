
""" 토스트 계란틀 / 20260917 / 체감 난이도: 실버
소요 시간 39분 / 시도 1회 / 실행 시간 299ms (코드트리) / 메모리 26MB (코드트리)

일단 과거의 내가 더 편하게 풀었다.
왜냐면 나는 합칠 계란에 대한 판정을 모두 완료한 뒤에 합쳐야 한다는 뭔가.. 지금까지 풀었던 문제들에
기반한 완료 후 처리 강박증에 빠진 나머지 그냥 bfs 돌리면서 한번에 처리해도 되는데 굳이 그룹별 정보를
딕셔너리에 받아서 따로 함수 구현해서 따로 처리해줬다.

근데 나쁜건 아닌 것 같음. 배열 갱신할 땐 항상 완료 후 처리!!!
종료 시점에 대한 처리는 이전보다 훨씬 편하게 했다.
엣지에 대한 것도 훨씬 잘 생각해냈으나 문제가 친절해서 다 알려줬다.. (0번째에 종료하는 경우)


"""

# 계란틀을 이루는 4개의 선 분리 가능
# [1] 상하좌우 인접한 계란틀과의 차이가 L~R사이면 해당 선을 분리
# 모든 계란틀에 대해 검사. 검사 완료 하고 나서 한번에 분리
# [2] 분리해서 한 그룹이 된 계란들의 계란의 양 계산, 적용
# [3] 종료: 계란의 이동이 더이상 필요 없을 때까지
# 구할 것: 계란의 이동이 몇 번 일어나는가? = 몇 턴인가?

# 의ㅡ심
# 가장자리 선은 제외인거얀? > 어차피 인접한게 없으니까 제외할 일이 없음
# 계란의 이동 무한대로 되는 경우? > 2000번 이내라고 알려줌
# 애초에 처음부터 이동 안해도 되는 경우?

# ==============================================
from collections import deque

## 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


## bfs
# 인접한 곳 탐색, L~R 사이인지 확인, group에 대한 정보 딕에 넣어줘
def bfs():
    visit = [[0]*N for _ in range(N)]
    group_info = {}
    idx = 0

    # 배열 순회하면서
    for r in range(N):
        for c in range(N):
            # 그룹에 포함되지 않은 곳만
            if not visit[r][c]:
                Q = deque([(r,c)])
                visit[r][c] = 1
                group_info[idx] = [(r,c)]

                while Q:
                    sr, sc = Q.popleft()

                    for k in range(4):
                        nr, nc = sr+dr[k], sc+dc[k]

                        # 범위, 방문 체크
                        if not in_range(nr, nc) or visit[nr][nc]:
                            continue
                        # 차이 확인
                        if not (L <= abs(arr[sr][sc]-arr[nr][nc]) <= R):
                            continue

                        # 여기까지 왔으면 같은 그룹으로 해줘야 함
                        visit[nr][nc] = 1
                        group_info[idx].append((nr,nc))
                        Q.append((nr,nc))

                # 한 그룹 탐색 끝났으면 다음 그룹 가야지
                idx += 1

    # 다 탐색했으면 그룹 인포 반환
    return group_info


# ## 계란 합치기
def hapchiggi(group_info):
    global arr

    new_arr = [[0]*N for _ in range(N)]
    for val in group_info.values():
        egg_sum = 0  # 계란의 총 합
        egg_num = len(val)  # 계란틀의 총 개수

        for x,y in val:
            egg_sum += arr[x][y]

        to_put = egg_sum//egg_num
        for x, y in val:
            new_arr[x][y] += to_put

    arr = new_arr


# =======================================
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

## 실행
turn = 0
while True:
    # [1] 계란틀 검사, 그룹 정보 받기
    group_info = bfs()

    # 그룹이 있긴 한지?
    if len(group_info) == N*N:
        print(turn)
        break

    # [2] 같은 그룹끼리 계란 합치기
    hapchiggi(group_info)

    # [3] 턴 수 +1
    turn += 1