# R행 C열 / 최종수위 E / 명령 N회
R, C, E, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

for _ in range(N):
    row, col, dig = map(int, input().split())

    lst = []

    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if 0 <= x < R and 0 <= y < C:
                lst.append(arr[x][y])

    max_height = max(lst)
    ans = max_height - dig  # 최종 높이

    # 최종 높이보다 낮으면 그대로 두고, 높으면 최종 높이로 변경
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if 0 <= x < R and 0 <= y < C:

                if arr[x][y] > ans:
                    arr[x][y] = ans

                if arr[x][y] < 0:
                    arr[x][y] = 0

# 물 채우고 부피 구하기
tot = 0
for x in range(R):
    for y in range(C):
        water = E - arr[x][y]

        if water > 0:
            tot += water

print(tot * 72 * 72)

# ==================================
# 개선한 코드

# R행 C열 / 최종수위 E / 명령 N회
R, C, E, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

for _ in range(N):
    row, col, dig = map(int, input().split())

    lst = []

    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if 0 <= x < R and 0 <= y < C:
                lst.append(arr[x][y])

    max_height = max(lst)
    ans = max_height - dig  # 최종 높이

    # 최종 높이보다 낮으면 그대로 두고, 높으면 최종 높이로 변경
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if 0 <= x < R and 0 <= y < C:

                if arr[x][y] > ans:
                    arr[x][y] = ans

                if arr[x][y] < 0:
                    arr[x][y] = 0

# 물 채우고 부피 구하기
tot = 0
for x in range(R):
    for y in range(C):
        water = E - arr[x][y]

        if water > 0:
            tot += water

print(tot * 72 * 72)