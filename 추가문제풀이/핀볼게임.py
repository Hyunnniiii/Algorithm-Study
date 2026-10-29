# 10:05 swea 터져서 보류 > 정답 푸하하
# 구할 것: 게임에서 얻을 수 있는 점수의 최댓값. 출발 위치와 방향 지정 가능
# ===========================================


def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N


# 블록 종류와 현재 방향을 입력하면 다음 방향을 반환
def change_dir(block, cur_d):
    if block == 1:
        lst = [2,0,3,1]
        return lst[cur_d]
    elif block == 2:
        lst = [3,2,0,1]
        return lst[cur_d]
    elif block == 3:
        lst = [1,3,0,2]
        return lst[cur_d]
    elif block == 4:
        lst = [2,3,1,0]
        return lst[cur_d]
    elif block == 5:
        lst = [2,3,0,1]
        return lst[cur_d]


def debug_print(msg):
    if DEBUG:
        print(msg)



#############################################
DEBUG = True


# 상좌하우
dr = [-1,0,1,0]
dc = [0,-1,0,1]


TC = int(input().strip())
for test_case in range(1, TC+1):
    # 입력 받기
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]

    change_loc = {}     # {idx : [(r, c), (nr, nc)]}
    for r in range(N):
        for c in range(N):
            if 5 < arr[r][c] < 11:
                if arr[r][c] in change_loc.keys():
                    change_loc[arr[r][c]].append((r,c))
                else:
                    change_loc[arr[r][c]] = [(r, c)]

    max_score = -float('inf')
    # 시작점, 시작 방향 지정
    for sr in range(N):
        for sc in range(N):
            for sd in range(4):
                # 블록, 웜홀, 블랙홀에서는 출발 못함
                if arr[sr][sc] != 0:
                    continue

                #print('===============================')
                # 이번 판에서의 점수
                score = 0

                # while문 돌려서 한 칸씩 전진
                cur_r, cur_c, cur_d = sr, sc, sd
                while True:
                    # print('한 칸 이동')
                    # print(cur_r, cur_c, cur_d)
                    # print()
                    nxt_r, nxt_c = cur_r + dr[cur_d], cur_c + dc[cur_d]

                    # 0. 범위 밖 > 유턴
                    if not in_range(nxt_r, nxt_c):
                        cur_d = (cur_d+2)%4
                        #print('점수 추가')
                        score += 1

                        # 유턴했는데 내 자리
                        if cur_r == sr and cur_c == sc:
                            break

                        # 유턴했는데 블록
                        if 1 <= arr[cur_r][cur_c] <= 5:
                            #print('점수 추가')
                            score += 1
                            cur_d = change_dir(arr[cur_r][cur_c], cur_d)

                        # 유턴했는데 웜홀
                        if 6 <= arr[cur_r][cur_c] <= 10:
                            for row, col in change_loc[arr[cur_r][cur_c]]:
                                if row == cur_r and col == cur_c:
                                    continue
                                cur_r, cur_c = row, col
                                break
                        continue

                    # 1. 블랙홀 > 끝
                    if arr[nxt_r][nxt_c] == -1:
                        break

                    # 2. 시작점 > 끝
                    if nxt_r == sr and nxt_c == sc:
                        break

                    # 3. 빈칸 > 그대로 전진
                    if arr[nxt_r][nxt_c] == 0:
                        cur_r, cur_c = nxt_r, nxt_c
                        continue

                    # 4. 블록 > 방향 바꿔주기
                    if 1 <= arr[nxt_r][nxt_c] <= 5:
                        #print('점수 추가')
                        score += 1
                        cur_d = change_dir(arr[nxt_r][nxt_c], cur_d)
                        cur_r, cur_c = nxt_r, nxt_c
                        continue

                    # 5. 웜홀 > 워프하기
                    if 6 <= arr[nxt_r][nxt_c] <= 10:
                        for row, col in change_loc[arr[nxt_r][nxt_c]]:
                            if row==nxt_r and col==nxt_c:
                                continue
                            cur_r, cur_c = row, col
                            break
                        continue

                max_score = max(score, max_score)
                #print(max_score)

    print(f'#{test_case}', max_score)




