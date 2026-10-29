
""" 방화벽 설치하기 / 20260915 / 체감 난이도: 실버
소요 시간 37분 / 시도 1회 / 실행 시간 417ms (코드트리) / 메모리 23MB (코드트리)

나 아직도!!!!!!!!!!! 백트래킹 할 때 조합 / 순열 생각 안하네
조금 소름 돋을 정도로 예전이랑 비슷하게 풀었다
r = num//M, c = num%M 아주 유용해보임 & 동시 BFS

처음에 내가 선택한 행,열 이후부터 탐색하고 싶어서 (조합을 하고 싶었던 거지) for문에다가 cur_r, cur_c부터
시작해주세요~~라고 코드를 짰다가 디버깅으로 잘못되었다는 것을 깨달았다.
근데 여기서 그냥 row~col~ 전부 다 돌리게 코드 짜서 순열이 되었고 실행시간 폭발했다.

"""
# ================
from collections import deque

def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<M

def bfs():
    visit = [[0]*M for _ in range(N)]
    Q = deque()

    for row in range(N):
        for col in range(M):
            if arr[row][col] == 2:
                Q.append((row, col))
                visit[row][col] = 1

    # 불 퍼뜨리기 시작
    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr+di[k], sc+dj[k]

            # 범위 내, 미방문, not 벽 > 가능
            if in_range(nr, nc) and not visit[nr][nc] and arr[nr][nc] != 1:
                Q.append((nr, nc))
                visit[nr][nc] = 1

    # 불 영역의 크기 출력
    return sum(map(sum, visit))


def choose_three(cnt, start):
    global min_fire
    # 종료: 방화벽 3군데에 모두 설치
    if cnt == 3:
        fire = bfs()
        min_fire = min(min_fire, fire)
        return

    # 실행: 너 여기에서 설치 할래?
    for num in range(start,N*M):
        r = num//M
        c = num%M

        # 빈칸이면 설치 가능
        if arr[r][c] == 0:
            arr[r][c] = 1
            choose_three(cnt+1, num+1)
            arr[r][c] = 0


# ===========================================
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 실행
wall = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            wall += 1

lst = []
min_fire = float('inf')
choose_three(0, 0)

print(N*M-min_fire-wall-3)