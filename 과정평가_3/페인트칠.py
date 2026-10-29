# 새로운 색을 칠하면 두께가 1 증가
# 같은 색은 또 칠해도 두께 변화 X > set

# 범위 체크: 페인트가 배열 넘어가진 않는지
# 좌표 계산 주의해서 하기

# 구할 것: 가장 두꺼운 곳의 두께

for TC in range(1, int(input()) + 1):
    # N행 M열, 칠하는 영역 개수 K (칠하는 횟수)
    N, M, K = map(int, input().split())
    arr = [[set() for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        row, col, height, width, color = map(int, input().split())

        for x in range(row, row + height):
            for y in range(col, col+ width):
                # 범위 체크
                if 0 <= x < N and 0 <= y < M:
                    arr[x][y].add(color)

    ans = 0
    for r in range(N):
        for c in range(M):
           ans = max(ans, len(arr[r][c]))

    print(f'#{TC} {ans}')