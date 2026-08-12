# N = int(input())
# bingo = [list(input().strip()) for _ in range(N)]
#
# # 8개 방향
# di = [-1,-1,-1,0,0,1,1,1]
# dj = [-1,0,1,-1,1,-1,0,1]
#
# ok = False
# # 빙고판 돌아가면서 센다
# for i in range(N):
#     for j in range(N):
#
#         # 비어있는 칸이 아니면 탐색
#         if bingo[i][j] != '.':
#             winner = bingo[i][j]
#             score = 1
#
#             # 주변에 같은 문자 있으면 진행
#             for k in range(8):
#                 ni, nj = i + di[k], j + dj[k]
#
#                 if 0 <= ni < N and 0 <= nj < N:
#                     if bingo[ni][nj] == winner:
#                         score += 1
#
#                     if score == N:
#                         ok = True
#                         break
#
# if ok:
#     print(winner)
# else:
#     print('ongoing')

# =============

# 가로, 세로, 대각선 중 연속으로 3개의 칸에 자신의 알파벳을 적어 넣은 사람이 승자
# 3번만 연속으로 있으면 빙고

N = int(input())    # 보드 크기
arr = [list(input().strip()) for _ in range(N)]

# 4개 방향: 우, 하, 우상, 우하
di = [0,1,-1,1]
dj = [1,0,1,1]

bingo = False
for i in range(N):
    for j in range(N):
        # .이 아니면 탐색
        if arr[i][j] != '.' and bingo == False:
            word = arr[i][j]

            for k in range(4):
                ni, nj = i + di[k], j + dj[k]

                # 그 다음에도 같은 알파벳이면 다음을 탐색
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == word :
                        last_i, last_j = ni + di[k], nj + dj[k]

                        if 0 <= last_i < N and 0 <= last_j < N and arr[last_i][last_j] == word:
                            print(word)
                            bingo = True
                            break
if bingo == False:
    print('ongoing')

# =============
N = int(input())    # 보드 크기
arr = [list(input().strip()) for _ in range(N)]

# 4개 방향: 우, 하, 우상, 우하
di = [0,1,-1,1]
dj = [1,0,1,1]

bingo = False
k = 3
for i in range(N):
    for j in range(N):
        # .이 아니고 빙고 아직 못 찾았으면 탐색
        if arr[i][j] != '.' and bingo == False:
            word = arr[i][j]

            for direction in range(4):
                count = 1   # 현재 찾은 칸

                # k=1(그 다음)부터 k-1까지 총 k-1개 확인 -> k개 오목 완성
                for step in range(1, k):
                    ni = i + di[direction]*step
                    nj = j + dj[direction]*step

                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == word:
                            count += 1
                        # 그 다음 칸이 같은 문자가 아니면 끝 (선택)
                        else:
                            break
                    # 그 다음 칸이 범위 벗어나면 끝 (선택)
                    else:
                        break

                # k개 만족하면 확인 끝낸다
                if count == k:
                    winner = word
                    bingo = True
                    break
if bingo:
    print(winner)
else:
    print('ongoing')