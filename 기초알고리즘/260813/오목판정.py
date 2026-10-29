# for TC in range(1, int(input()) + 1):
#     N = int(input())
#     # 돌이 있는 칸에 'o'
#     arr = [list(input()) for _ in range(N)]
#
#     # 4방향 탐색: 대각선 우측 위, 우, 대각선 우측 하, 하
#     di = [-1, 0, 1, 1]
#     dj = [1, 1, 1, 0]
#
#     success = 'NO'
#     for x in range(N):
#         for y in range(N):
#             cnt = 0
#
#             # 돌이 있으면 개수 세기 시작
#             if arr[x][y] == 'o':
#                 cnt += 1
#
#                 for k in range(4):
#                     ni, nj = x + di[k], y + dj[k]
#
#                     if 0 <= ni < N and 0 <= nj < N:
#                         while cnt <= 5:
#                             # 종료: cnt = 5일때
#                             if cnt == 5:
#                                 success = 'YES'
#                                 cnt = 1
#                                 break
#
#                             # 종료: 오목 아닐 때
#                             if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] != 'o':
#                                 cnt = 1
#                                 break
#
#                             # 오목인지 확인
#                             if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
#                                 cnt += 1
#                                 ni, nj = ni + di[k], nj + dj[k]
#
#     print(f'#{TC} {success}')

# =======================
# 개선한 코드
for TC in range(1, int(input()) + 1):
    N = int(input())
    # 돌이 있는 칸에 'o'
    arr = [list(input()) for _ in range(N)]

    # 4방향 탐색: 대각선 우측 위, 우, 대각선 우측 하, 하
    di = [-1, 0, 1, 1]
    dj = [1, 1, 1, 0]

    success = 'NO'
    for x in range(N):
        for y in range(N):

            # 돌이 있으면 개수 세기 시작
            if arr[x][y] == 'o':

                for k in range(4):
                    cnt = 1
                    ni, nj = x + di[k], y + dj[k]

                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1

                        # 성공: cnt = 5일때
                        if cnt == 5:
                            success = 'YES'
                            break

                        # 아니면 계속 탐색
                        ni += di[k]
                        nj += dj[k]


    print(f'#{TC} {success}')