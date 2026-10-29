for TC in range(1, int(input())+1):
    # N행 M열 / 필터개수 K / 필터종류 T
    N, M, K, T = map(int, input().split())

    # 쾌적한 영역: 모든 종류의 필터가 적용 (개수 상관X)
    # 시작 행, 열은 0부터 시작
    # 종류 T가 0부터 세는거임 그래서 T=1이면 0, 1로 필터 2개. 즉 총 T+1개가 되어야 함

    # 2차원 배열의 원소를 set으로 만들기
    arr = [[set() for _ in range(M)] for _ in range(N)]

    # 각 칸마다 필터 종류 추가
    for idx in range(K):
        # 필터종류 t, 시작행 si, 시작열 sj, 필터 행 크기 h, 필터 열 크기 w
        t, si, sj, h, w = map(int, input().split())

        for i in range(si, si+h):
            for j in range(sj, sj+w):
                # 범위 체크
                if  0 <= i < N and 0 <= j < M:
                    arr[i][j].add(t)

    # T+1개 있는지 확인
    cnt = 0
    for x in range(N):
        for y in range(M):
            if len(arr[x][y]) != T+1:
                cnt += 1

    print(f'#{TC} {cnt}')








