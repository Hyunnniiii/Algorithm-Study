# 격자판 흰 0/빨 1/파 2
# 말 번호, 이동방향 지정

# 말 번호 순서대로 움직인다
# 흰색: 이동. 말이 있으면, 그 위에 올린다. 몇 개든 올리기 가능
# 빨간색: 이동 전에 순서를 반대로 뒤집는다. 즉 원래 있던거 밑에 말 추가
# 파란색 / 범위 밖: 이동하지 않는다. 방향 반대로 전환해서 이동.
# 이때 반대 방향도 파란색이라면, 방향만 전환하고 가만히 있는다
# 말이 여러개 쌓여있었다면, 이동하는 말만 방향 반대로 바꿈.

# 쌓여있는 말 이동할 때는 본인 위에 있는 말과 함께 이동

# 말이 4개 이상 겹치면 즉시 게임 종료
# import pprint

## 입력 받기
N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]    # 색 표시
arr = [[[] for _ in range(N)] for _ in range(N)]        # 말 정보 표시 (숫자, 방향)


yoot = {}       # 키: 숫자 / 값: 위치 인덱스
for idx in range(1, K+1):
    x, y, d = map(int, input().split())
    yoot[idx] = [x-1, y-1, d-1]
    arr[x-1][y-1] = [[idx, d-1]]

# 우좌상하
di = [0,0,-1,1]
dj = [1,-1,0,0]

# 방향 바꿔주는 함수
def change(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    if direction == 3:
        return 2

# 종료 status 관리 함수
def check(nr, nc):
    if len(arr[nr][nc]) > 4:
        status = False
        return status


# ===== 별미친윷놀이다보겠네 =========================
# 함수: 흰색, 빨강일 때
def redwhite(number, to_see, nr, nc):
    move_lst = []
    meot = 0
    # 이동할 말 찾고
    for k in range(len(to_see)):
        if to_see[k][0] == number:
            for gg in range(k, len(to_see)):
                move_lst.append(to_see[gg])   # 원래 배열에서 옮길 리스트
            meot = k    # 몇번째 인덱스부터 제거할지
            break

    # 그 다음 칸에 append
    for lst in move_lst:
        arr[nr][nc].append(lst)
    for idx in range(meot, len(to_see)):
        nums, dirs = to_see[idx][0], to_see[idx][1]
        yoot[nums] = [nr, nc, dirs]

    status = check(nr, nc)

    # 몇번째부터 제거할지 반환
    return meot

# 함수: 파랑일 때
def blue(number, to_see, cur_r, cur_c, cur_d):
    move_lst = []
    meot = 0

    # 방향을 바꿔준다 > 딕셔너리랑 배열 모두에 반영
    real_d = change(cur_d)
    yoot[number][2] = real_d
    for lst in to_see:
        if lst[0] == number:
            lst[1] = real_d

    # 바뀐 방향 쪽으로 위치 바꿔주기 > 딕셔너리와 배열 모두
    nxt_r, nxt_c = cur_r + di[real_d], cur_c + dj[real_d]

    # 그 다음칸도 범위 내 / not 파란칸이어야 이동 (아니라면 그냥 방향만 바꾸고 끝)
    if (0 <= nxt_r < N and 0 <= nxt_c < N) and color[nxt_r][nxt_c] != 2:
        yoot[number][0], yoot[number][1] = nxt_r, nxt_c

        # 이동할 말 찾기
        for k in range(len(to_see)):
            if to_see[k][0] == number:
                for gg in range(k, len(to_see)):
                    move_lst.append(to_see[gg])  # 원래 배열에서 옮길 리스트
                meot = k  # 몇번째 인덱스부터 제거할지
                break
        status = check(nxt_r, nxt_c)
    # 몇번째부터 제거할지 반환
    return meot



ans = 0
status = True
while status:
    ans += 1

    # 안되면 그냥 종료
    if ans > 1000:
        status = False
        break

    # 한 턴 시행
    for number in range(1, K+1):
        cur_r, cur_c, cur_d = yoot[number][0], yoot[number][1], yoot[number][2]

        # 해당 번호의 방향으로 일단 가
        nxt_r, nxt_c = cur_r + di[cur_d], cur_c + dj[cur_d]
        to_see = arr[cur_r][cur_c]   # 해당 칸의 말 상태 리스트

        # [1] 다음칸이 범위 벗어나거나 파란색일 때
        if not (0 <= nxt_r < N and 0 <= nxt_c < N):
            remove_index = blue(number, to_see, cur_r, cur_c, cur_d)
            arr[cur_r][cur_c] = arr[cur_r][cur_c][:remove_index]

        if color[nxt_r][nxt_c] == 2:
            remove_index = blue(number, to_see, cur_r, cur_c, cur_d)
            arr[cur_r][cur_c] = arr[cur_r][cur_c][:remove_index]


        # [2] 다음 칸이 흰색일 때
        if color[nxt_r][nxt_c] == 0:
            remove_index = redwhite(number, to_see, nxt_r, nxt_c)
            arr[cur_r][cur_c] = arr[cur_r][cur_c][:remove_index]


        # [3] 다음 칸이 빨간색일 때
        if color[nxt_r][nxt_c] == 1:
            to_see.reverse()
            remove_index = redwhite(number, to_see, nxt_r, nxt_c)
            arr[cur_r][cur_c] = arr[cur_r][cur_c][:remove_index]

        # [5] 안되면 그냥 종료
        if ans > 1000:
            status = False
            break

if ans > 1000:
    print(-1)
else:
    print(ans)

