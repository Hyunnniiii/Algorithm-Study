
# 방화벽 세울 3군데 정하고 그때 불이 퍼지는거 시뮬 한 다음에 불 안퍼지는 영역의 크기를 구하면 됨
# 0. 입력받기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 방화벽을 세울 3군데 정하기: 조합
lst = []
for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            lst.append([x,y])

llst = []
def choose(idx, selected):
    global llst
    # 종료: 3개 위치 골랐을 때
    if len(selected) == 3:
        llst.append(selected)
        return

    # 고르기
    for k in range(idx, len(lst)):
        choose(k + 1, selected + [lst[k]])

choose(0, [])

# 2. 지정한 3군데에 세웠을 때 불 다 퍼질 때까지 돌리기
# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

from collections import deque
def bfs(arr):      # 각 3개 방화벽 조합마다 총 불의 개수 세는 함수
    cnt = 0     # 총 불의 개수
    visit = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            # 불이 있으면 시작
            if arr[x][y] == 2:
                visit[x][y] = 1
                q = deque()
                q.append((x, y))
                cnt += 1

                while q:
                    cur_x, cur_y = q.popleft()
                    for k in range(4):
                        ni, nj = cur_x + di[k], cur_y + dj[k]

                        if 0 <= ni < n and 0 <= nj < m:
                            if arr[ni][nj] == 0 and visit[ni][nj] == 0:
                                visit[ni][nj] = 1
                                cnt += 1
                                q.append((ni, nj))
    return cnt

import copy
ans = float('inf')
for i in range(len(llst)):
    arr2 = copy.deepcopy(arr)
    for j in range(3):
        a, b = llst[i][j][0], llst[i][j][1]
        arr2[a][b] = 1

        ans = min(ans, bfs(arr2))

# 3. 불이 퍼지지 않는 최대 영역 구하기
b_cnt = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            b_cnt += 1

print(n*m-ans-3-b_cnt)