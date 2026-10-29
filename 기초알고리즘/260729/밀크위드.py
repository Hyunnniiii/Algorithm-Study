# 가로 X, 세로 Y
C, R, mx, my = map(int, input().split())
row, col  = R - my, C - mx

arr = [list(input().strip()) for _ in range(R)]
time = [[0]*C for _ in range(R)]

# 8개 방향
dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]

milk = [[row, col]]  # 큐
arr[row][col] = '*'

# 풀 침입 시작
while milk:
    r, c = milk.pop(0)

    for k in range(8):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] == '.':
                milk.append([nr, nc])
                arr[nr][nc] = '*'
                time[nr][nc] = time[r][c] + 1

max_time = 0
for x in time:
    if max_time < max(x):
        max_time = max(x)
print(max_time)