
""" 술래잡기 / 20260930 에픽하이의 one을 들으며 / 체감 난이도: 골드5
소요 시간 86분 / 시도 2회 / 실행 시간 84ms (코드트리) / 메모리 18MB (코드트리)

첫 제출에서 실수한 것 목록
1. 거리 3 이상인 도망자들을 새로운 배열에 넣어주지 않고 초기화함
2. 달팽이 대각선 판정에서 N 써야 되는데 테케 N 숫자 씀
3. change 오타 << 이거 찾는데 오래걸림

1차 풀이의 나 : 레전드
달팽이를 아직 템플릿화 하지 않은 상태였어서 술래가 안으로 들어갔다 나오는걸 전부 다 빡구현했다.
템플릿의 중요성. 음음
그리고 술래와의 거리 3 이내를 bfs로 함.. 대체 왜?

예전에 되게 많이 고생했던 문제였는데 설계만 잘 하면 나쁘지 않은 문제라는 생각이 든다
구상을 오래하고 구현을 되게 빨리했는데,
이게 change를 오타 내버리니까 찾기가 참 쉽지 않았다.. 이러지마 진짜

"""
# 15:15 ~ 15:32 손구상 ~ 휴식4분 ~ 15:54 주석 구상 완
# ~ 16:14 구현 완료 후 시원하게 오답 ~ 16:45에 성공
# =========================

# 범위 체크다리
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


# 도망자들 이동한다리
def domangga(sr, sc):
    global arr

    imsi = [[[] for _ in range(N)] for _ in range(N)]
    go = set()     # 거리 3 이내 도망자 좌표

    for r in range(N):
        for c in range(N):
            if abs(r-sr) + abs(c-sc) <= 3:
                if len(arr[r][c]) > 0:
                    go.add((r,c))

    for r in range(N):
        for c in range(N):
            if (r,c) not in go and len(arr[r][c]) > 0:
                for people in arr[r][c]:
                    imsi[r][c].append(people)

            else:
                for people in arr[r][c]:
                    nr, nc = r + dr[people], c + dc[people]

                    # 범위 밖이면 > 방향 바꾸고 이동
                    if not in_range(nr, nc):
                        people = change[people]
                        nr, nc = r + dr[people], c + dc[people]

                    # 술래 없으면 이동 가능
                    if not (nr == sulle_r and nc == sulle_c):
                        imsi[nr][nc].append(people)
                    else:
                        imsi[r][c].append(people)
    arr = imsi


# 달팽이 꺾는 곳인지 확인해주는 함수
def may_i_change(row,col):
    if col-row==1 and row<N//2:
        return True
    elif row+col==N-1 and row<N//2:
        return True
    elif row+col==N-1 and row>N//2:
        return True
    elif row==col and col>N//2:
        return True
    else:
        return False


# 술래가 움직인다리
def sulle_move(sr, sc, sd, mode):
    global sulle_d
    nr, nc = sr + dr[sd], sc + dc[sd]

    if may_i_change(nr, nc):
        if mode == 0:
            sulle_d = (sd+1)%4
        elif mode == 1:
            sulle_d = (sd-1)%4

    return nr, nc


# 술래가 잡는다리
def sulle_japgi(sr, sc, sd):
    cnt = 0
    for k in range(3):
        nr, nc = sr+dr[sd]*k, sc+dc[sd]*k

        if not in_range(nr,nc):
            continue
        if len(arr[nr][nc])==0:
            continue
        if tree[nr][nc]:
            continue

        cnt += len(arr[nr][nc])
        arr[nr][nc] = []

    return cnt


def debug_print(word):
    if DEBUG:
        print(word)
        print('현재 술래 위치와 방향')
        print(sulle_r, sulle_c, sulle_d)
        print()
        print('현재 도망자 배열 상황')
        for row in arr:
            print(row)
        print()

#############
DEBUG = True
N, M, H, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]    # [도망자들 방향 목록]
tree = [[0]*N for _ in range(N)]    # 나무 있으면 1 없으면 0
for _ in range(M):
    x, y, d = map(int, input().split())
    arr[x-1][y-1].append(d)
for _ in range(H):
    x, y = map(int, input().split())
    tree[x-1][y-1] = 1
sulle_r, sulle_c, sulle_d = N//2, N//2, 0
mode = 0    # 0은 발산, 1은 수렴 (술래 달팽이 모드)

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 반대 방향 인덱스 리턴용
change = [2,3,0,1]

# 실행부
ans = 0
for time in range(1, K+1):
    # [1] 도망자 이동하기
    domangga(sulle_r, sulle_c)
    debug_print('도망자 이동 완료')

    # [2] 술래 이동하기
    sulle_r, sulle_c = sulle_move(sulle_r, sulle_c, sulle_d, mode)
    debug_print('술래 이동 완료')

    if sulle_r==0 and sulle_c==0:
        mode, sulle_d = 1, 2
    elif sulle_r==N//2 and sulle_c==N//2:
        mode, sulle_d = 0, 0

    # [3] 술래가 잡기
    cnt = sulle_japgi(sulle_r, sulle_c, sulle_d)
    ans += time * cnt
    debug_print('술래 잡기 완료')

print(ans)

