
# 13:37 시작
# 13:50 구상 완
# 14:41 화캉스
# 14:44 복귀
# 15:35 실패르
# 19:55 복귀

import pprint

# 각각의 말이 바라보는 방향 독립적으로 설정할 수 있다
# 목표: 갈 수 없는 격자의 크기 최소화
# 규칙: 본인의 말은 뛰어넘어서 지나갈 수 있음 / 상대편 말은 뛰어넘을 수 없음
# / 계산할 때 상대편 말이 있는 곳은 제외 / 상대편 말이 있는 곳까지는 가능
# 말들은 이미 배치되어 있고, 그 상태에서 못 가는 영역을 최소화하기.

from copy import deepcopy

## 입력 받기
N, M = map(int, input().split())    # NxM 체스판
arr = [list(map(int, input().split())) for _ in range(N)]

# 일단 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 필요한 자료 생성
visit = [[0]*M for _ in range(N)]   # 지나갈 수 있는 곳 표시

mal_cnt = 0     # 본인의 말 개수
lst = []        # 본인의 말이 존재하는 곳의 좌표
six_cnt = 0     # 상대방 말의 개수
for x in range(N):
    for y in range(M):
        if 0 < arr[x][y] <= 5:
            mal_cnt += 1
            lst.append((x,y))
        if arr[x][y] == 6:
            six_cnt +=1

# 체스 말 종류마다 가능한 방향 넣어두기
dir_dict = dict()
dir_dict['one'] = [(0,), (1,), (2,), (3,)]
dir_dict['two'] = [(0, 1), (2, 3)]
dir_dict['three'] = [(0, 3), (3, 1), (1, 2), (2, 0)]
dir_dict['four'] = [(2,0,3), (0,3,1), (3,1,2), (0,2,1)]
dir_dict['five'] = [(0,1,2,3)]

# 함수: 숫자와 딕셔너리 키값 매칭
def match(sutza):
    if sutza == 1:
        return 'one'
    if sutza == 2:
        return 'two'
    if sutza == 3:
        return 'three'
    if sutza == 4:
        return 'four'
    if sutza == 5:
        return 'five'

# 함수: 체스 종류, 방향을 선택했을 때 갈 수 있는 곳을 visit에 표시하고,
# 처리된 visit과 추가된 칸 수(cnt)를 반환
def assign(si, sj, idx, meot):      # (시작좌표, 체스 번호, 방향)
    cnt = 1
    if visit[si][sj] == 1:
        cnt = 0

    visit[si][sj] = 1
    r_si, r_sj = si, sj

    # 갈 수 있는 방향들 순차적으로 탐색하면서
    for k in dir_dict[idx][meot]:
        while True:
            ni, nj = si + di[k], sj + dj[k]
            # 갈 수 있는 곳이면
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                if visit[ni][nj] == 0:
                    visit[ni][nj] = 1
                    cnt += 1
                si, sj = ni, nj

            # 경계 넘어가면 종료
            if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] == 6:
                si, sj = r_si, r_sj
                break
    return cnt

## 시작: 백트래킹
max_color = -float('inf')
def btrk(idx, color):
    global max_color, visit
    # 종료: 내가 가진 모든 말에 대해 선택 완료
    if idx == mal_cnt:
        max_color = max(max_color, color)
        return
    # 선택: 리스트에 있는 좌표를 하나씩 꺼내서, 해당 말의 방향을 하나씩 선택
    chess_num = arr[lst[idx][0]][lst[idx][1]]
    # 번호에 따라 키값 반환
    chess_num = match(chess_num)

    # 해당 체스가 할 수 있는 모든 방향에 대해 카운트 세기
    for k in range(len(dir_dict[chess_num])):
        rem_visit = deepcopy(visit)
        plus = assign(lst[idx][0], lst[idx][1], chess_num, k)
        btrk(idx+1, color + plus)
        visit = rem_visit
btrk(0, 0)

print(N*M - max_color - six_cnt)
