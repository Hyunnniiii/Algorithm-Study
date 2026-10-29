# 16:17 시작
# 16:28 구상완
# 16:54 1차 구현 완, 검증: 시간복잡도가 걱정된다
# 17:01 제출했는데 성공함 뭐임?


from collections import deque

## [0] 입력 받기
# NxN 계란판, L~R 사이로 차이날 때 계란판 분리
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

## [1] BFS 함수 정의
# 계란틀 배열을 탐색하면서 합칠 영역을 찾고, 평균으로 바꿔준다
def bfs():
    global check, ans
    for row in range(N):
        for col in range(N):
            if visit[row][col] == 0:
                check += 1

                Q= deque()
                Q.append((row, col))

                eggs = set()
                eggs.add((row, col))

                egg_sum = arr[row][col]
                visit[row][col] = 1

                while Q:
                    si, sj = Q.popleft()

                    for k in range(4):
                        ni, nj = si + di[k], sj + dj[k]

                        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                            if abs(arr[ni][nj] - arr[si][sj]) >= L and abs(arr[ni][nj] - arr[si][sj]) <= R:
                                Q.append((ni, nj))
                                visit[ni][nj] = 1
                                eggs.add((ni, nj))
                                egg_sum += arr[ni][nj]
                for x, y in eggs:
                    arr[x][y] = egg_sum // len(eggs)
    ans += 1

## [2] 함수 실행
status = True      # 계란 이동 필요 여부
ans = 0     # 계란 이동 횟수

while status:
    visit = [[0] * N for _ in range(N)]
    check = 0
    bfs()

    if check == N*N:
        status = False
        break

print(ans-1)    # 안옮겨도 될 때에도 탐색하니까
