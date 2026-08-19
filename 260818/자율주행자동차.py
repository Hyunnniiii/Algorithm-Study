# 1. 왼쪽으로 간 적 없으면 좌회전해서 그 방향으로 1칸 전진
# 2. 왼쪽이 인도 / 이미 방문한 도로이면 다시 좌회전하고 1번
# 3. 2번 과정을 4방향에 대해 했으나 전진 못했으면 현재 방향에서 한 칸 후진하고 1번
# 4. 3번 과정에서 후진도 못하면 끝

# 구할 것: 방문한 도로의 총 면적

# [1] 입력 받기
n, m = map(int, input().split())    # n x m 도로
x, y, d = map(int, input().split())     # 초기위치, 방향
arr = [list(map(int, input().split())) for _ in range(n)]   # 도로 상태

# [2] 필요한 세팅

# 방향 (북동남서)
di = [-1,0,1,0]
dj = [0,1,0,-1]

cnt = 1     # 거쳐간 도로의 총 면적
fail_cnt = 0
visit = [[0]*m for _ in range(n)]   # 방문한 도로 표시
visit[x][y] = 1

# [3] 시작
status = True
while status:
    # 좌회전 먼저!!
    d -= 1

    # 회전한 방향으로 다음 칸 갈 수 있는가?
    ni, nj = x + di[d%4], y + dj[d%4]

    # 갈 수 있을 때
    if arr[ni][nj] == 0 and visit[ni][nj] == 0:
        x, y = ni, nj
        visit[x][y] = 1
        cnt += 1
        fail_cnt = 0

    # 갈 수 없을 때
    else:
        fail_cnt += 1

    # 4방향 모두 확인했으나 못 간 경우 > 후진
    if fail_cnt == 4:
        fail_cnt = 0
        back_x, back_y = x - di[d%4], y - dj[d%4]

        if arr[back_x][back_y] == 1:
            status = False
            break
        x, y = back_x, back_y

print(cnt)