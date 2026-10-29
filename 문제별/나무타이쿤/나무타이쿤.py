# 16:18 시작
# 16:31 구상완
# 16:51 1차 코딩 완
# 17:05 다듬기 완 (대각선 방향 순서 수정, q 수정)
# 17:14 성공 ㄷㄷ for문 위치 수정함. 영양제 다 처리하고 나서 다음 단계 수행해야 함


from collections import deque

# 0. 입력 받기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 8방향 (문제에서 준 대로) > 이걸로 4방향도 처리 가능
di = [0,-1,-1,-1,0,1,1,1]
dj = [1,1,0,-1,-1,-1,0,1]

# 초기 설정
q = deque()
for frst in ([n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]):
    q.append(frst)

# 시작
for _ in range(m):
    direction, length = map(int, input().split())
    direction -= 1      # 1~8번이므로 인덱스 맞춰주기

    # 1. 이동 규칙에 따라 이동시킨다
    for i in range(len(q)):
        q[i][0], q[i][1] = (q[i][0] + di[direction]*length)%n, (q[i][1] + dj[direction]*length)%n
        cur_i, cur_j = q[i][0], q[i][1]

        # 2. 해당 칸의 나무의 길이 +1
        arr[cur_i][cur_j] += 1

    # 3. 인접한 대각선 확인
    for coord in q:
        si, sj = coord[0], coord[1]
        for k in range(4):
            ni, nj = si + di[2*k+1], sj + dj[2*k+1]

            # 범위 안에 있고 나무가 있으면 +1
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] != 0:
                    arr[si][sj] += 1

    # 4. 높이 2 이상인 곳 2만큼 잘라내고 영양제 올리기
    s = len(q)
    for x in range(n):
        for y in range(n):

            # q에 없던 곳이면서 높이 2 이상이면 > 길이 자르고 push
            if [x,y] not in q and arr[x][y] >= 2:
                arr[x][y] -= 2
                q.append([x, y])


    for _ in range(s):
        q.popleft()

print(sum(map(sum, arr)))

# [개선]
# 필요없는 변수 선언은 지양할 것
# frst, cur_i, cur_j, coord
# 개쩌는 함수 선언 풀이 나도 해보기


