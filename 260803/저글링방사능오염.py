# 3초 뒤에 죽음 -> 일단 시간 표시해놓고 제일 마지막에 +2
# 1 저글링 O / 0에는 저글링 없음
# 열/행 순서로 주고, 좌표의 시작이 1 주의
from collections import deque

C, R = map(int, input().split())    # R행 C열
arr = [list(map(int, input())) for _ in range(R)]

# 상하좌우 방향
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 시작점 입력 받기
start_j, start_i = map(int, input().split())
start_i, start_j = start_i - 1, start_j - 1

# 필요한 리스트 생성
q = deque()     # 방문할 곳
q.append([start_i, start_j])
visit = [[0]*C for _ in range(R)]      # 이미 지나온 곳 & 시간
visit[start_i][start_j] = 1
arr[start_i][start_j] = 0

# 시작
while q:
    si, sj = q.popleft()

    for k in range(4):
        ni, nj = si + di[k], sj + dj[k]

        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] == 1 and visit[ni][nj] == 0:
                visit[ni][nj] = visit[si][sj] + 1   # 시간 및 방문 표시
                q.append([ni, nj])  # 앞으로 갈 곳 추가
                arr[ni][nj] = 0    # 죽은 저글링 표시

# 정산
zero = 0
max_time = 0
for x in range(R):
    for y in range(C):
        if arr[x][y] == 1:
            zero += 1
        if visit[x][y] > max_time:
            max_time = visit[x][y]
print(max_time + 2)   # 3초 뒤에 죽음!
print(zero)





