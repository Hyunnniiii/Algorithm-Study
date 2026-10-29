
""" 정육면체 한번 더 굴리기 / 20260925 / 체감 난이도: 실버
소요 시간 60분 / 시도 2회 / 실행 시간 68ms (코드트리) / 메모리 17MB (코드트리)

아니 진짜 어이없네 주사위 잊어버림;;;; 뭐야???
한참 생각해서 겨우 알아냄;;;
그거 말곤 별거 X 다만 또 풀기

"""
# 21:32 시작 ~ 21:49 손구상 완료 ~ 22:15 구현완 but 주사위 배열 잘못 씀 ~ 22:34 끝..
# 엄 첫문장 맞춤법 틀린거 거슬림
# 구할 것: M번 진행해서 얻는 점수의 총합
# ======================

import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

# 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

def change(d):
    t, b, e, w, s, n = dice # 위/아래/동/서/남/북
    if d==0:    # 위
        dice[:] = [s,n,e,w,b,t]
    elif d==1:  # 오른쪽
        dice[:] = [w,e,t,b,s,n]
    elif d==2:  # 아래
        dice[:] = [n,s,e,w,t,b]
    elif d==3:  # 왼쪽
        dice[:] = [e,w,b,t,s,n]


# [1] 정육면체 굴리기
def roll():
    global dice_r, dice_c, dice_num, cur_d
    nr, nc = dice_r + dr[cur_d], dice_c + dc[cur_d]

    if not in_range(nr, nc):
        cur_d = (cur_d+2)%4
        nr, nc = dice_r + dr[cur_d], dice_c + dc[cur_d]

    dice_r, dice_c = nr, nc
    change(cur_d)
    dice_num = dice[1]

    if dice_num>arr[dice_r][dice_c]:
        cur_d = (cur_d+1)%4
    elif dice_num<arr[dice_r][dice_c]:
        cur_d = (cur_d-1)%4


# [2] 점수 계산 BFS
def score(dice_r, dice_c):
    my_num = arr[dice_r][dice_c]

    tot_sum = my_num
    Q = deque()
    Q.append((dice_r, dice_c))
    visit = [[0]*N for _ in range(N)]
    visit[dice_r][dice_c] = 1

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr+dr[k], sc+dc[k]

            if not in_range(nr,nc) or visit[nr][nc]:
                continue
            if arr[nr][nc] == my_num:
                Q.append((nr,nc))
                visit[nr][nc] = 1
                tot_sum += my_num
    return tot_sum


def debug_print(word):
    if DEBUG:
        print(word)
        print('현재 주사위 위치: ', dice_r, dice_c)
        print('현재 방향: ', cur_d)
        print('현재 주사위 바닥면: ', dice_num)
        print('얻은 점수: ', ans)
        print()

###########################
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dice_r, dice_c = 0,0
dice_num, cur_d = 6, 1   # 현재 주사위 바닥 숫자, 주사위 방향
ans = 0
DEBUG = False

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 주사위 초기 상태: 위/아래/동/서/남/북
dice = [1, 6, 3, 4, 2, 5]

# 실행부
for _ in range(M):
    # [1] 정육면체 굴리기
    roll()
    debug_print('굴리기 완료')

    # [2] 점수 계산 BFS
    get = score(dice_r, dice_c)
    ans += get
    debug_print('정산완료')
print(ans)