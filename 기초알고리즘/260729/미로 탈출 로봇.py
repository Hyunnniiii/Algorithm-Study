C, R = map(int, input().split())    # 가로 C, 세로 R
start_C, start_R, end_C, end_R = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(R)]

q = [[start_R - 1, start_C - 1]]  # 갈 수 있는 길의 좌표 큐
dist = [[-1]*C for _ in range(R)]   # 거리 표시할 배열
dist[start_R - 1][start_C - 1] = 0

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

while q:
    cur_r, cur_c = q.pop(0)

    for k in range(4):
        nr, nc = cur_r + dr[k], cur_c + dc[k]

        if 0 <= nr < R and 0 <= nc < C:
            # 길이 열려있을 때
            if miro[nr][nc] == 0:
                q.append([nr, nc])
                miro[nr][nc] = 1
                dist[nr][nc] = dist[cur_r][cur_c] + 1

print(dist[end_R - 1][end_C - 1])