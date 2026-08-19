# 1. 한 행에 1개씩 배치하면서 가능한 경우 모두 탐색 > 백트래킹
# 2. # 으로 표시된 곳에는 배치 불가
# 3. 이미 둔 곳과 같은 행, 열에는 배치 불가

N = int(input())    # 룩의 개수

# . 빈칸 / # 장애물
arr = [list(input()) for _ in range(N)]

visit = [0]*N   # 방문한 열 기록
ans = 0

def nrook(idx):
    global ans
    # 종료: N행에 모두 놨을 때
    if idx == N:
        ans += 1
        return

    # 룩 배치하기
    for y in range(N):
        # 샵이 아니면 배치할 수 있음
        if arr[idx][y] == '.':
            if visit[y] == 0:
                # 방문표시
                visit[y] = 1
                nrook(idx+1)
                visit[y] = 0
nrook(0)
print(ans)
