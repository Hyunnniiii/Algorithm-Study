for T in range(1, int(input())+1):
    N = int(input())    # 여행지 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_dist = 0
    min_dist = 2001

    for i in range(0, N-1):
        for j in range(i+1, N):
            dist = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])

            if dist > max_dist:
                max_dist = dist
            elif dist < min_dist:
                min_dist = dist

    print(f'#{T} {min_dist} {max_dist}')