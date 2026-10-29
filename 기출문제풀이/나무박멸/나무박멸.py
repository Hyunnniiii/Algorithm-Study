# 1. 성장: 인접한 상하좌우 칸에 있는 나무의 수만큼 나무가 자람
# 2. 번식: 인접한 상하좌우 칸 중 벽/다른나무/제초제가 모두 없으면 번식 진행
# (번식되는 수 = 원래 칸의 나무 // 번식 가능한 칸의 수)
# 성장 & 번식은 모든 나무에서 동시에!!
# 3. 박멸: 나무가 가장 많이 박멸되는 곳에 제초제 처리
# 제초제는 대각선으로 k칸만큼 전파. 전파 도중 벽/나무 없는 칸 나오면 그쪽 방향 전파 끝
# 제초제는 c년동안 남아있다. 만약 남아있는데 뿌려지면 초기화되고 다시 c년
# 새로운 제초제 처리까지 하면 >> 기존 제초제 사라짐. 즉, 새로운 제초제 위치 선정한 다음에
# 기존꺼 시간 다 되면 없애주고, 그 다음에 제초제 뿌리기 진행

# 제출 전 확인: m=1일 때 / k = 1일 때 / 격자에 나무가 없을 때

# -1 벽 / 0 빈칸 / 양수: 나무의 수
N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for x in range(N):
    for y in range(N):
        if arr[x][y] == -1:
            arr[x][y] = -float('inf')

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 대각선
ddi = [-1,-1,1,1]
ddj = [-1,1,-1,1]

for _ in range(M):
    # [1] 성장: 동시에
    remember1 = []
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 0:
                sungjang = 0
                for k in range(4):
                    nrow, ncol = row + di[k], col + dj[k]

                    if 0 <= nrow < N and 0 <= ncol < N and arr[nrow][ncol] > 0:
                        sungjang += 1
                remember1.append(sungjang)
    idx = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 0:
                arr[row][col] += remember1[idx]
                idx += 1

    # [2] 번식: 동시에
    remember2 = []  # 나무 추가할 곳 좌표 딕셔너리로 넣기 실패;;
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 0:
                bunsik = []
                for k in range(4):
                    nrow, ncol = row + di[k], col + dj[k]

                    if 0 <= nrow < N and 0 <= ncol < N and arr[nrow][ncol] == 0:
                        bunsik.append((arr[row][col], nrow, ncol))
                remember2.append(bunsik)

    for lst in remember2:
        for llst in lst:
            arr[llst[1]][llst[2]] += llst[0] // len(lst)

    # [3] 제초제 뿌릴 곳 찾기
    max_jaecho = 0
    max_jaecho_lst = []
    for row in range(N):
        for col in range(N):
            # 탐색 가능한 곳에 대해 진행
            if arr[row][col] >= 0:
                jaecho = [(row, col)]
                jaecho_cnt = arr[row][col]
                for d in range(4):
                    for k in range(1, K+1):
                        nr, nc = row + ddi[d]*k, col + ddj[d]*k

                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > 0:
                            jaecho_cnt += arr[nr][nc]
                            jaecho.append((nr, nc))
                        else:
                            break

                if jaecho_cnt > max_jaecho:
                    max_jaecho = jaecho_cnt
                    max_jaecho_lst = jaecho

    # 박멸한 나무 개수 더하기
    ans += max_jaecho

    # [4] 제초제 시간 반영하기
    for row in range(N):
        for col in range(N):
            if arr[row][col] < 0:
                arr[row][col] += 1

    # [5] 선정된 위치에 제초제 뿌리기
    for lst in max_jaecho_lst:
        arr[lst[0]][lst[1]] = -C


print(ans)