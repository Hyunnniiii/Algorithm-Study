
""" 전투로봇 / 20260919 / 체감 난이도: 실버
소요 시간 45분 / 시도 1회 / 실행 시간 56ms (코드트리) / 메모리 17MB (코드트리)

구상 15분 구현 30분
이 문제 내가 상좌우하 설정하면 최단거리 작은행열 보장한다고 착각했던 문제다. 푸하하
거리제한 bfs를 알아두니 참 편하구만
과거의 나 창의력은 더 좋은듯. 몬스터 찾으면 바로 새로운 bfs 재귀로 시작.. 참신하구만

놓친 점: 종료조건에 대해 생각했으나.. 몬스터들에 의해 길이 막혀있을 거라는 생각은 못함
다행히 테케 2번이 딱 그 케이스라서 알아차렸지만.. 놓친거 에바라고 생각

"""

# 전투로봇 1개, 한 칸에 몬스터 한 마리
# 초기 전투로봇 레벨 2, 1초에 상하좌우 인접한 한 칸씩 이동
# 자신의 레벨보다 작은 몬스터만 죽일 수 있다
# 레벨이 같으면 지나가기만 가능. 레벨 높으면 지나가기도 못함

# [1] 전투로봇 이동
# 없앨 수 있는 몬스터가 있다면 없애러 간다.
# 즉, 없앨 수 있는 몬스터가 없으면 > 게임 종료
# 거리(BFS)가 가장 가까운 > 행 작은 > 열 작은
# [2] 이동 후 처리
# 전투로봇이 몬스터 칸에 도달하면, 몬스터는 바로 사라진다
# 본인 레벨과 같은 수의 몬스터 없앨 때마다 레벨업

# 구할 것: 전투로봇이 일을 끝낼 때까지 걸리는 시간

# 의-심
# 안끝나는 경우가 있는가 > 없음
# 처음부터 몬스터가 없는 경우 또는 처음부터 죽일 몬스터가 없는 경우 > 가능함
# 종료 가능한 경우: 모두 죽여서 or 애초에 몬 없을 때 / 나보다 레벨 큰 몬만 남았을 때
# ===================================
import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

# 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

# 이동
# - BFS로 짧은거리가 나오면 그 거리까지만 구한 다음에
# - 작은 행, 작은 열 튜플 비교해서 남은 최종을 목적지로 삼는다
def bfs(cur_r, cur_c):
    Q = deque([(cur_r, cur_c)])
    visit = [[-1]*N for _ in range(N)]
    visit[cur_r][cur_c] = 0
    dist = float('inf')
    final = (float('inf'), float('inf'))    # 행, 열 저장

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr+dr[k], sc+dc[k]

            # 범위 내, 미방문 체크
            if not in_range(nr,nc) or visit[nr][nc] != -1:
                continue

            # 더 먼 거리가 나오면 > 그만
            if visit[sr][sc] == dist:
                continue

            # 몬스터 못 죽이지만 지나갈 수 있으면 > 그 다음으로
            if arr[nr][nc] == cur_lev or arr[nr][nc] == 0:
                Q.append((nr,nc))
                visit[nr][nc] = visit[sr][sc] + 1

            # 죽일 수 있는 몬스터가 있으면 > 이 거리까지 모두 봐주세요
            if 0 < arr[nr][nc] < cur_lev:
                Q.append((nr,nc))
                visit[nr][nc] = visit[sr][sc]+1
                dist = visit[nr][nc]
                final = min(final, (nr,nc))

    return final[0], final[1], dist


################
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 전투로봇 초기 정보
cur_r, cur_c, cur_lev, cur_kill = -1, -1, 2, 0
for r in range(N):
    for c in range(N):
        if arr[r][c]==9:
            cur_r, cur_c = r, c
            arr[r][c] = 0
            break

# 방향(상하좌우)
dr = [-1,1,0,0]
dc = [0,0,-1,1]

## 실행부
time = 0
while True:
    # [1] 이동
    # - BFS로 짧은거리가 나오면 그 거리까지만 구한 다음에
    # - 작은 행, 작은 열 튜플 비교해서 남은 최종을 목적지로 삼는다
    cur_r, cur_c, dist = bfs(cur_r, cur_c)

    # 못 갈 수 있음: 여러 이유로.. 몬스터가 애초에 없거나, 레벨이 다 높거나, 막혀있거나..
    if dist == float('inf'):
        print(time)
        break

    # 갈 수 있으면 시간 추가
    time += dist

    # [3] 처리
    # - 과정 2에서 받은 거리, 좌표 정보에 따라 배열, 전투로봇 정보 갱신
    arr[cur_r][cur_c] = 0
    cur_kill += 1
    # 레벨업 가능 여부 확인
    if cur_kill==cur_lev:
        cur_lev+=1
        cur_kill=0