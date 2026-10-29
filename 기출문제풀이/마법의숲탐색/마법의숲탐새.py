
''' 마법의 숲 탐색 / 20260918 / 체감 난이도 : 골드 3
소요 시간: 3h / 시도: 6회 / 실행 시간: 388ms (코드트리) / 메모리: 24MB

[타임라인]
09:00 - 09:38(38분) 문제 읽기 / 입력 받기 / 구상
09:38 - 10:35(57분) 구현, 1차 제출 > fail
10:35 - 10:54(19분) 배열에 음수 인덱싱 한 것을 발견, 패딩 사용 > fail
10:54 - 11:24(30분) 배열 초기화 시점 잘못됨 확인 및 수정 > fail
                (이때 처음으로 내가 이해한 방향 이동 순서가 맞는지 의심)
11:25 -   BFS에서 cur_idx를 잘못 사용함을 확인 및 set으로 수정 > fail

[구상]
-

[구현]
-
-
-

[디버깅]
-

[후기]


---------------------------------------------------------
[개선]


'''

# [1] 골렘 내려오기
# 지정된 열에서 내려온다 (출구 어디있는지도 주어짐)
# 정령은 어떤 방향에서든 탑승 가능 / 내릴 땐 지정된 곳만 가능
# 남 > 서 > 동 우선순위.
# 남쪽으로 가다가 막혀있으면 회전하면서 옆으로 간 다음에 내려간다.
# 서쪽: 반시계 / 동쪽: 시계 > 이거 그냥 출구만 바꿔주면 됨. 회전 아니다!!
# 골렘이 이동할 수 있는 가장 남쪽까지 계속 내려가기

# [2] 정령 이동
# 골렘 도착하면 상하좌우 인접한 칸으로 이동 가능
# 현재 위치한 골렘의 출구가 다른 골렘과 인접하면, 출구만을 통해 이동 가능
# 갈 수 있는 가장 남쪽의 칸에 간 뒤에 이동 종료, 정산

# [3] 초기화
# 골렘이 최대한 남쪽으로 갔지만, 몸의 일부가 숲을 벗어난다면
# 정산하지 말고, 숲에 있는 골렘 초기화

# 구할 것: 각 정령들이 최종으로 위치한 행의 총합

# 다른 정령이 이미 있는 칸에 새로운 정령 갈 수 있는가? > 예제를 보니 가능
# 근데 이거 남쪽이 안돼서 서쪽으로 갔다고 했을 때 다시 남쪽 확인이야 아니면 계속 서쪽으로 가? > 아닌감????
# 인덱스 주의
# =======================================
from collections import deque

# 범위
def in_range(nr, nc):
    return 0<=nr<R+3 and 0<=nc<C


# 최대한 아래로 내려오기
def down(idx):   # 정령 번호
    global arr, jung

    r, c, d = jung[idx][0], jung[idx][1], jung[idx][2]
    sr, sc, sd = r, c, d

    while True:
        rsr, rsc, rsd = sr, sc, sd
        ## 남쪽
        # 범위 확인
        if not (in_range(sr+1, sc-1) and in_range(sr+1, sc+1) and in_range(sr+2, sc)):
            pass
        # 누가 있나 확인
        elif arr[sr+1][sc] or arr[sr+1][sc-1] or arr[sr+1][sc+1] or arr[sr+2][sc]:
            pass
        # ok 너 이동
        else:
            jung[idx] = [sr+1, sc, sd]
            sr = sr+1
            continue

        ## 서쪽
        # 범위 확인
        if not (in_range(sr-1, sc-1) and in_range(sr, sc-2) and in_range(sr+1, sc-1) and
                in_range(sr+1, sc-2) and in_range(sr+2, sc-1)):
            pass
        # 누가 있나 확인
        elif arr[sr+1][sc] or arr[sr-1][sc-1] or arr[sr][sc-2] or arr[sr+1][sc-1] or \
            arr[sr+1][sc-2] or arr[sr+2][sc-1]:
            pass
        # ok 너 이동
        else:
            jung[idx] = [sr+1, sc-1, (sd-1)%4]
            sr, sc, sd = sr+1, sc-1, (sd-1)%4
            continue


        ## 동쪽
        # 범위 확인
        if not (in_range(sr-1, sc+1) and in_range(sr, sc+2) and in_range(sr+1, sc+1) and
                in_range(sr+1, sc+2) and in_range(sr+2, sc+1)):
            pass
        # 누가 있나 확인
        elif arr[sr+1][sc] or arr[sr-1][sc+1] or arr[sr][sc+2] or arr[sr+1][sc+1] or \
                arr[sr+1][sc+2] or arr[sr+2][sc+1]:
            pass
        # ok 너 이동
        else:
            jung[idx] = [sr+1, sc+1, (sd+1)%4]
            sr, sc, sd = sr+1, sc+1, (sd+1)%4
            continue


        if sr == rsr and sc == rsc and sd == rsd:
            break


    # arr에 표시, 윗 두줄 검사
    arr[sr][sc], arr[sr-1][sc], arr[sr][sc-1], arr[sr][sc+1], arr[sr+1][sc] = idx, idx, idx, idx, idx
    for row in range(0, 3):
        for col in range(C):
            if arr[row][col] > 0:
                arr = [[0]*C for _ in range(R+3)]
                jung = {}
                return


def find_max_row(idx):
    global ans

    sr, sc, sd = jung[idx]

    Q = deque([[sr, sc]])
    visit = [[0]*C for _ in range(R+3)]
    visit[sr][sc] = 1
    max_row = sr
    visit_idx = set()
    visit_idx.add(arr[sr][sc])

    while Q:
        r, c = Q.popleft()
        cur_idx = arr[r][c]  # 현재 내가 위치한 칸의 idx

        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]

            # 범위 내, 미방문, 빈칸 확인
            if not in_range(nr, nc) or visit[nr][nc] or not arr[nr][nc]:
                continue
            # 나와 같은 idx
            if arr[nr][nc] in visit_idx:
                Q.append([nr, nc])
                visit[nr][nc] = 1
                max_row = max(max_row, nr)

            # 나와 다른 idx > 내가 출구일 때만 갈 수 있음
            if arr[nr][nc] not in visit_idx:
                if (r == jung[cur_idx][0] + dr[jung[cur_idx][2]] and
                    c == jung[cur_idx][1] + dc[jung[cur_idx][2]]):
                    Q.append([nr,nc])
                    visit_idx.add(arr[nr][nc])
                    visit[nr][nc] = 1
                    max_row = max(max_row, nr)

    ans += (max_row-1)

def debug_print():
    for row in arr:


R, C, K = map(int, input().split())
arr = [[0]*C for _ in range(R+3)]     # 숲
jung = {}     # {정령 idx: [정령 중심 좌표, 출구 방향]}

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]


## 실행부
ans = 0
for idx in range(1, K+1):
    c, d = map(int, input().split())

    # 정령 정보 등록
    jung[idx] = [1, c-1, d]

    # 내려가
    down(idx)

    # 만약 배열 초기화 되었다면 > 밑의 과정은 수행하지 마
    if sum(map(sum, arr)) == 0:
        continue

    # 가장 밑으로 가
    find_max_row(idx)

print(ans)