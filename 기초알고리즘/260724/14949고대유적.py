for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*M for _ in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    lr = []
    ud = []

    for i in range(N):
        for j in range(M):
            # 해당 블록이 1일 때 탐사 시작
            if arr[i][j] == 1:
                # 좌우 방향
                count = 1
                nj = j+1
                while nj<M and arr[i][nj]==1:
                    count+=1
                    nj += 1
                lr.append(count)

                # 상하 방향
                count = 1
                ni = i+1
                while ni<N and arr[ni][j]==1:
                    count += 1
                    ni += 1
                ud.append(count)
    lr = max(lr)
    ud = max(ud)


    print(f'#{test_case}', max(lr, ud))