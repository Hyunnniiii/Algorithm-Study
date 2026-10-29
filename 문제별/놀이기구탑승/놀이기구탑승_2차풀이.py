

""" 놀이기구 탑승 / 20260919 / 체감 난이도: 실버
소요 시간 30분 / 시도 1회 / 실행 시간 48ms (코드트리) / 메모리 16MB (코드트리)

리스트 대소비교로 자리 한번에 정한 것, 딕셔너리 활용한 것 등 많이 발전함
쓸데없는 변수 선언 줄었고, continue 활용해서 조건문 분기하는 것도 좋음
사실 첨에 딕 안에 set으로 할 수 있나 싶어서 리스트로 했는데 해보니까 되네..

"""

# 각 학생별로 좋아하는 학생 4명씩 있음 (자기자신x 중복x)
# [1] 우선순위가 높은 칸으로 탑승
# 인접에 좋친 많은 > 인접에 빈칸 많은 > 행 작은 > 열 작은
# 입력으로 주어진 순서대로 탑승
# 항상 빈칸으로만 이동

# [2] 점수
# 학생들이 전부 탑승한 이후 정산
# 인접한 곳에 앉아있는 좋아하는 사람의 수에 따라 점수
# 0, 1, 10, 100, 1000

# 구할 것: 최종 총 점수 구하기
# 인덱스 -1
# =====================
import sys
sys.stdin = open('input.txt', 'r')

# [0] 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

# [1] 우선순위 탐색
def find(idx):
    real_seat = [-1,-1,1,1]     # 최종 선택한 정보 (좋친 수, 빈칸 수, -행, -열)

    # 배열 싹 다 순회하면서 칸의 정보 입수
    for r in range(N):
        for c in range(N):
            # 0. 누가 있으면 못 앉음
            if arr[r][c]:
                continue

            # 0. 이곳에서의 나의 정보
            cur_info = [0,0,-r,-c]

            # 1. 인접한 빈칸과 좋친 수를 구하시오
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]

                # 범위 벗어나면 스킵
                if not in_range(nr, nc):
                    continue

                # 빈칸이면 > 빈칸 수에 추가
                if arr[nr][nc] == 0:
                    cur_info[1] += 1

                # 좋친이면 > 좋친 수에 추가
                if arr[nr][nc] in friend_info[idx]:
                    cur_info[0] += 1

            # 2. 다 구했으면 비교해서 갱신하시오
            real_seat = max(cur_info, real_seat)

    # 3. 찐 최종 내 자리 배열에 표시하기
    arr[-real_seat[2]][-real_seat[3]] = idx


#############
N = int(input().strip())
arr = [[0]*N for _ in range(N)]
friend_info = {}
for _ in range(1, N*N+1):
    me, one, two, three, four = map(int, input().split())
    friend_info[me] = {one, two, three, four}

# 4방향: 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 점수 리스트
grade = [0,1,10,100,1000]

# 실행
for idx in friend_info.keys():
    # [1] 다 앉아
    find(idx)

# [2] 정산
ans = 0
for row in range(N):
    for col in range(N):
        me = arr[row][col]
        cnt = 0
        # 내 주변 좋친 수를 구해
        for k in range(4):
            nr, nc = row+dr[k], col+dc[k]

            # 범위 밖 제외
            if not in_range(nr,nc):
                continue
            # 좋친이면 > +1
            if arr[nr][nc] in friend_info[me]:
                cnt += 1

        # 다 구했으면 점수 더하기
        ans += grade[cnt]
print(ans)




