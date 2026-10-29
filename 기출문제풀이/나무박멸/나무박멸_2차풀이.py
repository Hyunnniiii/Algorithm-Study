
""" 나무박멸 / 20260925 오늘도 에어컨 바람에 손이 시리다 / 체감 난이도: 실버
소요 시간 60분 / 시도 2회 / 실행 시간 334ms (코드트리) / 메모리 24MB (코드트리)

옛날이랑 거의 비슷하게 풀었는데 오늘의 내가 미세하게 멍청했던 부분
: 벽을 -1로 해놓고서 만약 벽에서 제초제를 뿌리거나 뿌리다 멈추는 경우 그 칸을 0으로 만들어버림
처음 제출했을 때 그거 때문에 틀린건 아니었는데 다시 보니 그러고 있었드라
1차 풀이 때는 벽을 -inf로 만들었고, 제초제 배열 따로 안만들고 음수 집어넣었음. ㄷㄷ

틀린 부분: 제초제 뿌릴 곳 선정할 때 만약 나무가 아무 곳에도 없으면 초기값으로 설정해둔게 반환되는데
초기값을 음수로 둬서 문제 발생함. 쩝. 킬 수 프린트했는데 음수 나와서 바로 알아냄


"""
# 10:57 ~ 11:19 구상 ~ 11:50 1제출 ~ 11:56 2제출
# 맨 처음에 나무가 아예 없는 칸에 뿌리면? > 그 칸만 뿌리면 됨
# 구할 것: M년동안 박멸한 나무의 그루 수
# =======================
import sys
sys.stdin = open('../input.txt', 'r')


# [0] 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

# [1] 나무 성장
def grow():
    global arr
    imsi =[row[:] for row in arr]
    for r in range(N):
        for c in range(N):
            if arr[r][c] > 0:
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]

                    if not in_range(nr, nc):
                        continue
                    if arr[nr][nc] > 0:
                        imsi[r][c] += 1
    arr = imsi


# [2] 나무 번식
def burnsick():
    global arr
    imsi = [row[:] for row in arr]

    for r in range(N):
        for c in range(N):
            if arr[r][c] > 0:
                b_lst = []
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]

                    if not in_range(nr,nc):
                        continue
                    if arr[nr][nc] == 0 and jaecho[nr][nc] == 0:
                        b_lst.append((nr,nc))

                if b_lst:
                    b_cnt = arr[r][c]//len(b_lst)
                    for x, y in b_lst:
                        imsi[x][y] += b_cnt
    arr = imsi


# [3] 제초제 뿌릴 곳 선정
def choose_jaecho():
    real_info = (-1,-1,-1)
    for r in range(N):
        for c in range(N):
            if arr[r][c]==0 or arr[r][c]==-1:
                continue

            cnt = arr[r][c]
            for k in range(4):
                for step in range(1,K+1):
                    nr, nc = r + ddr[k]*step, c + ddc[k]*step

                    if not in_range(nr,nc):
                        continue
                    if arr[nr][nc]==-1 or arr[nr][nc]==0:
                        break
                    cnt += arr[nr][nc]
            real_info = max(real_info, (cnt, -r, -c))
    return real_info


def debug_print(word):
    if DEBUG:
        print(word)
        print('나무 상황')
        for row in arr:
            print(row)
        print()

        print('제초제 상황')
        for row in jaecho:
            print(row)
        print()

#######################
N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
jaecho = [[0]*N for _ in range(N)]
DEBUG = False

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 대각선
ddr = [-1,-1,1,1]
ddc = [-1,1,1,-1]

# 실행부
ans = 0     # 총 박멸한 나무 그루 수
for time in range(M):
    # [1] 나무 성장
    grow()
    debug_print('나무 성장 완')

    # [2] 나무 번식
    burnsick()
    debug_print('나무 번식 완')

    # [3] 제초제 뿌릴 곳 선정
    info = choose_jaecho()

    # [4] 뿌려
    kill, sr, sc = info
    if kill == -1:
        continue
    sr, sc = -sr, -sc
    ans += kill
    jaecho[sr][sc] = -C-1

    if arr[sr][sc] != -1:
        arr[sr][sc] = 0
    for k in range(4):
        for step in range(1,K+1):
            nr, nc = sr + ddr[k]*step, sc + ddc[k]*step

            if not in_range(nr,nc):
                continue
            if arr[nr][nc]==-1 or arr[nr][nc]==0:
                jaecho[nr][nc] = -C-1
                break
            jaecho[nr][nc] = -C-1
            if arr[sr][sc] != -1:
                arr[nr][nc] = 0
    debug_print('제초제 뿌리기 완')

    # [5] 제초제 갱신
    # 제초제 배열에서 음수인 부분만 1씩 더해주기
    for r in range(N):
        for c in range(N):
            if jaecho[r][c] < 0:
                jaecho[r][c] += 1
    debug_print('제초제 갱신 완')
print(ans)