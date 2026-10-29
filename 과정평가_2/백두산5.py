for TC in range(1, int(input())+1):
    N, M = map(int, input().split())    # N행 M열
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [[0]*M for _ in range(N)]   # 분화구 표시

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    # 1. 분화구 찾기
    for x in range(N):
        for y in range(M):

            # 암석지대가 아니면 살펴보기
            if arr[x][y] != 0:
                fire = 1
                # 주변 4방향보다 크면 분화구
                for k in range(4):
                    ni, nj = x + di[k], y + dj[k]

                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[x][y] <= arr[ni][nj]:
                            fire = 0
                            break

                if fire == 1:
                    v[x][y] = 1

    # 분화구 좌표 구하기
    flst = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 1:
                flst.append([i, j])
                cnt += 1


    lst = []
    # 2. 2군데 이상 분화구가 있을 때 분출 면적 구하기
    if len(flst) >= 2:
        for i in range(len(flst)):
            count = 0
            a, b = flst[i][0], flst[i][1]

            for k in range(4):
                ni, nj = a + di[k], b + dj[k]

                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] != 0:
                         count += 1
            lst.append(count)

        llst = []
        for x in range(len(lst)-1):
            for y in range(x+1, len(lst)):
                hap = lst[x] + lst[y]
                llst.append(hap+2)
        print(f'#{TC}', max(llst))

    # 2. 2군데 이상 분화구가 있지 않을 때
    elif len(flst) == 1:
        count = 0
        a, b = flst[0][0], flst[0][1]

        for k in range(4):
            ni, nj = a + di[k], b + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] != 0:
                    count += 1
        lst.append(count)


        llst = []
        for x in range(len(lst) - 1):
            for y in range(x + 1, len(lst)):
                hap = lst[x] + lst[y]
                llst.append(hap + 2)
        print(f'#{TC}', llst[0])

    else:
        print(f'#{TC}', 0)