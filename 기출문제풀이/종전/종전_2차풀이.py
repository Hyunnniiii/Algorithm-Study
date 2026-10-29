
""" 종전 / 20260926 배불러서 졸림 / 체감 난이도: 골드
소요 시간 모름분 / 시도 1회 / 실행 시간 342ms (코드트리) / 메모리 24MB (코드트리)

아놔 진짜 이거 왤케 어렵냐 나는
머리가 나쁘면 몸이 고생한다
> 1차 코드리뷰 한거 봤는데 백트래킹 시도함 ㅋㅋㅋ 개고생했네

나아진 점: 둘 다 결국 복잡한 로직을 생각해냈지만, 코드의 구조 자체는 내가 훨 깔끔함.
    꾸역꾸역 함수화해서 최대한 덜 복잡하려고 노력했지만.. 그래도 힘들었따잇.

"""
# 구할 것: 인구 수의 최댓값과 최솟값의 차이가 가장 작을 때의 값
# ========================
import sys
sys.stdin = open('../input.txt', 'r')

# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

# 2. 해당 시작점에서 시작했을 때 가능한 이동 횟수의 조합 뽑기
def get_kan(sr, sc):
    r, c = sr, sc
    kan_lst = []    # 둘의 조합

    # 우상으로 얼마나 갈 수 있는지
    r_kan = 0

    while True:
        nr, nc = r + dr[0], c + dc[0]

        if not in_range(nr, nc):
            break

        r_kan += 1
        r, c = nr, nc

        # 좌상 길이 1, 2, 3, ...
        l_kan = 0
        nnr, nnc = nr, nc

        while True:
            nnnr, nnnc = nnr + dr[1], nnc + dc[1]

            if not in_range(nnnr, nnnc):
                break

            l_kan += 1
            nnr, nnc = nnnr, nnnc  # ★ 실제 이동

            # 현재 좌상 끝에서 좌하 r_kan칸 가능한가?
            last_r = nnr + dr[2] * r_kan
            last_c = nnc + dc[2] * r_kan

            if not in_range(last_r, last_c):
                continue

            kan_lst.append((r_kan, l_kan))

    return kan_lst


# 4. 해당 visit으로 부족 표시 시작
def color_bujok():
    y1, y3, x2, x4 = check[0][1], check[2][1], check[1][0], check[3][0]
    # 2번 부족
    for r in range(x4):
        for c in range(y3+1):
            if visit[r][c]==1:
                break
            visit[r][c] = 2

    # 3번 부족
    for c in range(y3+1, N):
        for r in range(x2+1):
            if visit[r][c] == 1:
                break
            visit[r][c] = 3

    # 4번 부족
    for r in range(x4, N):
        for c in range(y1):
            if visit[r][c] == 1:
                break
            visit[r][c] = 4

    # 5번 부족
    for c in range(y1, N):
        for r in range(N-1, x2, -1):
            if visit[r][c] == 1:
                break
            visit[r][c] = 5


def debug_print(word):
    if DEBUG:
        print(word)
        print('사각형 그리기 확인')
        for row in visit:
            print(row)
        print()

DEBUG = False
#########################
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 대각 4방향
dr = [-1,-1,1,1]
dc = [1,-1,-1,1]

# 실행
# 1. 직사각형 시작점 꼭짓점 잡기
ans = float('inf')
for sr in range(N):
    for sc in range(N):

        # 2. 해당 시작점에서 시작했을 때 가능한 이동 횟수의 조합 뽑기
        kan_lst = get_kan(sr, sc)

        # 3. 각 조합마다 지나간 경로 1 표시
        for r_kan, c_max_kan in kan_lst:
            visit = [[0] * N for _ in range(N)]
            check = [(sr, sc)]  # 사각형 꼭짓점 좌표 모을거임
            cr, cc = sr, sc
            visit[sr][sc] = 1

            # 우상으로 올라가
            for r in range(1, r_kan+1):
                nr, nc = cr + dr[0]*r, cc + dc[0]*r
                visit[nr][nc] = 1

            # 좌상으로 올라가
            check.append((nr,nc))
            cr, cc = nr, nc
            for c in range(1, c_max_kan+1):
                nr, nc = cr+dr[1]*c, cc+dc[1]*c
                visit[nr][nc] = 1

            # 좌하로 내려가
            check.append((nr,nc))
            cr, cc = nr, nc
            for r in range(1, r_kan+1):
                nr, nc = cr + dr[2]*r, cc + dc[2]*r
                visit[nr][nc] = 1

            # 우하로 내려가
            check.append((nr,nc))
            cr, cc = nr, nc
            for c in range(1, c_max_kan+1):
                nr, nc = cr+dr[3]*c, cc+dc[3]*c
                visit[nr][nc] = 1

            debug_print('사각형 그리기 완료')

            # 4. 해당 visit으로 부족 표시 시작
            color_bujok()
            debug_print('부족 표시 완료')

            # 5. 각 부족별 인구수 계산 후 min/max 차이 최소인걸로 갱신
            point = [0,0,0,0,0]   # 0번 인덱스는 사용 X
            for r in range(N):
                for c in range(N):
                    # 1번 부족
                    if visit[r][c] == 0 or visit[r][c] == 1:
                        point[0] += arr[r][c]
                    # 나머지 부족
                    else:
                        point[visit[r][c]-1] += arr[r][c]
            gap = max(point) - min(point)
            ans = min(ans, gap)
print(ans)

















