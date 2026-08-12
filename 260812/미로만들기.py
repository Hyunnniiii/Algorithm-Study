N = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(N)]

# i hate mirro
# 상하좌우로 쭉 가다가 검은방이 나오면 +1 해주고, 그 칸을 흰색 처리
# 그렇게 계속 진행해서 마지막칸에 도달했을 때 최소인 걸 찾기
# 근데 이걸 일일히 하면 오래걸릴 것이기 때문에
# 아까 보급로 문제처럼 똑같은 칸을 지울 때 이전에 좀 덜 지운걸로 갱신해서 가보면 어떨까

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 최소 거리 표시할 2차원 배열
dist = [[float('inf')]*N for _ in range(N)]

from heapq import heappush, heappop

def mirro(si, sj):
    q = []
    heappush(q, (0, si, sj))    # 지금까지의 거리, 현재 위치
    dist[si][sj] = 0

    while q:
        cur_dist, cur_i, cur_j = heappop(q)

        for k in range(4):
            ni, nj = cur_i + di[k], cur_j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 다음칸이 흰 방일 때
                if arr[ni][nj] == 1:
                    # 길이 짧을 때만 바꿔주고, 그 다음 경로로 추가
                    if dist[ni][nj] > dist[cur_i][cur_j]:
                        dist[ni][nj] = dist[cur_i][cur_j]
                        heappush(q, (dist[ni][nj], ni, nj))

                # 다음칸이 검은 방일 때
                if arr[ni][nj] == 0:
                    # 길이 짧을 때만 바꿔주고, 그 다음 경로로 추가
                    if dist[ni][nj] > dist[cur_i][cur_j] + 1:
                        dist[ni][nj] = dist[cur_i][cur_j] + 1
                        heappush(q, (dist[ni][nj], ni, nj))

mirro(0,0)
print(dist[N-1][N-1])