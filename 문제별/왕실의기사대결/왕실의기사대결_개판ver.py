# 이거 틀리면 엎음 ㅗ
# 내가 해놓고 너무 복잡해서 인덱싱 실수하고 딕셔너리 처리 복잡해서 멸망함


# 범위
def in_range(nr, nc):
    return 0<=nr<L and 0<=nc<L

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]


# 일단 내 옆이 벽인지, 경계인지 확인
def check_me(idx, d):
    r, c = gisa_info[idx][0], gisa_info[idx][1]
    sero, garo = gisa_info[idx][2], gisa_info[idx][3]

    if d == 0:  # 상
        sr, sc = r - 1, c

        # 바로 옆이 경계면 못 감
        if not in_range(sr, sc):
            return False
        # 바로 옆에 벽이 있으면 못 감
        for col in range(sc, sc + garo):
            if arr[sr][col] == 2:
                return False
        return True

    if d == 1:  # 우
        sr, sc = r, c + garo

        # 바로 옆이 경계면 못 감
        if not in_range(sr, sc):
            return False
        # 바로 옆에 벽이 있으면 못 감
        for row in range(sr, sr + sero):
            if arr[row][sc] == 2:
                return False
        return True

    if d == 2:  # 하
        sr, sc = r + sero, c

        # 바로 옆이 경계면 못 감
        if not in_range(sr, sc):
            return False
        # 바로 옆에 벽이 있으면 못 감
        for col in range(sc, sc + garo):
            if arr[sr][col] == 2:
                return False
        return True

    if d == 3:  # 좌
        sr, sc = r, c - 1

        # 바로 옆이 경계면 못 감
        if not in_range(sr, sc):
            return False
        # 바로 옆에 벽이 있으면 못 감
        for row in range(sr, sr + sero):
            if arr[row][sc] == 2:
                return False
        return True


def push(d):
    global to_find

    new_to_find = set()
    for idx in to_find:
        r, c = gisa_info[idx][0], gisa_info[idx][1]
        sero, garo = gisa_info[idx][2], gisa_info[idx][3]

        if d == 0:  # 상
            sr, sc = r - 1, c

            for col in range(sc, sc + garo):
                for row in range(sr, -1, -1):
                    # 빈칸이면 > 끝
                    if gisa_arr[row][col] == -1:
                        break
                    # 기사면 > 추가
                    if gisa_arr[row][col] >= 0:
                        new_to_find.add(gisa_arr[row][col])

        if d == 1:  # 우
            sr, sc = r, c + garo

            for row in range(sr, sr + sero):
                for col in range(sc, L):
                    # 빈칸이면 > 끝
                    if gisa_arr[row][col] == -1:
                        break
                    # 기사면 > 추가
                    if gisa_arr[row][col] >= 0:
                        new_to_find.add(gisa_arr[row][col])

        if d == 2:  # 하
            sr, sc = r + sero, c

            for col in range(sc, sc + garo):
                for row in range(sr, L):
                    # 빈칸이면 > 끝
                    if gisa_arr[row][col] == -1:
                        break
                    # 기사면 > 추가
                    if gisa_arr[row][col] >= 0:
                        new_to_find.add(gisa_arr[row][col])

        if d == 3:  # 좌
            sr, sc = r, c - 1

            for row in range(sr, sr + sero):
                for col in range(sc, -1, -1):
                    # 빈칸이면 > 끝
                    if gisa_arr[row][col] == -1:
                        break
                    # 기사면 > 추가
                    if gisa_arr[row][col] >= 0:
                        new_to_find.add(gisa_arr[row][col])
    to_find = list(new_to_find)

    return to_find


# 그 기사들 움직일 수 있는지 확인
def can_go(d):
    global real_nxt

    # 인접한 기사 없으면 > 나만 옮기면 돼
    if len(real_nxt) == 0:
        return True

    # 인접한 기사들마다 한 칸 갈 수 있나 확인하기
    # 한 명이라도 갈 수 없으면 못 간다
    for gisa in real_nxt:
        res = check_me(gisa, d)

        if not res:
            return False

    return True


