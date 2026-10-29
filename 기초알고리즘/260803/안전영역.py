from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 물 높이 0부터 max값까지만 돌리기 위해 최댓값 구하기
max_height = 0
for x in arr:
    for xx in x:
        if xx > max_height:
            max_height = xx

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

max_cnt = 0    # 안전영역의 최댓값

# 비가 0부터 건물 최대 높이까지 올 때
for rain in range(0, max_height+1):

    # 준비할 리스트
    q = deque()    # 다음에 갈 곳
    visit = [[0]*N for _ in range(N)]
    cnt = 0    # 안전영역의 개수

    for x in range(N):
         for y in range(N):
            # 비보다 높고, 방문하지 않은 건물부터 탐색 시작
            if arr[x][y] > rain and visit[x][y] == 0:
                sx, sy = x, y
                q.append([sx, sy])
                visit[sx][sy] = 1
                cnt += 1

            while q:
                a, b = q.popleft()

                for k in range(4):
                    nx, ny = a + di[k], b + dj[k]

                    # 그 다음칸이 방문하지 않은 곳이면서 비보다 높으면 진행
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] > rain and visit[nx][ny] == 0:
                            q.append([nx, ny])
                            visit[nx][ny] = 1

    # 배열 한바퀴 돌면 집계
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)

