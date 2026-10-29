#
# 02:36 문제 읽기 시작
# 02:51 구상 완
# 03:15 백트래킹이 낫다는걸 깨닫고 백트래킹 일단 구현 완
# 03:24 1번 구간 구현 완
# 03:44 완성 .. 제출해보겠음 > 실패 ^^
# 03:46 디버깅 해보겠음
# 백트래킹에 문제가 있느건 알겠는데 못 찾는 중
# 장실 타임 16:04 ~16:07
# 16:11 2차도전 > 시간초과 이런 ㅅㅂ 포기



# 0. 입력받기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 1. 각 칸에서 상하좌우 연속 3번 bfs.. 가 아니라 백트래킹인가?
# 함수 정의: 각 시작점에서 상하좌우 3번 이동했을 때 숫자합 구하기

visit = [[0]*m for _ in range(n)]
max1 = 0

def tetris(move, cnt, si, sj):
    global max1

    # 종료 조건: 3번 이동했을 때
    if move == 3:
        max1 = max(max1, cnt)
        return

    # 갈 방향 선택하기
    for k in range(4):
        ni, nj = si + di[k], sj + dj[k]

        if 0 <= ni < n and 0 <= nj < m:
            if visit[ni][nj] == 0:

                # 해당 방향을 선택
                visit[ni][nj] = 1
                tetris(move+1, cnt+arr[ni][nj], ni, nj)
                visit[ni][nj] = 0

                # 선택 안하면? > 코드 필요 없음

#  함수 실행: 연속 블럭에서의 최댓값 구하기
for x in range(n):
    for y in range(m):
        visit[x][y] = 1
        tetris(0, arr[x][y], x, y)
        visit[x][y] = 0
# print(max1)

# 2. 빠큐 모양 돌리기
# 빠큐 돌리기 함수 정의
# 너무 무식한데 이게 맞나요?
def yut():
    max2 = 0
    for r in range(n):
        for c in range(m):
                if 0 <= r < n-1 and 1 <= c < m-1:
                    one = arr[r][c] + arr[r+1][c] + arr[r+1][c-1] + arr[r+1][c+1]
                    max2 = max(one, max2)
                if 0 <= r < n-2 and 1 <= c < m:
                    two = arr[r][c] + arr[r+1][c] + arr[r+1][c-1] + arr[r+2][c]
                    max2 = max(two, max2)
                if 0 <= r < n-1 and 0 <= c < m-2:
                    three = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1]
                    max2 = max(three, max2)
                if 0 <= r < n-2 and 0 <= c < m-1:
                    four = arr[r][c] + arr[r+1][c] + arr[r+2][c] + arr[r+1][c+1]
                    max2 = max(four, max2)
    return max2

max2 = yut()

# 3. 1/2번 중 최대값이 정답
print(max(max1, max2))

