# 구할 것: 손해를 보지 않으면서 홈방법 서비스를 가장 많은 집에 제공하는 서비스 영역일 때
# >> 그때 서비스 받은 집의 수
# ==============================
_tc = 1


######################
TC = int(input().strip())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [0] 최종 구할 것들
    max_home = -float('inf')

    # [1] 중심 좌표 늘려가면서
    for r in range(N):
        for c in range(N):

            # [2] 서비스 영역의 크기 늘려가기
            for k in range(1, N+2):

                income = 0
                home = 0
                cost = k**2 + (k-1)**2

                # [3] 그러면 중심으로부터 k만큼의 거리들만 탐색하면 됨
                for row in range(N):
                    for col in range(N):
                        if abs(row-r) + abs(col-c) > k-1:
                            continue

                        if arr[row][col] > 0:
                            income += M
                            home += 1

                if income >= cost:
                    max_home = max(max_home, home)

    if test_case == _tc:
        print(f'#{test_case}', max_home)
    else:
        print(f'{test_case}', max_home)