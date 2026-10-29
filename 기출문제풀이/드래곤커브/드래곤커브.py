# 고려할 것: 마지막에 좌표가 양수인 것들만 추려야 함, g=0일 때, n=1일 때

from collections import deque
## 입력 받기
N = int(input().strip())

# 4개 방향: 문제에 나온 순으로(우상좌하)
di = [0,-1,0,1]
dj = [1,0,-1,0]

# 어떤 방향이냐에 따라 그 다음에 들어갈 방향이 달라짐
# 인덱스: 원래 방향 / 값: 다음 방향의 인덱스
nxt_dir = [1, 2, 3, 0]

# 함수: 방향에 따라 그 다음 좌표를 반환한다
def coord(x, y, direction):
    if direction == 0:     # 우
        return (x, y+1)
    if direction == 1:     # 상
        return (x-1, y)
    if direction == 2:     # 좌
        return (x, y-1)
    if direction == 3:     # 하
        return (x+1, y)

## 드래곤 커브 수행
ans = set()     # 드래곤 커브로 생긴 좌표 넣을 곳
for _ in range(N):
    sx, sy, d, g = map(int, input().split())
    Q = deque([d])    # 방향 인덱스 임시 저장할 큐
    real_Q = deque([d])

    # 방향 저장
    for chasu in range(1, g+1):
        while Q:
            to_change = Q.pop()
            real_nxt = nxt_dir[to_change]
            real_Q.append(real_nxt)

        for idx in range(len(real_Q)):
            Q.append(real_Q[idx])

    # 좌표 저장
    ans.add((sx, sy))
    while real_Q:
        dd = real_Q.popleft()
        sx, sy = coord(sx, sy, dd)

        # 범위 안에 있는 것만
        if 0 <= sx <= 100 and 0 <= sy <= 100:
            ans.add((sx, sy))

## 정산
dragon = 0
for row, col in ans:
    if ((row+1, col) in ans) and ((row, col+1) in ans) and ((row+1, col) in ans) and ((row+1, col+1) in ans):
        dragon += 1

print(dragon)