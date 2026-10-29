
# 뭔소리임??

# NxN 미지 공간에 갇힘. 탈출해야 함
# 미지 공간의 어딘가에 정육면체 형태의 시간의 벽 존재
# 빈 공간 0, 장애물 1
# 초기에 시간의 벽 윗면 어딘가에서 시작. (2로 주어짐)
# 시간의 벽 위치 3, 탈출구 4
# 탈출구는 시간의 벽 외부 바닥에 위치
# 시간의 벽에서 미지의 공간 바닥으로 이어질 수 있는 출구는 하나이다
# 시간 이상 현상: 매 v의 배수 턴마다 d로 한칸씩 확산. 계속 지속됨. 빈칸으로만 확산.
# 더 확산될 수 없으면 멈춘다. 독립적 & 동시에 확산
# 시간 이상 현상이 확산된 후에 타임머신 이동

# 매 턴 상하좌우 한 칸씩 이동
# 목표: 장애물과 시간 이상 현상을 피해 탈출구까지 도달하기 위한 최소 시간 구하기 (불가하면 -1)

# 시간 이상 현상은 미지의 공간 바닥에만 F개 존재.
# 정육면체는 항상 공간 내부에 딱 들어가는가? > yes
# 시간의 벽에서 무조건 탈출 가능? > 아닌듯
# 탈출구 하나? > yes
# ================================
from collections import deque

# 미지공간 범위
def in_range_big(nr,nc):
    return 0<=nr<N and 0<=nc<N

# 미지의 벽 범위
def in_range_small(nr, nc):
    return 0<=nr<M and 0<=nc<4*M

# 출구 좌표가 시간의 벽에서 어딘지 구하기
def find_exit_coord(sr,sc,er,ec,d):
    if d == 0:  # 동
        return M-1 - (er-sr)
    if d==1:    # 북
        return 2*M-1 - (ec-sc)
    if d==2:    # 서
        return 2*M + (er-sr)
    if d==3:    # 남
        return 3*M + (ec-sc)

# 시간의 벽에서 나가는 경로 구하기
def bfs():
    for r in range(M):
        for c in range(M):
            if centrl[r][c]==2:
                Q = deque([[r,c,0]])    # 0은 윗면 / 1은 옆면
                c_visit[r][c] = 0

                while Q:
                    sr, sc, sm = Q.popleft()

                    for k in range(4):
                        nr, nc = sr + dr[k], sc + dc[k]
                        nm = sm

                        # 현재 중앙에 있는 경우
                        if sm == 0:
                            # 중앙 > 남
                            if nr == M:
                                nr, nc, nm = 0, 3*M + sc, 1

                            # 중앙 > 북
                            elif nr == -1:
                                nr, nc, nm = 0, 2*M-1-sc, 1

                            # 중앙 > 동
                            elif nc == M:
                                nr, nc, nm = 0, M-1-sr, 1

                            # 중앙 > 서
                            elif nc == -1:
                                nr, nc, nm = 0, 2*M+sr, 1

                        # 현재 옆면에 있는 경우
                        else:
                            # 옆면 > 중앙
                            if nr == -1:

                                if 0 <= nc < M:          # 동
                                    nr, nc, nm = M-1-sc, M-1, 0

                                elif M <= nc < 2*M:      # 북
                                    nr, nc, nm = 0, 2*M-1-sc, 0

                                elif 2*M <= nc < 3*M:    # 서
                                    nr, nc, nm = sc-2*M, 0, 0

                                else:                    # 남
                                    nr, nc, nm = M-1, sc-3*M, 0

                            # 옆면 아래로 벗어남
                            elif nr == M:
                                continue

                            # 남 > 동
                            elif nc == 4*M:
                                nc = 0

                            # 동 > 남
                            elif nc == -1:
                                nc = 4*M-1


                        # 이제 방문 처리
                        # 도착한 곳 중앙일 때
                        if nm == 0:
                            # 미방문, 벽 확인
                            if c_visit[nr][nc] != -1 or centrl[nr][nc]==1:
                                continue

                            if sm == 0:
                                c_visit[nr][nc] = c_visit[sr][sc] + 1
                            elif sm == 1:
                                c_visit[nr][nc] = n_visit[sr][sc] + 1

                        else:
                            # 미방문, 벽 확인
                            if n_visit[nr][nc] != -1 or nxt[nr][nc] == 1:
                                continue

                            if sm == 0:
                                n_visit[nr][nc] = c_visit[sr][sc] + 1
                            elif sm == 1:
                                n_visit[nr][nc] = n_visit[sr][sc] + 1

                        Q.append([nr, nc, nm])


