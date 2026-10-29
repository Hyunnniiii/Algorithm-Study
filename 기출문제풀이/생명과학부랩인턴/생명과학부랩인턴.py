# 13:36

# [1]첫번째 열부터 탐색 시작
# 해당 열의 위 > 아래로 내려가면서 가장 빨리 발견한 곰팡이를 채취
# 곰팡이가 없을 수도 있음

# [2] 곰팡이 이동
# (방향, 속력)에 따라 각자 이동.
# 벽에 도달하면 방향 반대, 속력은 유지
# 방향 바꿀 때는 시간이 걸리지 않는다 > 0행에서 위로 가면 그 다음 칸은 1행
# 이동 후 한 칸 안에 곰팡이가 2개면 큰거만 남긴다

# 구할 것: 모든 열을 순회한 뒤 총 채취한 곰팡이 합
# 주의할 점: k=0일때(곰팡이가 없을 때) / 탐색하는 열에 곰팡이가 없을 때
import pprint

## 입력 받기
n, m, z = map(int, input().split())
arr = [[(0,0,0)]*m for _ in range(n)]

for _ in range(z):
    x, y, vel, d, size = list(map(int, input().split()))

    arr[x-1][y-1] = (size, vel, d-1)

# 상하우좌
di = [-1,1,0,0]
dj = [0,0,1,-1]

# 함수: 입력된 방향의 정반대 방향을 리턴
def change(dd):
    if dd == 0:
        return 1
    if dd == 1:
        return 0
    if dd == 2:
        return 3
    if dd == 3:
        return 2


## 시작
ans = 0
for idx in range(m):
    # [1] 행 내려가면서 탐색 시작
    for row in range(n):
        visit = [[(0, 0, 0)] * m for _ in range(n)]  # 임시 보관용

        if arr[row][idx][0] > 0:
            ans += arr[row][idx][0]
            arr[row][idx] = (0, 0, 0)
            break

    # [2] 곰팡이 이동하기
    for r in range(n):
        for c in range(m):
            if arr[r][c][0] > 0:
                pang, sokdo, direction = arr[r][c]  # 원래 있던 곳의 정보

                cur_r, cur_c = r, c

                # 범위를 벗어나는 순간 방향을 반대로 바꾼다: 부호 반대로, 방향도 갱신해주기
                for _ in range(sokdo):
                    nr, nc = cur_r + di[direction], cur_c + dj[direction]

                    if (0 <= nr < n and 0 <= nc < m):
                        cur_r, cur_c = nr, nc
                    else:
                        nr, nc = cur_r - di[direction], cur_c - dj[direction]
                        cur_r, cur_c = nr, nc
                        direction = change(direction)

                # 옮겨진 곳에 곰팡이 넣기
                if visit[cur_r][cur_c][0] < arr[r][c][0]:
                    visit[cur_r][cur_c] = (pang, sokdo, direction)

    arr = [brr[:] for brr in visit]

## 정산
print(ans)
