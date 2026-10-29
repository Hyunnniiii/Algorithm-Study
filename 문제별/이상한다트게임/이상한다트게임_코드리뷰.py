
''' 이상한 다트 게임 / 20260831 / 체감 난이도 : 실버 1
소요 시간: 1시간 37분 / 시도: 4회 / 실행 시간: 177ms (코드트리) / 메모리: 21MB

[타임라인]
# 13:36 - 13:47(11분) 문제 읽기 / 구상
# 13:47 - 14:26(39분) 구현 완료, 점검 후 제출 > fail
# 14:26 - 14:30(4분) 정규화할 때 숫자 개수 및 숫자 카운트 전면 수정 > fail
# 14:30 - 14:52(22분) 정규화할 때 제거하는 곳을 0으로 해뒀는데, 이것까지 계산에 포함해서 수정 > fail
# 14:52 - 15:13(21분) 애초에 시계방향 인덱싱을 잘못했음을 확인, 수정 > success

[구상]
- (bad)
    - 루틴 안지킴. 구상 단계에서 엣지 케이스나 주의할 부분 생각 미리 하고, 주석에다 써놓고 하기로
    했잖니?? 문제가 이해가 잘 돼서 신나서 바로 구현한듯;;

[구현]
- (good)
    - 기능 단위마다 결과를 확인해서 pprint로 확인했다. 디버깅 때 어디에서 틀렸는지 확인하기 쉬웠고,
    구현할 때도 편했다. 그리고 좀 빨라졌다.
- (bad)
    - 일단 첫 구현에서 틀린 부분이 너무 많다. 특히 인덱싱 실수를 하다니!!
    이거는 너무 테케랑 비교만 하고 안일하게 넘어간게 아닌가 싶은 생각이 든다..

[디버깅]
- (good)
    - 사실 마지막 수정할 때는 무조건 정규화 부분에서 틀렸을 거라 생각했는데
    그냥 코드 신생아 마인드로 보자 하고 처음부터 봤더니 인덱싱에서 틀렸다
    잘 안풀릴 때는 처음부터 내 코드를 다시 돌아보자
- (bad)
    - 정규화 틀린거 확인을 또 거대한 테케 하나하나 계산하면서 보고 있었음
    만들어서 확인해보면 편하다고.. 해보라고

[후기]
    - 실수를 안하는 사람이 되고 싶도다
    근데 실수일까? 문제 읽고 엣지나 신경쓸 부분에 대해 좀 더 생각하는 시간을 가지자

---------------------------------------------------------
[개선할 사항]
# 와 이걸 bfs로 풀 생각을 전혀 못했는데 해봐야지


'''
# =======================================================
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