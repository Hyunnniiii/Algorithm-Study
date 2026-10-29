# 모든 신입사원은 K개의 명함을 가진다
# 8방향의 인접한 신입에게 명함 전달
# I 성향: 12시부터 시계 방향 / E 성향: 12시부터 반시계 방향
# 방향 왜 알려준거지? >> K개가 다 사라지면 더이상 주고싶어도 못 준다!
# 범위 체크하기
# 한 바퀴 돌았는데 소진 안하면 다시 또 돌아야됨?? > 아님

# 구할 것: 전달된 명함의 총 개수

# 내향형의 방향
idi = [-1, -1, 0, 1, 1, 1, 0, -1]
idj = [0, 1, 1, 1, 0, -1, -1, -1]

# 외향형의 방향
edi = [-1, -1, 0, 1, 1, 1, 0, -1]
edj = [0, -1, -1, -1, 0, 1, 1, 1]

# 0: 빈자리 / 1: I 성향 / 2: E 성향
for TC in range(1, int(input()) + 1):
    # N행 M열 / 명함개수 K개
    N, M, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]  # 명함 개수 표시

    for row in range(N):
        for col in range(M):
            # 사람 있으면 명함 나눠주기 시작
            if arr[row][col] != 0:
                idx = 0

                if arr[row][col] == 1:  # 내향형 인간
                    for k in range(8):

                        if idx == K:
                            break

                        ni, nj = row + idi[k], col + idj[k]

                        # 범위 내에 있고 사람이 있다면
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                            visit[ni][nj] += 1
                            idx += 1

                elif arr[row][col] == 2:  # 외향형 인간
                    for k in range(8):

                        if idx == K:
                            break

                        ni, nj = row + edi[k], col + edj[k]

                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                            visit[ni][nj] += 1
                            idx += 1

    ans = 0
    for x in range(N):
        for y in range(M):
            ans += visit[x][y]

    print(f'#{TC} {ans}')


# 나으 생각
# 일단 배열 순회하면서 0이 아니면 시작
# 1/2에 따라 정해진 di/dj 순서대로 8방향 돌아가면서
# 사람이 있는 곳에 +1
# 이때 K보다 늘어나면 멈춘다