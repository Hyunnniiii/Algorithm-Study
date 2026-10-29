# 비타민 있는 칸으로 가면 1개 획득, 비타민 사라짐
# 장애물 칸 이동 불가, 머물렀던 칸은 장애물 칸으로 변경

for TC in range(1, int(input()) + 1):
    R, C = map(int, input().split())  # R행 C열

    # 시작점 (sr, sc) / M번 이하의 이동으로 N개 이상의 비타민 먹기
    sr, sc, M, N = map(int, input().split())

    # 시작 위치는 장애물이 아님. 빈칸 또는 비타민
    # 빈 칸 0, 비타민 1, 장애물 -1
    arr = [list(map(int, input().split())) for _ in range(R)]

    # 만약 시작점에 비타민일 경우 처리, 시작점 방문처리
    if arr[sr][sc] == 1:
        N = N - 1
    arr[sr][sc] = -1

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    ans = 0
    # idx: 이동 횟수 / vit: 먹은 비타민 개수
    def eat(idx, vit, sr, sc):
        global ans
        # 종료: M번 이동하기 전에 또는 M번째에 비타민 다 채웠을 때
        if vit == N and idx <= M:
            ans = 1
            return

        # 종료: M번째까지 비타민 N개 못먹었을 때
        if idx == M:
            return

        for k in range(4):
            ni, nj = sr + di[k], sc + dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] == 0:  # 그냥 통로면
                    arr[ni][nj] = -1
                    eat(idx + 1, vit, ni, nj)
                    arr[ni][nj] = 0

                if arr[ni][nj] == 1:  # 비타민이면
                    arr[ni][nj] = -1
                    eat(idx + 1, vit + 1, ni, nj)
                    arr[ni][nj] = 1


    eat(0, 0, sr, sc)
    print(f'#{TC} {ans}')