
""" 시공의 돌풍 / 20260917 / 체감 난이도: 실버
소요 시간 34분 / 시도 1회 / 실행 시간 497ms (코드트리) / 메모리 25MB (코드트리)

조건문 처리해주는 부분, 방향 전환 처리 부분에서 훨씬 깔끔해졌다는 게 눈에 보인다.
청소하는 부분도 청소 역방향으로 탐색하면서 마지막에 따로 처리할 필요 없게 구현한 점이
훨씬 나아진 것 같다.
헷갈리지 않게 위/아래 아예 분리해서 구현한 것도 굳. 과거엔 이중 while문 돌렸던데
뭐 좋긴 하지만 앵간하면 이중 while은 안하는게.. 그리고 왜 더하는거랑 빼는 배열을 따로
했을까?? 영향을 줄거라고 생각했나보다

"""
# [1] 먼지 확산
# 인접한 곳에 시공돌풍 있거나, 격자 밖이 아니라면 확산
# 본인 칸 // 5 만큼 확산
# 원래 칸은 확산된 만큼 줄어든다
# 확산되는 먼지는 모든 먼지가 확산을 마친 뒤에 더해진다. 단계 분리!

# [2] 청소
# 윗칸 반시계, 아랫칸 시계 방향 바람
# 먼지는 바람의 방향대로 한 칸씩 이동

# 구할 것: t초 후 먼지의 총량

# 의-심
# 1. 시공돌풍은 항상 행이 연속인가? > 근데 분리되어 있어도 그냥 해도 될 것 같은데?
# 2. 애초에 먼지가 하나도 없는 경우? > 주어질 수 있다
# 3. 먼지 나눠주다가 음수가 되는 경우? > 나누기 5라서 없다
# 4. 조기 종료인 경우가 있는가? > 모든 칸이 0이 되는 경우일 것 같은데.. 처리를 해줘야 하는지 의문
# ================================

## 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<M

## 먼지 확산 bfs
def spread():
    imsi = [[0]*M for _ in range(N)]

    # 모든 칸에서 진행
    for r in range(N):
        for c in range(M):
            # 시공의 돌풍에서는 하지마
            if arr[r][c] == -1:
                continue

            # 상하좌우 4칸 확인합니다 (얘는 뭘 써도 상관 없음)
            for k in range(4):
                nr, nc = r+dr1[k], c+dc1[k]

                # 범위 내, 노시공돌풍
                if not in_range(nr, nc) or arr[nr][nc] == -1:
                    continue

                # 그게 아니라면 먼지 확산, 나는 줄어들어
                imsi[nr][nc] += arr[r][c]//5
                imsi[r][c] -= arr[r][c]//5

    # 모든 칸에 대해 했으면 이제 반영해줘
    for r in range(N):
        for c in range(M):
            arr[r][c] += imsi[r][c]


## 청소하기 (위)
def clean_up(sr1, sc1):  # 시공돌풍 윗부분 좌표, 첫 탐색 방향
    # 해당 방향으로 계속 진행하다가 경계를 벗어나면 방향 꺾기
    orig, d = 0, 0
    sr, sc = sr1, sc1
    while True:
        nr, nc = sr+dr1[d], sc+dc1[d]

        # 범위밖이라면 바꿔줘
        if not in_range(nr,nc):
            d = (d+1)%4
            nr, nc = sr+dr1[d], sc+dc1[d]

        # 다음칸이 시공돌풍이면 끝
        if (nr==sr1 and nc==sc1):
            break

        # 다음 칸에 내 숫자 넣고, 다음 칸 숫자 보관
        new = arr[nr][nc]
        arr[nr][nc] = orig
        orig = new
        sr, sc = nr, nc


## 청소하기(아래)
def clean_down(sr2, sc2):  # 시공돌풍 윗부분 좌표, 첫 탐색 방향
    # 해당 방향으로 계속 진행하다가 경계를 벗어나면 방향 꺾기
    orig, d = 0, 0
    sr, sc = sr2, sc2
    while True:
        nr, nc = sr + dr2[d], sc + dc2[d]

        # 범위밖이라면 바꿔줘
        if not in_range(nr, nc):
            d = (d + 1) % 4
            nr, nc = sr + dr2[d], sc + dc2[d]

        # 다음칸이 시공돌풍이면 끝
        if (nr == sr2 and nc == sc2):
            break

        # 다음 칸에 내 숫자 넣고, 다음 칸 숫자 보관
        new = arr[nr][nc]
        arr[nr][nc] = orig
        orig = new
        sr, sc = nr, nc


#########################
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 시공돌풍 좌표 구하기
idx = 0
for r in range(N):
    for c in range(M):
        if idx == 0 and arr[r][c] == -1:
            sr1, sc1 = r, c
            idx += 1
        elif idx == 1 and arr[r][c] == -1:
            sr2, sc2 = r, c

dr1 = [0,-1,0,1]
dc1 = [1,0,-1,0]
dr2 = [0,1,0,-1]
dc2 = [1,0,-1,0]

# 실행
for _ in range(T):
    # [1] 먼지 확산
    spread()

    # [2] 청소
    clean_up(sr1, sc1)
    clean_down(sr2, sc2)

print(sum(map(sum, arr))+2)