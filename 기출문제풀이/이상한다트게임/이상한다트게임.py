# 13:36 시작
# 13:47 구현 시작
# 14:26 1차 코딩 완, 2번 테케 틀림
# 14:30 일단 테케 다 맞음 > fail: 정규화할 때 삭제한 곳도 포함해버림
# 14:52 2차 제출 > fail: 삭제하는 곳을 0으로 설정해서 오류 났고, 애초에 시계방향 인덱싱 잘못함
# 15:13 3차 제출 > 성공..
# import pprint

# 원판 개수 n, 원판에 적혀있는 숫자의 개수 m
# r번째 원판에 적힌 m번째 정수 (r,m)

# 1. 회전
# 각 원판의 회전은 독립적
# 원판 종류 x: x의 배수인 원판 회전, 방향 d: 시계/반시계, 회전 칸수 k

# 2. 숫자 지우기
# 인접하면서 숫자가 같으면 지운다
# 인접: 같은 원판 안에서 왼쪽/오른쪽 or 다른 원판에서 같은 위치
# 지워지는 숫자가 아예 없는 경우: 원판 전체의 수의 평균을 구해서 정규화
# 정규화: 평균과 같은 수 그대로, 평균보다 큰 수는 -1, 작은 수는 +1
# 지운 다음에 다른 수로 대체하지는 않는다

## 입력 받기
n, m, q = map(int, input().split())
dart = [list(map(int, input().split())) for _ in range(n)]
pan = [i for i in range(1,n+1)]
num_cnt = n*m

## 시작
for _ in range(q):
    x, d, k = map(int, input().split())

    # [1] 회전할 판을 구한다
    rlst = []   # 회전할 판을 담을 리스트
    for hubo in pan:
        if hubo % x == 0:
            rlst.append(hubo)

    # [2] x의 배수인 판들을 d방향으로 k만큼 회전한다
    nlst = []   # 회전한 다음의 리스트 > 배열에 집어넣을 것
    for np in rlst:
        if d == 0:  # 시계 방향
            nlst = dart[np-1][m-k:] + dart[np-1][:m-k]

        elif d == 1:    # 반시계 방향
            nlst = dart[np-1][k:] + dart[np-1][:k]

        for idx in range(len(nlst)):
            dart[np-1][idx] = nlst[idx]
    # print('회전 이후')
    # pprint.pprint(dart)


    # [3] 인접하면서 숫자가 같은 수를 지운다
    # 이거 지울 수 있는 경우가 겹칠 수 있어서.. 모아놓고 한번에 처리해야 할듯
    to_remove = set()     # 지울 곳 좌표
    for row in range(n):
        for col in range(m):
            if dart[row][col] != -100:
                # 1. 같은 행
                ncol1, ncol2 = (col-1)%m, (col+1)%m

                if dart[row][col] == dart[row][ncol1]:
                    to_remove.add((row, col))
                    to_remove.add((row, ncol1))
                if dart[row][col] == dart[row][ncol2]:
                    to_remove.add((row, col))
                    to_remove.add((row, ncol2))

                # 2. 같은 열
                if row == 0:
                    if dart[0][col] == dart[1][col]:
                        to_remove.add((row, col))
                        to_remove.add((row+1, col))
                if row == n-1:
                    if dart[n-1][col] == dart[n-2][col]:
                        to_remove.add((n-1, col))
                        to_remove.add((n-2, col))
                if 0 < row < n-1:
                    nrow1, nrow2 = row - 1, row + 1

                    if dart[row][col] == dart[nrow1][col]:
                        to_remove.add((row, col))
                        to_remove.add((nrow1, col))
                    if dart[row][col] == dart[nrow2][col]:
                        to_remove.add((row, col))
                        to_remove.add((nrow2, col))

    for coord in to_remove:
        dart[coord[0]][coord[1]] = -100

    # print('제거 이후')
    # pprint.pprint(dart)

    num_cnt = num_cnt - len(to_remove)
    if num_cnt == 0:
        break

    # [4] 정규화: 지운 숫자가 없다면
    if len(to_remove) == 0:
        pan_sum = 0
        for r in range(n):
            for c  in range(m):
                if dart[r][c] != -100:
                    pan_sum += dart[r][c]

        pan_mean = pan_sum // num_cnt

        for rrow in range(n):
            for ccol in range(m):
                if dart[rrow][ccol] != -100:
                    if dart[rrow][ccol] > pan_mean:
                        dart[rrow][ccol] -= 1
                    if dart[rrow][ccol] < pan_mean:
                        dart[rrow][ccol] += 1
    # print('정규화 이후')
    # pprint.pprint(dart)

ans = 0
for r in range(n):
    for c in range(m):
        if dart[r][c] != -100:
            ans += dart[r][c]

print(ans)