###########################
N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 동서남북 배열
east = [list(map(int, input().split())) for _ in range(M)]
west = [list(map(int, input().split())) for _ in range(M)]
south = [list(map(int, input().split())) for _ in range(M)]
north = [list(map(int, input().split())) for _ in range(M)]
nxt = [[] for _ in range(M)]
for r in range(M):
    nxt[r] = east[r] + north[r] + west[r] + south[r]    # 동북서남

# 중앙 배열
centrl = [list(map(int, input().split())) for _ in range(M)]

# 이상 현상
weird = []
for _ in range(F):
    r, c, d, v = map(int, input().split())
    weird.append([r,c,d,v])

# 4방향(우상좌하)
dr = [0,-1,0,1]
dc = [1,0,-1,0]

# 이상현상 4방향(우좌하상)
di = [0,0,1,-1]
dj = [1,-1,0,0]

# 시간의 벽 좌상단 위치 구하기
for r in range(N-1,-1,-1):
    for c in range(N-1,-1,-1):
        if arr[r][c] == 3:
            start_r, start_c = r, c

# 출구 위치 구하기
for r in range(N):
    for c in range(N):
        if arr[r][c] == 3:
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]

                if in_range_big(nr,nc) and arr[nr][nc] == 0:
                    exit_r, exit_c, exit_d = nr, nc, k
        if arr[r][c] == 4:
            real_exit_r, real_exit_c = r, c

# 시간의 벽 배열에서의 출구 위치
in_exit_r, in_exit_c = M-1, find_exit_coord(start_r,start_c,exit_r,exit_c, exit_d)

# 시간의 벽에서 나가는 경로 구하기
c_visit = [[-1]*M for _ in range(M)]
n_visit = [[-1]*(4*M) for _ in range(M)]
bfs()
real_time = n_visit[in_exit_r][in_exit_c]   # 출구 앞까지 내려오는데 걸린 시간
if real_time != -1:
    real_time += 1
ans = -1

