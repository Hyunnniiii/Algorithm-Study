# 15:36 시작
# 15:47 구상완
# 16:13 1차 뼈대 코딩 완
# 16:28 1차 끝. 점검


# 초기 전투로봇 레벨 2 / 한 칸에는 몬스터 최대 1마리만
# 전투로봇은 자신보다 레벨 높은 몬스터 칸 못 지나감.
# 레벨이 낮아야만 없앨 수 있다. 같으면 지나갈 순 있어도 죽이지는 못함
# 거리 > 행 > 열 순으로
# 레벨과 같은 수의 몬스터 죽이면 레벨업

from collections import deque

## 입력 받기
n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

## 0. 필요한 요소들 준비
di = [-1,0,0,1]
dj = [0,-1,1,0]

## 1. 최단 거리의 몬스터 찾는 BFS 함수 정의
def bfs():
    global tot_time, cur_level, kill, Q

    si, sj = Q[0]
    visit = [[-1] * n for _ in range(n)]
    visit[si][sj] = 0

    hubo = []

    # 몬스터 1번 죽이러 가는 while문
    while Q:

        i, j = Q.popleft()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            # 범위 내, 미방문, 나보다 레벨 크지 않으면 진행 가능
            if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] == -1:
                # 나와 레벨 같으면 / 빈 공간이면 방문 처리만 하고 패스
                if arr[ni][nj] == cur_level or arr[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    Q.append([ni, nj])

                # 나보다 레벨 적은 몬스터가 있으면 일단 후보 넣기
                if arr[ni][nj] > 0 and arr[ni][nj] < cur_level:
                    visit[ni][nj] = visit[i][j] + 1
                    hubo.append((visit[ni][nj], ni, nj))    # 걸린 시간, 좌표 저장

    # 죽일 수 있는 몬스터가 아예 없으면 > 종료
    if not hubo:
        Q.clear()
        return

    # 있으면 > 행/열 순으로 정렬 후 처리하기
    hubo.sort()
    time, x, y = hubo[0]

    # 몬스터를 처죽인다
    arr[x][y] = 0
    tot_time += time
    kill += 1

    # 레벨업 여부 확인하기
    if kill == cur_level:
        kill = 0
        cur_level += 1

    # 마무리) 초기화 후 다음 몬스터 찾기 시작
    start_i, start_j = x, y
    Q.clear()
    Q.append([start_i, start_j])

## [2] 실행하기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start_i, start_j = i, j
            arr[i][j] = 0

Q = deque([[start_i, start_j]])
kill = 0
cur_level = 2
tot_time = 0

while Q:
    bfs()
print(tot_time)


