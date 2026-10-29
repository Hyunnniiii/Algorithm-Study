for T in range(1, int(input())+1):
    N, M = map(int, input().split())    # N행 M열

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    max_pang = 0
    for i in range(N):
        for j in range(M):
            pang = arr[i][j]

            for step in range(1, pang+1):
                for k in range(4):
                    ni, nj = i + di[k]*step, j + dj[k]*step

                    if 0 <= ni < N and 0 <= nj < M:
                        pang += arr[ni][nj]

            if pang > max_pang:
                max_pang = pang

    print(f'#{T} {max_pang}')
