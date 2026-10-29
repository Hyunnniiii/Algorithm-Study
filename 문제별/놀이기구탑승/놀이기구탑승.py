# 16:10 시작
# 16:24 구상 완료
# 17:20 1차 코딩 완 > 제출 성공

# 1) 인접한 4개 방향 중 좋아하는 친구 가장 많은 위치로 간다
# 2) 그 칸이 여러 곳이면, 그 중에서 인접한 칸이 비어있는게 많은 곳으로 간다
# 3) 그것조차 여러 곳이면, 행 번호 작은 곳
# 4) 그것조차 여러 곳이면, 열 번호 작은 곳
# 전부 다 배정한 뒤에 점수 매겨야 함

N = int(input().strip())
arr = [[0]*N for _ in range(N)]
information = [list(map(int, input().split())) for _ in range(N*N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

for idx in range(N*N):
    student, bf = information[idx][0], set(information[idx][1:])

    # [1] 인접 4방향 중 좋아하는 친구의 수 많은 곳으로
    hubo1 = []  # 1번에서 좋은 위치들 모아둘 리스트
    max_grade = 0  # 주변에 좋친 몇명인지
    for x in range(N):
        for y in range(N):
            # 해당 자리에 사람이 없을 때 탐색
            if arr[x][y] == 0:
                find_grade = 0
                for k in range(4):
                    nx, ny = x + di[k], y + dj[k]

                    # 범위 안에 있고 좋친이 있으면
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] in bf:
                            find_grade += 1
                if find_grade == max_grade:
                    hubo1.append((x, y))
                elif find_grade > max_grade:
                    hubo1 = [(x, y)]
                    max_grade = find_grade
    # 여기서 결정되면 바로 배정
    if len(hubo1) == 1:
        x, y = hubo1[0][0], hubo1[0][1]
        arr[x][y] = student

    # [2] 후보에 있는 좌표들 중 비어있는 인접칸이 많은 곳 찾기
    hubo2 = []
    max_blank = 0
    if len(hubo1) > 1:
        for row, col in hubo1:
            find_blank = 0
            for k in range(4):
                nrow, ncol = row + di[k], col + dj[k]

                # 범위 안에 있고 비어있으면
                if 0 <= nrow < N and 0 <= ncol < N and arr[nrow][ncol] == 0:
                    find_blank += 1

            if find_blank == max_blank:
                hubo2.append((row, col))
            elif find_blank > max_blank:
                hubo2 = [(row, col)]
                max_blank = find_blank
    # 여기서 결정되면 바로 배정
    if len(hubo2) == 1:
        x, y = hubo2[0][0], hubo2[0][1]
        arr[x][y] = student

    # [3] 결국 여기까지 왔다면 행열 순서로 배정
    if len(hubo2) > 1:
        x, y = hubo2[0][0], hubo2[0][1]
        arr[x][y] = student

# 집계하기
ans = 0     # 총점
cnt = 0     # 칸 당 점수
for x in range(N):
    for y in range(N):
        # 해당 칸에 들어간 학생에 해당하는 정보 찾기
        for row in information:
            if row[0] == arr[x][y]:
                bestfriend = set(row[1:])
        cnt = 0
        for k in range(4):
            ni, nj = x + di[k], y + dj[k]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in bestfriend:
                cnt += 1

        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)