# 그러면 이제 해당 시간 동안 일어난 시간 이상 현상 반영해주기
# 이상현상 칸은 7로 표시하겠음
if real_time != -1:
    for w in weird:
        i,j,d,v = w[0], w[1], w[2], w[3]
        arr[i][j] = 7

        for _ in range(real_time//v):
            ni, nj = i+di[d], j+dj[d]
            if not in_range_big(ni, nj) or arr[ni][nj] in (1,3,4):
                break
            arr[ni][nj] = 7
            i, j = ni, nj

            print('이상 현상 반영')
            for row in arr:
                print(row)
        w[0], w[1] = i, j   # 다음에 여기서부터 시작하세요

    # 찐 bfs 시작
    # 출구 좌표에서 시작해서 bfs를 수행한다
    # 이때 시간 이상 현상 반영해주고 시작하는 거임
    if arr[exit_r][exit_c] == 7:
        ans = -1
    else:
        Q = deque([[exit_r, exit_c]])
        real_visit = [[0] * N for _ in range(N)]
        real_visit[exit_r][exit_c] = real_time

        ans = -1

        while Q:
            si, sj = Q.popleft()

            # 시간 체크
            # 새로운 거리가 나오면 > 시간 +1
            if real_visit[si][sj]+1 != real_time:
                print('새로운 거리 등장, 시간 +1')
                real_time += 1
                print('시간은 :', real_time)

                # 이상 현상 표시
                for w in weird:
                    r, c, d, v = w[0], w[1], w[2], w[3]
                    print('이상 현상 현황', w)
                    if real_time%v==0:
                        nr, nc = r + di[d], c + dj[d]
                        if not in_range_big(nr,nc) or arr[nr][nc] in (1,3,4):
                            continue
                        arr[nr][nc] = 7
                        w[0], w[1] = nr, nc

                        print('이상 현상 표시')
                        for row in arr:
                            print(row)
                        print()

            # 한 칸 이동
            for k in range(4):
                ni, nj = si + di[k], sj + dj[k]

                # 범위 내, 미방문, 이상현상 확인
                if not in_range_big(ni, nj) or real_visit[ni][nj]:
                    continue
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 7:
                    continue
                # 탈출구
                if arr[ni][nj] == 4:
                    real_visit[ni][nj] = real_visit[si][sj] + 1
                    ans = real_visit[si][sj] + 1
                    Q = []
                    break
                # 빈칸
                Q.append((ni,nj))
                real_visit[ni][nj] = real_visit[si][sj] + 1
                print('다음 경로로 이동')
                for row in real_visit:
                    print(row)
                print()

print(ans)











# 뭔소리임??

# NxN 미지 공간에 갇힘. 탈출해야 함
# 미지 공간의 어딘가에 정육면체 형태의 시간의 벽 존재
# 빈 공간 0, 장애물 1
# 초기에 시간의 벽 윗면 어딘가에서 시작. (2로 주어짐)
# 시간의 벽 위치 3, 탈출구 4
# 탈출구는 시간의 벽 외부 바닥에 위치
# 시간의 벽에서 미지의 공간 바닥으로 이어질 수 있는 출구는 하나이다
# 시간 이상 현상: 매 v의 배수 턴마다 d로 한칸씩 확산. 계속 지속됨. 빈칸으로만 확산.
# 더 확산될 수 없으면 멈춘다. 독립적 & 동시에 확산
# 시간 이상 현상이 확산된 후에 타임머신 이동

# 매 턴 상하좌우 한 칸씩 이동
# 목표: 장애물과 시간 이상 현상을 피해 탈출구까지 도달하기 위한 최소 시간 구하기 (불가하면 -1)

# 시간 이상 현상은 미지의 공간 바닥에만 F개 존재.
# 정육면체는 항상 공간 내부에 딱 들어가는가? > yes
# 시간의 벽에서 무조건 탈출 가능? > 아닌듯
# 탈출구 하나? > yes
# ================================
from collections import deque

# 미지공간 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

# 출구 좌표가 시간의 벽에서 어딘지 구하기
def find_exit_coord(sr,sc,er,ec,d):
    if d == 0:  # 동
        return M-1 - (er-sr)
    if d==1:    # 북
        return 2*M-1 - (ec-sc)
    if d==2:    # 서
        return 2*M + (er-sr)
    if d==3:    # 남
        return 3*M + (ec-sc)

###########################
N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 동서남북 배열
east = [list(map(int, input().split())) for _ in range(M)]
west = [list(map(int, input().split())) for _ in range(M)]
south = [list(map(int, input().split())) for _ in range(M)]
north = [list(map(int, input().split())) for _ in range(M)]
nxt = [[] for _ in range(M)]
for r in range(M):
    nxt[r] = east[r] + north[r] + west[r] + south[r]    # 동북서남

# 중앙 배열
centrl = [list(map(int, input().split())) for _ in range(M)]

# 이상 현상
weird = []
for _ in range(F):
    r, c, d, v = map(int, input().split())
    weird.append([r,c,d,v])

# 4방향(우상좌하)
dr = [0,-1,0,1]
dc = [1,0,-1,0]

# 이상현상 4방향(우좌하상)
di = [0,0,1,-1]
dj = [1,-1,0,0]

# 시간의 벽 좌상단 위치 구하기
for r in range(N-1,-1,-1):
    for c in range(N-1,-1,-1):
        if arr[r][c] == 3:
            start_r, start_c = r, c

# 출구 위치 구하기
for r in range(N):
    for c in range(N):
        if arr[r][c] == 3:
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]

                if in_range(nr,nc) and arr[nr][nc] == 0:
                    exit_r, exit_c, exit_d = nr, nc, k
        if arr[r][c] == 4:
            real_exit_r, real_exit_c = r, c

# 시간의 벽 배열에서의 출구 위치
in_exit_r, in_exit_c = M-1, find_exit_coord(start_r,start_c,exit_r,exit_c, exit_d)
print('출구 위치', exit_r, exit_c)
print('시간의 벽 배열에서 출구 위치', in_exit_r, in_exit_c)

