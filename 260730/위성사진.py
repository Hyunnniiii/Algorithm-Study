W, H = map(int, input().split())   # H행, W열
mok = [list(input().strip()) for _ in range(H)]

# 방향: 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

q = []    # 방문할 목장 표시
visit = [[0]*W for _ in range(H)]   # 방문한 칸 표시
dlst = []    # 거리 배열

# 배열 순회하다가 * 나오면 시작
for i in range(H):
    for j in range(W):
        distance = 1

        if mok[i][j] == '*' and visit[i][j] == 0:
            q.append([i, j])
            visit[i][j] = 1

        while q:
            start_i, start_j = q.pop(0)
            visit[start_i][start_j] = 1     # 갔다고 표시

            for k in range(4):
                ni, nj = start_i + di[k], start_j + dj[k]

                if 0 <= ni < H and 0 <= nj < W:
                    if mok[ni][nj] == '*' and visit[ni][nj] == 0:
                        visit[ni][nj] = 1
                        q.append([ni, nj])
                        distance += 1
        dlst.append(distance)

max_dist = 0
for x in dlst:
    if x > max_dist:
        max_dist = x
print(max_dist)