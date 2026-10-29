# 5 <= N <= 15, 2 <= M <= N
# NxN 배열에 MxM 파리채

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 배열 순회하면서 최댓값 갱신
    max_pari = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            pari_num = 0

            for r in range(i, i+M):
                for c in range(j, j+M):
                    pari_num += arr[r][c]
            if pari_num > max_pari:
                max_pari = pari_num
    print(f'#{T} {max_pari}')

    # max_pari = 0
    # for i in range(N-M+1):
    #     for j in range(N-M+1):
    #         pari = arr[i][j]
    #         for k in range(3):
    #                 ni, nj = i + di[k], j + dj[k]
    #                 pari += arr[ni][nj]
    #         if max_pari < pari:
    #             max_pari = pari
    # print(f'#{T} {max_pari}')
    #
    # 이 코드는 2x2만 가능한 코드 (오른쪽, 아래, 대각선 정의)
