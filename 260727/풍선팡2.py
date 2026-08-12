# for T in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     f_num = []
#     flower = 0
#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             flower = arr[i][j] + arr[i-1][j] + arr[i+1][j] \
#                      + arr[i][j-1] + arr[i][j+1]
#             f_num.append(flower)
#     print(f'#{T} {max(f_num)}')

# =======
# 위의 코드는 모서리 쪽을 아예 고려하지 않음 -> 실패

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    f_num = []
    for i in range(N):
        for j in range(M):
            flower = arr[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]

                if 0 <= ni < N and 0 <= nj < M:
                    flower += arr[ni][nj]
            f_num.append(flower)

    print(f'#{T} {max(f_num)}')