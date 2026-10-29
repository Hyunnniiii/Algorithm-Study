# 3 <= N <= 20 / 0 <= H <= 10 (H는 높이)
# 한 구역이 상하좌우보다 위험도 높으면 활화산
# 가장자리: 활화산 판단 불가 -> 가장자리에 있으면 범위 내 상하좌우보다 커도 활화산이 아니다

# 구할 것: 활화산 위험도의 (최대 - 최소)값
# 영역 내 활화산이 **1개 또는 없으면** -1

for T in range(1, int(input())+1):

    N = int(input())    # N: 구역의 크기 (NxN)
    arr = [list(map(int, input().split())) for _ in range(N)]
    hwasan = [[0]*N for _ in range(N)]  # 활화산만 표시할 배열

    # 상하좌우 방향
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    # 배열 탐색하기: 가장자리는 탐색 X
    for i in range(1, N-1):
        for j in range(1, N-1):
            max_san = arr[i][j]
            is_hwal = 0

            for k in range(4):
                ni, nj = i + di[k], j + dj[k]

                # 탐색할 곳이 범위 내에 있으면 비교
                if 0 <= ni < N and 0 <= nj < N:
                    if max_san <= arr[ni][nj]:
                        break
                    else:
                        is_hwal += 1

                # 주변 4군데보다 모두 크면 활화산 배열에 추가
                if is_hwal == 4:
                    hwasan[i][j] = arr[i][j]

    # 활화산의 최대-최소 구하기
    final = []
    for x in range(N):
        for y in range(N):
            # 활화산이 있으면
            if hwasan[x][y] != 0:
                final.append(hwasan[x][y])

    # 활화산이 1개이거나, 없으면 -1
    if len(final) == 1 or len(final) == 0:
        print(f'#{T}', -1)
    else:
        print(f'#{T} {max(final)-min(final)}')