# 시간의 벽에서 나가는 경로 구하기
# 1. 중앙에서 먼저 bfs
c_visit = [[-1] * M for _ in range(M)]
for r in range(M):
    for c in range(M):
        if centrl[r][c] == 2:
            Q = deque([[r, c]])
            c_visit[r][c] = 0

            while Q:
                sr, sc = Q.popleft()
                for k in range(4):
                    nr, nc = sr+dr[k], sc+dc[k]

                    # 범위 내, 미방문, 벽 체크
                    if not (0<=nr<M and 0<=nc<M) or c_visit[nr][nc]!=-1:
                        continue
                    if centrl[nr][nc] == 1:
                        continue

                    # 진행 가능하면 표시
                    c_visit[nr][nc] = c_visit[sr][sc]+1
                    Q.append([nr,nc])
            print('중앙 이동 완료')
            for row in centrl:
                print(row)
            print()
            for row in c_visit:
                print(row)
            print()
            print('=======')



# 4가지 경우에 대해 bfs 돌리기 (동서남북으로 시작)
hubo = []
for r in range(M-1,-1,-1):  # 동
    if c_visit[r][M-1] != -1 and nxt[0][M-1-r] != 1:
        e_visit = [[-1] * (4 * M) for _ in range(M)]
        Q = deque([[0, M-1-r]])
        e_visit[0][M-1-r] = c_visit[r][M-1] + 1

        while Q:
            sr, sc = Q.popleft()
            for k in range(4):
                nr, nc = sr + dr[k], (sc + dc[k])%(4*M)

                # 범위 내, 미방문, 벽 체크
                if not 0<=nr<M or e_visit[nr][nc] != -1:
                    continue
                if nxt[nr][nc] == 1:
                    continue

                # 만약 종료 지점이라면 > 바로 끝
                if nr==in_exit_r and nc==in_exit_c:
                    e_visit[nr][nc] = e_visit[sr][sc] + 1
                    hubo.append(e_visit[nr][nc])
                    break

                # 진행 가능하면 표시
                e_visit[nr][nc] = e_visit[sr][sc] + 1
                Q.append([nr, nc])
        print('동쪽 이동 완료')
        for row in nxt:
            print(row)
        print()
        for row in e_visit:
            print(row)
        print()
        print('=======')

for r in range(M):  # 서
    if c_visit[r][0] != -1 and nxt[0][2*M+r] != 1:
        w_visit = [[-1] * (4 * M) for _ in range(M)]
        Q = deque([[0, 2*M+r]])
        w_visit[0][2*M+r] = c_visit[r][0] + 1

        while Q:
            sr, sc = Q.popleft()
            for k in range(4):
                nr, nc = sr + dr[k], (sc + dc[k])%(4*M)

                # 범위 내, 미방문, 벽 체크
                if not 0<=nr<M or w_visit[nr][nc] != -1:
                    continue
                if nxt[nr][nc] == 1:
                    continue

                # 만약 종료 지점이라면 > 바로 끝
                if nr==in_exit_r and nc==in_exit_c:
                    w_visit[nr][nc] = w_visit[sr][sc] + 1
                    hubo.append(w_visit[nr][nc])
                    break

                # 진행 가능하면 표시
                w_visit[nr][nc] = w_visit[sr][sc] + 1
                Q.append([nr, nc])
        print('서쪽 이동 완료')
        for row in nxt:
            print(row)
        print()
        for row in w_visit:
            print(row)
        print()
        print('=======')

for c in range(M):  # 남
    if c_visit[M-1][c] != -1 and nxt[0][3*M+c] != 1:
        s_visit = [[-1] * (4 * M) for _ in range(M)]
        Q = deque([[0, 3*M+c]])
        s_visit[0][3*M+c] = c_visit[M-1][c] + 1

        while Q:
            sr, sc = Q.popleft()
            for k in range(4):
                nr, nc = sr + dr[k], (sc + dc[k])%(4*M)

                # 범위 내, 미방문, 벽 체크
                if not 0<=nr<M or s_visit[nr][nc] != -1:
                    continue
                if nxt[nr][nc] == 1:
                    continue

                # 만약 종료 지점이라면 > 바로 끝
                if nr==in_exit_r and nc==in_exit_c:
                    s_visit[nr][nc] = s_visit[sr][sc] + 1
                    hubo.append(s_visit[nr][nc])
                    break

                # 진행 가능하면 표시
                s_visit[nr][nc] = s_visit[sr][sc] + 1
                Q.append([nr, nc])
        print('남쪽 이동 완료')
        for row in nxt:
            print(row)
        print()
        for row in s_visit:
            print(row)
        print()
        print('=======')

