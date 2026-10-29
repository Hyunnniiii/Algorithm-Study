# 미세먼지를 최대한 적게 마시면서 이동하고 싶음
# 가는 경로가 길어도 먼지만 적게 마시면 됨
# 갔던 길 되돌아가도 됨

# 구할 것: 총 미세먼지의 최소값

# 나으 생각
# 출발지에서부터 bfs를 하는데
# 거리대로 visit 고치는게 아니라 먼지가 나오면 1을 추가
# 근데 이제 이전에 넣은 값보다 작은 경우가 생기면 그걸로 바꾸기
# 주의: 범위 체크, 출발지가 목적지인 경우 > 답은 출발지의 값
# 출발지에 먼지가 있을 수 있음

from collections import deque

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

for TC in range(1, int(input())+1):
    # 지도 한 변의 길이 N
    N = int(input().strip())

    start_i, start_j, end_i, end_j = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[float('inf')] * N for _ in range(N)]

    def bfs(si, sj, ei, ej):
        # 큐 / visit 생성
        q = deque()
        q.append((si, sj))

        visit[si][sj] = arr[si][sj]     # 출발지 먼지 먹기

        # 출발
        while q:
            ci, cj = q.popleft()

            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]

                # 범위 체크, 더 적은 때만 갱신
                if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] > visit[ci][cj] + arr[ni][nj]:
                    visit[ni][nj] = visit[ci][cj] + arr[ni][nj]
                    q.append((ni, nj))

    bfs(start_i, start_j, end_i, end_j)

    print(f'#{TC} {visit[end_i][end_j]}')