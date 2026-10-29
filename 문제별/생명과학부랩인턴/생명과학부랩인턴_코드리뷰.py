
''' 생명과학부 랩 인턴 / 20260901 / 체감 난이도 : 실버 1
소요 시간: 1시간 / 시도: 1회 / 실행 시간: 820ms (코드트리) / 메모리: 35MB

[타임라인]
# 13:36 - 13:48(12분) 문제 읽기 / 입력 받기 / 구상
# 13:48 - 14:30 (42분) 구현, 디버깅
# 14:30 - 14:34 (4분) 엣지 확인, 제출

[구상]
    - 익숙한 문제지만 열심히 읽었다. 너무 익숙하고 문제에서 친절하게 ~~에 유의하라고 써져있어서
     오히려 의심스러움; 엣지도 뭐가 있을지 생각하고 구현 시작함.
    - 어떤 자료형을 사용하면 효율적일지에 대한 생각은 많이 안한 것 같다. 해라

[구현]
- (good)
    - 다른 부분은 괜찮았는데 곰팡이 이동하는 부분에서 조금 버벅였다.
    배열 안에 튜플 하나 넣는 방식으로 입력을 받아서 만약에 이동한 칸에 곰팡이가 이미 있었다거나,
    이동 후 만나는 경우에 배열에서 바로 처리가 불가해서 이 부분에서 고민을 좀 했다.
    - 배열 안에 여러 요소 들어가게 하는 방법도 다시 알아놔야겠다.
    (왜냐면 효율을 위해 한 칸에 하나만 넣은게 아니라 여러개 넣는 방법을 까먹어서 그렇게 한거임;)

- (bad)
    - 제출하기 전 visit 배열 위치 확인 안함. 마지막에 갑자기 생각나서 적었던거라..
    곰팡이 이동할 때 생성하면 되는데 채취 단계에서 생성하는 바람에 반복문 안에 배열 생성이
    들어가버렸고 시간이 엄청 길게 나왔다.

---------------------------------------------------------
[개선할 사항]
- 딕셔너리를 활용한 풀이

'''
# =======================================================
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
        if arr[row][idx][0] > 0:
            ans += arr[row][idx][0]
            arr[row][idx] = (0, 0, 0)
            break

    # [2] 곰팡이 이동하기
    visit = [[(0, 0, 0)] * m for _ in range(n)]  # 임시 보관용
    for r in range(n):
        for c in range(m):
            if arr[r][c][0] > 0:
                pang, sokdo, direction = arr[r][c]  # 원래 있던 곳의 정보

                cur_r, cur_c = r, c

                # 속도의 범위가 1000까지 되므로 정규화해주기
                new_sokdo = 0
                if direction == 0 or direction == 1:
                    new_sokdo = sokdo % (2*(n-1))
                if direction == 2 or direction == 3:
                    new_sokdo = sokdo % (2*(m-1))

                # 범위를 벗어나는 순간 방향을 반대로 바꾼다: 부호 반대로, 방향도 갱신해주기
                for _ in range(new_sokdo):
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

    arr = visit

## 정산
print(ans)
