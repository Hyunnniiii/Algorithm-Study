# 15:47 시작
# 16:00 구상 완료
# 16:09 장실
# 16:13 복귀 / 다시 구상. 어떻게 회전할지 모르겠음
# 16:18 회전 도전
# 17:40 종료

# 19:09 시작
# 19:42 일단 완성 후 제출

# import pprint
from collections import deque

# 입력 받기
N, RN = map(int, input().split())    # N 회전 가능 레벨 / RN 회전 횟수
arr = [list(map(int, input().split())) for _  in range(2**N)]
rotate_lev = list(map(int, input().split()))    # 회전 레벨

# 함수: 회전하고 그 다음 시작점 찾기
def find_big_start(si, sj, big):
    # 그 다음이 범위 안에 있으면 > 행만 옮기기
    if sj + 2**L < 2**N:
        return si, sj + 2**(L-1)

    # 그 다음이 범위 밖이면 > 열 바꿔주기
    if sj + 2**L >= 2**N:
        return si + 2**L, 0


# 함수: 회전할 하나의 그룹에서 그 다음 시작점 찾기
def find_start(small):
    if small == 0:
        return si, sj
    if small == 1:
        return si + 2**(L-1), sj
    if small == 2:
        return si, sj + 2**(L-1)
    if small == 3:
        return si - 2**(L-1), sj

# 함수: Q에 있는 배열의 숫자들 회전된 위치에 넣어주기
# 2341 순서로 넣으면 됨
def assign(Q, idx):
    for k in range(4):
        nxt = idx.pop(0)
        nx, ny = nxt[0], nxt[1]

        cnt = 0
        for r in range(nx, nx + 2**(L-1)):
            for c in range(ny, ny + 2**(L-1)):
                arr[r][c] = Q[k][cnt]
                cnt += 1

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

## 회전 레벨 리스트 주어진 만큼 반복
for L in rotate_lev:

    # [1] 회전하기
    si, sj = 0, 0
    for big in range(((2**N) // (2**L))**2):
        # **Level 0 처리
        if L == 0:
            break

        Q = deque()
        idx = []
        for small in range(4):
            lst = []    # 작은 그룹 숫자들 담을 리스트
            si, sj = find_start(small)
            idx.append((si, sj))
            for x in range(si, si + 2**(L-1)):
                for y in range(sj, sj + 2**(L-1)):
                    lst.append(arr[x][y])
            Q.append(lst)

        # 회전한 위치에 다시 배정해주기
        deque.rotate(Q, -1)
        assign(Q, idx)

        # 그 다음 작은 네모 위치
        si, sj = find_big_start(si, sj, big)

    # [2] 얼음 녹는 것 확인하기 : 얼음은 동시에 녹는다
    remove_lst = []
    for row in range(2**N):
        for col in range(2**N):
            if arr[row][col] > 0:
                bingha = 0
                for k in range(4):
                    nrow, ncol = row + di[k], col + dj[k]

                    if 0 <= nrow < 2**N and 0 <= ncol < 2**N and arr[nrow][ncol] > 0:
                        bingha += 1
                if bingha < 3:
                    remove_lst.append((row, col))

    for rlst in remove_lst:
        arr[rlst[0]][rlst[1]] -= 1

## [3] 가장 큰 군집 찾기: dfs
visit = [[0]*(2**N) for _ in range(2**N)]
def dfs(x, y):
    cnt = 1

    for k in range(4):
        nx, ny = x + di[k], y + dj[k]

        if 0 <= nx < 2**N and 0 <= ny < 2**N:
            if arr[nx][ny] > 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                cnt += dfs(nx, ny)
    return cnt

final_ans = 0
for rr in range(2**N):
    for cc in range(2**N):
        if arr[rr][cc] > 0 and visit[rr][cc] == 0:
            visit[rr][cc] = 1
            cnt = dfs(rr, cc)
            final_ans = max(final_ans, cnt)

print(sum(map(sum, arr)))
print(final_ans)