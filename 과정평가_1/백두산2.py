# 3 <= N / M <= 50
# 마그마, 대피: 상하좌우
# 구해야 할 것: 대피소들 중 하나로 대피할 수 있는 최소시간 (** 대피 못하면 -1 출력)

# 바꿔야 할 핵심은 4개야.
#
# 사람도 한 시간마다 len(pq)개를 전부 움직여야 함
# time += 1을 이동 가능한 칸마다 하면 안 됨
# people 방문 확인이 필요함
# 한 사람 위치에서 네 방향이 막혔다고 전체 실패가 아님

from collections import deque
for T in range(1, int(input())+1):
    N, M = map(int, input().split())    # N행 M열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 마그마 먼저 채우고 -> 사람 배열 채우기
    fire = [[0]*M for _ in range(N)]
    people = [[0]*M for _ in range(N)]

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    # 마그마 큐, 사람큐
    mq = deque()
    pq = deque()

    # 마그마/사람의 시작점 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 4:
                s_pi, s_pj = i, j
                people[s_pi][s_pj] = 1
                pq.append([s_pi, s_pj])
            elif arr[i][j] == 3:
                s_mi, s_mj = i, j
                mq.append([s_mi, s_mj])
                fire[s_mi][s_mj] = 1

    # 0 암석 / 1 땅 / 2 대피소 / 3 분화구 / 4 현재위치

    # 1. 마그마: 마그마가 못 가는 곳을 제외하고(암석0, 대피소2) 1씩 늘리기
    # 2. 사람: 사람이 못 가는 곳을 제외하고(암석0, 분화구3, 마그마가 온 곳) 1씩 늘리기

    # 시작
    depi = True
    time = 1
    while depi:
        # 마그마 먼저
        for _ in range(len(mq)):
            mi, mj = mq.popleft()

            for k in range(4):
                n_mi, n_mj = mi + di[k], mj + dj[k]

                # arr 범위 내에 있으면서 마그마가 못 가는 곳(0,2), 이미 간 곳 제외
                if 0 <= n_mi < N and 0 <= n_mj < M:
                    if arr[n_mi][n_mj] != 0 and arr[n_mi][n_mj] != 2 and fire[n_mi][n_mj] != 1:
                        fire[n_mi][n_mj] = 1
                        mq.append([n_mi, n_mj])

        # 사람
        pi, pj = pq.popleft()

        no = 0
        for k in range(4):
            n_pi, n_pj = pi + di[k], pj + dj[k]

            # arr 범위 내에 있으면서 사람이 못 가는 곳(마그마, 0, 3) 제외
            if 0 <= n_pi < N and 0 <= n_pj < M:
                # 대피소를 만나면 끝
                if arr[n_pi][n_pj] == 2:
                    depi = False
                    break

                # 대피소를 못 만났으나 길은 있으면
                elif arr[n_pi][n_pj] == 1 and fire[n_pi][n_pj] == 0:
                    people[n_pi][n_pj] = time
                    pq.append([n_pi, n_pj])
                    time += 1

                # 갈 길이 없으면
                else:
                    no += 1

                # 모든 방향에서 갈 곳이 없으면 끝
                if no == 4:
                    time = -1
                    depi = False
                    break

    print(f'#{T} {time}')







