# K시간 뒤 기린이 먹을 수 있는 사과의 최대 개수
# 기린은 오른쪽 첫번째 나무에 서있다!!
# 갔던 길을 다시 못 간다는 조건은 없음

def apple(idx, row, col, sm):
    global max_apple

    # 종료 조건: K시간 뒤
    if idx == K:
        max_apple = max(sm, max_apple)
        return

    # 사과 먹기, 방문 안한 곳으로
    # 상하좌우 4방향
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    for k in range(4):
        ni, nj = row + di[k], col + dj[k]

        if 0 <= ni < 2 and 0 <= nj < N:
                eat = arr[row][col]
                arr[row][col] = 0
                apple(idx+1, ni, nj, sm + eat)
                arr[row][col] = eat

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]

max_apple = 0

apple(0,1,0,0)
print(max_apple)