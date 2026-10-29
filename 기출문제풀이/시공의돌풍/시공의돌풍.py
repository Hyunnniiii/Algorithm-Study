# 13:43 시작
# 14:00 구상 완
# 14:26 1단계 구현 완
# 15:26 2단계 구현 완 근데 while문 무한 반복
# 15:48 2단계 드디어 완성
# 16:06 1차 제출 > 성공

# nxm 격자칸, 시돌 항상 1번 열에 설치, 크기는 두 칸
# 범위 벗어나거나 시공돌풍이 있는 곳에는 확산 안됨


# 1. 먼지 4방향 확산
# 인접 확산 가능한지 확인 > 각 칸에 원래 칸 // 5만큼 확산 > 확산 다 끝나면 먼지 더한다

# 2. 시공돌풍 청소
# 윗칸 반시계, 아랫칸 시계 바람 > 먼지가 바람 방향대로 한 칸씩 이동
# 시돌에서는 먼지 0 바람 나오고, 시돌로 들어간 먼지는 사라진다

from collections import deque
# from pprint import pprint

## 입력 받기
N, M, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

## 필요한 자료 생성
# 우상좌하 (좌/우회전도 같이 쓰기 위해)
di = [0,-1,0,1]
dj = [1,0,-1,0]

sidol = []    # 시공의 돌풍 좌표 담을 리스트

## 시작
# [1] 먼지 확산
def hwaksan():
    arr_to_sum = [[0] * M for _ in range(N)]
    arr_to_sub = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            # 시공의 돌풍이면 > 좌표 저장
            if arr[r][c] == -1:
                if (r,c) not in sidol:
                    sidol.append((r, c))

            # 아니면 > 먼지 확산
            else:
                give = arr[r][c] // 5  # 나눠줄 먼지의 양
                for k in range(4):
                    nr, nc = r + di[k], c + dj[k]

                    # 범위 내에 있고 시공의 돌풍이 없으면
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != -1:
                        arr_to_sub[r][c] -= give
                        arr_to_sum[nr][nc] += give

    # 방에 있는 모든 먼지가 확산을 끝낸 다음 > 반영하기
    for r in range(N):
        for c in range(M):
            arr[r][c] = arr[r][c] + arr_to_sum[r][c] + arr_to_sub[r][c]

# [2] 돌풍의 시공 청소 시작
# 청소하는 함수 정의
def clean(direction):
    d = 0
    if direction == 'L':    # 위쪽
        c_row, c_col, dust = sidol[0][0], sidol[0][1], 0
        nrow, ncol = c_row + di[0], c_col + dj[0]
        status = True
        # 돌풍으로 돌아올 때까지 반복
        while status:
            # 범위 내에 있을 때까지는 같은 방향으로 진행
            while 0 <= nrow < N and 0 <= ncol < M:
                ndust = arr[nrow][ncol]
                arr[nrow][ncol] = dust
                dust = ndust

                # 다음 칸이 돌풍이면 끝
                if nrow == sidol[0][0] and ncol == sidol[0][1]:
                    status = False
                    break
                else:
                    c_row, c_col = nrow, ncol
                    nrow, ncol = c_row + di[d], c_col + dj[d]

            # 벽 만나서 while문 끝나면 방향 회전
            d = (d+1)%4
            nrow, ncol = c_row + di[d], c_col + dj[d]

    if direction == 'R':
        c_row, c_col, dust = sidol[1][0], sidol[1][1], 0
        nrow, ncol = c_row + di[0], c_col + dj[0]
        status = True
        # 돌풍으로 돌아올 때까지 반복
        while status:
            # 범위 내에 있을 때까지는 같은 방향으로 진행
            while 0 <= nrow < N and 0 <= ncol < M:
                ndust = arr[nrow][ncol]
                arr[nrow][ncol] = dust
                dust = ndust

                # 다음 칸이 돌풍이면 끝
                if nrow == sidol[1][0] and ncol == sidol[1][1]:
                    status = False
                    break
                else:
                    c_row, c_col = nrow, ncol
                    nrow, ncol = c_row + di[d], c_col + dj[d]

            # 벽 만나서 while문 끝나면 방향 회전
            d = (d-1) % 4
            nrow, ncol = c_row + di[d], c_col + dj[d]

    # 다 하고 나면 돌풍 자리 초기화
    arr[sidol[0][0]][sidol[0][1]] = -1
    arr[sidol[1][0]][sidol[1][1]] = -1

# [3] t초 후 먼지의 총합 구하기
for _ in range(t):
    hwaksan()
    clean('R')
    clean('L')

print(sum(map(sum, arr))+2)
