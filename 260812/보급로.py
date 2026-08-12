for TC in range(1, int(input())+1):
    N = int(input())    # 지도의 크기 NxN
    arr = [list(map(int, input())) for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]

    # 다익스트라 같음.
    # 왼쪽 또는 위로부터 그 직전 dist + 현재 칸 더했을 때 더 작은 곳을 선택
    # 상하좌우인가?? >> YES
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    from heapq import heappush, heapify, heappop

    def dijk(sw, si, sj):
        hq = []
        heappush(hq, (sw, si, sj))

        while hq:
            # 가장 비용이 적은 경로 불러오기
            cur_w, cur_i, cur_j = heappop(hq)

            # 현재 거리가 더 멀면 갱신 x
            if dist[cur_i][cur_j] < cur_w:
                continue
            # 더 짧다면 바꿔준다
            dist[cur_i][cur_j] = cur_w

            # 그 다음(오른쪽, 아래)으로 갔을 때
            for k in range(4):
                ni, nj = cur_i + di[k], cur_j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    # 현재 저장된 것보다 더 작으면 갱신
                    if dist[cur_i][cur_j] + arr[ni][nj] < dist[ni][nj]:
                        dist[ni][nj] = dist[cur_i][cur_j] + arr[ni][nj]
                        heappush(hq, (dist[ni][nj], ni, nj))

        return dist[N-1][N-1]
    print(f'#{TC} {dijk(0,0,0)}')