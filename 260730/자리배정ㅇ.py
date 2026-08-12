C, R = map(int, input().split())    # C열 R행
K = int(input())    # K 관객번호

# 좌석 번호 입력할 배열
arr = [[0]*C for _ in range(R)]

# 상>우>하>좌 순서대로 이동
di = [-1,0,1,0]
dj = [0,1,0,-1]


if K > C*R :    # 좌석 부족한 경우
    print(0)

elif K == 1:    # 대기 1번인 경우
    x, y = 1, 1
    print(x, y)

else:
    # 격자에 순서대로 번호 입력
    sx, sy = R-1, 0
    arr[sx][sy] = 1
    waiting = 2

    is_ok = True
    while is_ok:
        for k in range(4):
            nx, ny = sx + di[k], sy + dj[k]

            while 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 0:
                arr[nx][ny] = waiting
                waiting += 1

                if waiting == K + 1:
                    print(ny+1, R-nx)
                    is_ok = False
                    break
                else:
                    nx, ny = nx + di[k], ny + dj[k]
            sx, sy = nx - di[k], ny - dj[k]


