# N x M 토마토 창고
# 1 익은 토마토 / 0 토마토 / -1 토마토 없음
# 구할 것: 며칠이 지나면 토마토가 모두 익는지

# 토마토가 존재하는 곳의 좌표를 전부 큐에 넣은 다음에 bfs를 돌리기
# 가까운 곳에 알아서 먼저 작은 숫자 채워짐

from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 토마토 존재하는 좌표 전부 큐에 넣기
q = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            q.append([x, y])

# bfs 함수 정의
def tomato():
    while q:
        si, sj = q.popleft()

        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = arr[si][sj] + 1
                    q.append([ni, nj])
tomato()

# 결과 출력: 처음 익은 토마토의 값이 1이었으므로 정답에서 1 빼줘야 함
ans = -2
for x in range(N):
    for y in range(M):
        # 가장 오래된 날짜 구하기
        ans = max(ans, arr[x][y])
        # 익지 않은 토마토가 남아있으면
        if arr[x][y] == 0:
            ans = -1
            break
    if ans == -1:
        break

# 이미 모두 익어있었다면 > ans = 1
if ans == 1:
    print(0)

# 익지 않은 토마토가 있었다면 > ans = -1
elif ans == -1:
    print(ans)

else:
    print(ans-1)