for c in range(M-1,-1,-1):  # 북
    if c_visit[0][c] != -1 and nxt[0][2*M-c-1] != 1:
        n_visit = [[-1] * (4 * M) for _ in range(M)]
        Q = deque([[0, 2*M-c-1]])
        n_visit[0][2*M-c-1] = c_visit[0][c] + 1

        while Q:
            sr, sc = Q.popleft()
            for k in range(4):
                nr, nc = sr + dr[k], (sc + dc[k])%(4*M)

                # 범위 내, 미방문, 벽 체크
                if not 0<=nr<M or n_visit[nr][nc] != -1:
                    continue
                if nxt[nr][nc] == 1:
                    continue

                # 만약 종료 지점이라면 > 바로 끝
                if nr==in_exit_r and nc==in_exit_c:
                    n_visit[nr][nc] = n_visit[sr][sc] + 1
                    hubo.append(n_visit[nr][nc])
                    break

                # 진행 가능하면 표시
                n_visit[nr][nc] = n_visit[sr][sc] + 1
                Q.append([nr, nc])
        print('북쪽 이동 완료')
        for row in nxt:
            print(row)
        print()
        for row in n_visit:
            print(row)
        print()
        print('=======')

print(hubo)
if not hubo:
    ans = -1
else:
    real_time = min(hubo)
    ans = real_time

# 그러면 이제 해당 시간 동안 일어난 시간 이상 현상 반영해주기
if ans != -1:
    for w in weird:
        i,j,d,v = w[0], w[1], w[2], w[3]
        arr[i][j] = 3

        for _ in range(ans//v):
            ni, nj = i+di[d], j+dj[d]
            if not in_range(ni, nj) and arr[ni][nj] != 0:
                continue
            arr[ni][nj] = 3
            i, j = ni, nj
        w[0], w[1] = i, j   # 다음에 여기서부터 시작하세요


    # 찐 bfs 시작
    # 출구 좌표에서 시작해서 bfs를 수행한다
    # 이때 시간 이상 현상 반영해주고 시작하는 거임
    Q = deque([[exit_r, exit_c]])
    real_visit = [[0] * N for _ in range(N)]
    real_visit[exit_r][exit_c] = real_time + 1
    real_time += 1

    while Q:
        si, sj = Q.popleft()
        if real_visit[si][sj]+1 != real_time:
            print('새로운 거리 등장, 시간 +1')
            real_time += 1
            print('시간은 :', real_time)

            # 이상 현상 표시
            for w in weird:
                r, c, d, v = w[0], w[1], w[2], w[3]
                print('이상 현상 현황', w)
                if real_time%v==0:
                    nr, nc = r + di[d], c + dj[d]
                    if arr[nr][nc] != 0 or not in_range(nr,nc):
                        continue
                    arr[nr][nc] = 3
                    w[0], w[1] = nr, nc

                    print('이상 현상 표시')
                    for row in arr:
                        print(row)
                    print()

        # 한 칸 이동
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]

            # 범위 내, 미방문, 이상현상 확인
            if not in_range(ni, nj) or real_visit[ni][nj]:
                continue
            if arr[ni][nj] == 1 or arr[ni][nj] == 3:
                continue
            # 탈출구
            if arr[ni][nj] == 4:
                real_visit[ni][nj] = real_visit[si][sj] + 1
                ans = real_visit[si][sj] + 1
                Q = []
                break
            # 빈칸
            Q.append((ni,nj))
            real_visit[ni][nj] = real_visit[si][sj] + 1
            print('다음 경로로 이동')
            for row in real_visit:
                print(row)
            print()

    if real_visit[real_exit_r][real_exit_c] == 0:
        ans = -1
print(ans)








