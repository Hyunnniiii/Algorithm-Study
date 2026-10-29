# 제출 전 확인: M=1일 때 / N=2일 때 /
# 초기: 1행 1열 -> 좌표는 (0,0). 초기의 방향은 오른쪽

# 1. 주사위 방향대로 움직임
# 2. 상하좌우로 인접한 칸들 중 같은 숫자가 적혀있는 모든 칸의 합을 더한다. 본인의 칸 포함
# 여기서 인접하다는 것이 뭐지?? 그냥 일반 BFS를 말하는건가??
# 3. 주사위 아랫면과 보드의 칸 숫자 비교
# 주사위 숫자가 크면: 방향 시계 90도 회전
# 바닥칸 숫자가 크면: 방향 반시계 90도
# 숫자가 같으면: 방향 그대로
# *범위를 벗어나면: 다음에 가야했을 방향의 반대로

# 구할 것: M번 굴렸을 때 총 점수의 합
from collections import deque

## 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 시계방향
di = [-1,0,1,0]
dj = [0,1,0,-1]

dice = [1,5,4,2,3,6]
# 함수: 방향에 따라 주사위의 방향을 바꿔주고, 바닥면의 숫자를 리턴
def jusawii(d):
    if d == 0:  # 위
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]
    if d == 1:  # 오른쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]
    if d == 2:  # 아래
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]
    if d == 3:  # 왼쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]
    return dice[5]


# BFS 함수: 상하좌우로 인접한 모든 칸의 수를 리턴
# ans 입력은 1로 해야함: 시작점 포함
def bfs(si, sj, ans):
    global kan_badak

    Q = deque([(si, sj)])
    visit[si][sj] = 1

    while Q:
        si, sj = Q.popleft()

        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                if arr[ni][nj] == kan_badak:
                    Q.append((ni, nj))
                    visit[ni][nj] = 1
                    ans += 1
    return ans

## 실행
# [0] 초기 설정: 시작 (0,0), 방향 d=1
si, sj, d = 0, 0, 1
final_ans = 0

for _ in range(M):
    visit = [[0] * N for _ in range(N)]
    # [1] 주사위 옮기기
    si, sj = si + di[d], sj + dj[d]
    dice_badak = jusawii(d)
    kan_badak = arr[si][sj]

    # [2] BFS 확인하고 총점 더해주기
    final_ans += bfs(si, sj, 1) * kan_badak

    # [3] 주사위면 vs 바닥 > 방향 바꾸기
    if dice_badak > kan_badak:
        d = (d+1)%4
    elif dice_badak < kan_badak:
        d = (d-1)%4

    # [4] 범위 확인 > 넘어가면 정반대로 바꾸기
    ni, nj = si + di[d], sj + dj[d]
    if not (0 <= ni < N and 0 <= nj < N):
        d = (d+2)%4

print(final_ans)