# 이동
def move(idx, d):
    global real_nxt, gisa_arr

    imsi = [[-1]*L for _ in range(L)]

    # 일단 나는 이동 가능
    gisa_info[idx][0] += dr[d]
    gisa_info[idx][1] += dc[d]

    sero, garo = gisa_info[idx][2], gisa_info[idx][3]
    sr, sc = gisa_info[idx][0], gisa_info[idx][1]

    for row in range(sr, sr+sero):
        for col in range(sc, sc+garo):
            imsi[row][col] = idx

    # 가능하다면. 인접 기사 이동
    if len(real_nxt) != 0:
        for g in range(N):
            # 죽은 사람 제외
            if gisa_info[g] == []:
                continue

            # 리스트에 있는거는 바꿔주고, 아닌건 그대로
            if g in real_nxt:
                gisa_info[g][0] += dr[d]
                gisa_info[g][1] += dc[d]

            sero, garo = gisa_info[g][2], gisa_info[g][3]
            sr, sc = gisa_info[g][0], gisa_info[g][1]

            for row in range(sr, sr + sero):
                for col in range(sc, sc + garo):
                    imsi[row][col] = g

    # 불가하다면. 그냥 그대로임
    else:
        for g in range(N):
            if g != idx and gisa_info[g] != []:    # 난 제외 ㅎㅎ
                sero, garo = gisa_info[g][2], gisa_info[g][3]
                sr, sc = gisa_info[g][0], gisa_info[g][1]

                for row in range(sr, sr + sero):
                    for col in range(sc, sc + garo):
                        imsi[row][col] = g

    gisa_arr = imsi


# =======================================
L, N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(L)]
gisa_arr = [[-1]*L for _ in range(L)]
gisa_info = {}   # 기사들의 가로세로 길이, 체력 저장


for idx in range(N):
    # 위치 (r,c), 직사각형 (세로 h, 가로 w), 초기체력 k
    r, c, h, w, k = map(int, input().split())
    for row in range(r-1, r+h-1):
        for col in range(c-1, c+w-1):
            gisa_arr[row][col] = idx
            gisa_info[idx] = [r-1, c-1, h, w, k, k]

ans = 0
for _ in range(Q):
    idx, d = map(int, input().split())

    # [0] 없는 기사 > 무시
    if gisa_info[idx-1] == []:
        continue

    # [1] 일단 내 옆이 벽인지, 경계인지 확인
    me_res = check_me(idx-1, d)
    if not me_res:
        continue

    # [2] 인접한 기사 전부 확인
    to_find = [idx-1]
    real_nxt = set()
    while True:
        nxt_gisa = push(d)

        # 더 이상 인접한 사람 없으면 끝
        if nxt_gisa == []:
            break

        # 사람 있으면 > 추가하고 걔 옆을 또 탐색
        to_find = nxt_gisa
        real_nxt.update(nxt_gisa)

    # [3] 그 기사들이 갈 수 있나 확인, 이동
    res = can_go(d)

    # [4] 결과에 따라 나만 이동하거나, 다같이 이동
    if res:
        move(idx-1, d)

    # [5] 대미지 확인 (다른 애들 움직였을 때만)
    if res:
        for row in range(L):
            for col in range(L):
                # 일단 나는 제외
                if gisa_arr[row][col] == idx-1:
                    continue

                # 안움직인 기사 제외
                if gisa_arr[row][col] not in real_nxt:
                    continue

                # 체력 0 이상인 기사가 있는데, 함정도 있으면
                if gisa_arr[row][col] >= 0 and arr[row][col] == 1 and (gisa_info[gisa_arr[row][col]][4] != 0):
                    gisa_info[gisa_arr[row][col]][4] -= 1

        # [6] 체력 0 된 기사 제거
        for gisa in real_nxt:
            if gisa_info[gisa][4] == 0:
                # 배열에서 제거
                for row in range(L):
                    for col in range(L):
                        if gisa_arr[row][col] == gisa:
                            gisa_arr[row][col] = -1
                # 딕에서 제거
                gisa_info[gisa] = []


ans = 0
for idx in range(N):
    if gisa_info[idx] != []:
        ans += (gisa_info[idx][5]-gisa_info[idx][4])
print(ans)