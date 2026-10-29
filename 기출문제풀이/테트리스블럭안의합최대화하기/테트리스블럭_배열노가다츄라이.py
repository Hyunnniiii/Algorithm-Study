# 0. 입력받기
n, m = map(int, input().split())    # nxm 배열
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 1. 각 칸에서 상하좌우 3번 백트래킹
# 함수 정의: 각 시작점에서 상하좌우 3번 이동했을 때 숫자합 구하기
visit = [[0]*m for _ in range(n)]
max1 = 0

def tetris(move, cnt, si, sj):
    global max1

    # 종료 조건: 3번 이동했을 때
    if move == 3:
        max1 = max(max1, cnt)
        return

    # 갈 방향 선택하기
    for k in range(4):
        ni, nj = si + di[k], sj + dj[k]

        # 범위 안에 있고 방문한 적 없다면
        if 0 <= ni < n and 0 <= nj < m:
            if visit[ni][nj] == 0:

                # 해당 방향을 선택
                visit[ni][nj] = 1
                tetris(move+1, cnt+arr[ni][nj], ni, nj)
                visit[ni][nj] = 0

                # 선택 안하면? > 코드 필요 없음

#  함수 실행: 연속 블럭에서의 최댓값 구하기
for x in range(n):
    for y in range(m):
        visit[x][y] = 1
        tetris(0, arr[x][y], x, y)
        visit[x][y] = 0

# 2. 빠큐모양 처리
# 배열 만들기
yut = [((0,0), (1,0), (2,0), (1,1)),    # ㅏ
       ((1,0), (1,1), (1,2), (0,1)),    # ㅗ
       ((1,0), (0,1), (1,1), (2,1)),    # ㅓ
       ((0,0),(0,1), (0,2), (1,1))]     # ㅜ

# 배열 순회하면서 최댓값 구하기
max2 = 0
for row in range(n):
    for col in range(m):
        # 4개 모양에 대해 수행
        for blocks in range(4):
            cur_sum = 0

            # 4개 블록을 합한다
            for k in range(4):
                nr, nc = row + yut[blocks][k][0], col + yut[blocks][k][1]

                if 0 <= nr < n and 0 <= nc < m:
                    cur_sum += arr[nr][nc]

            # 합친게 기존 max보다 크면 갱신
            max2 = max(max2, cur_sum)

print(max(max1, max2))