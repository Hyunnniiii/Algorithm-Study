
''' 토스트 계란틀 / 20260820 / 체감 난이도 : 실버 4
소요 시간: 44분 / 시도: 1회 / 실행 시간: 207ms (코드트리) / 메모리: 24MB

[타임라인]
# 16:17 - 16:28(11분) 문제 읽기 / 구상
# 16:28 - 16:54(26분) 구현
# 16:54 - 17:01(7분) 디버깅, 다듬기 > 성공

[구상]
- (good)
    - 보자마자 bfs라는 생각이 바로 들었고 어떻게 풀지도 빠르게 파악이 가능했던 것 같다
- (bad)
    - 그래서 그런지 무빙워크 풀 때처럼 100% 진심으로 세세한 구상을 하지 않은 것
    앞으로는 쉽던 말던 무조건 구상 자세하게 하기

[구현]
- (good)
    - bfs를 열심히 풀어왔어서 그런지 막힘없이 잘 진행했다
- (bad)
    - 구현하면서 구상 때 생각하지 않았던 필요한 변수들이 생기면 효율 고려하지 않고 일단 만든다.
    구상을 더 자세히 하거나, 구현할 때도 좀 효율적으로 굳이 이 변수를 새로 생성해야 하는지 생각해야 함

[후기]
    - 전형적인 bfs 문제였던 것 같다.
    - 어제 백트래킹 시간초과의 트라우마가 떠올라서 bfs 수행할 때마다 visit 생성하는거 맞는지
    제출 전에 다소 고민함. 그래서 고민을 안하고 싶으니까 시간복잡도를 아예 다시 공부하는 걸로

---------------------------------------------------------
'''

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
