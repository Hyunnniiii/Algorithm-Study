
""" 예술성 / 20260925 문제를 끝내고 보니 아시안게임 한일전 패배 / 체감 난이도: 실버
소요 시간 63분 / 시도 1회 / 실행 시간 108ms (코드트리) / 메모리 19MB (코드트리)

일단 이 문제가 아마 과정평가였나 그래서 초면임 쩝
어제 회전하는 빙하 문제로 인해. 회전을 다시 공부했는데 그거 써먹으려고 풀었다.

확실히 회초리 맞았더니 좀 푸는게 정립된듯?? 뭔가 진짜 문제풀이의 과정이 깔끔하다. 땡스투 마이 팀장
첨에 문제 봤을 때 맞닿은 변의 개수를 어떻게 구해야 할지가 제일 관건이라고 생각했는데 생각보다
아이디어가 빠르게 잘 떠올라서 좋았던 문제르. 그 외엔 그냥 무난.
앞으로 남은 날들을 이 문제처럼 풀어야지

"""

# 19:45 시작 ~ 19:59 손구상 ~ 20:08 주석 설계 완료 ~ 20:48 완료

# 구할 것: 초기/1회전/2회전/3회전 이후 예술 점수의 합
# ===========================
import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


# 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

# [1] 예술 점수 구하기
def find_group():
    idx = 1     # 그룹 넘버. 한 그룹 다 찾으면 +1
    group_info = {}     # 그룹 정보 > {idx: (칸수, 숫자값)}
    visit = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visit[row][col]:
                continue
            Q = deque()
            Q.append((row, col))
            my_num = arr[row][col]
            visit[row][col] = idx
            group_info[idx] = [1, arr[row][col]]

            while Q:
                sr, sc = Q.popleft()

                for k in range(4):
                    nr, nc = sr + dr[k], sc + dc[k]

                    if not in_range(nr,nc) or visit[nr][nc]:
                        continue
                    if arr[nr][nc] != my_num:
                        continue
                    Q.append((nr,nc))
                    visit[nr][nc] = idx
                    group_info[idx][0] += 1
            idx += 1
    return visit, group_info


# 1-2. 조화로움 계산하기
def calculate():
    art_sum = 0     # 조화로움의 합
    neighbor_info = {}  # 그룹 간 맞닿은 변의 개수 저장 {(G1, G2): 변 개수}
    for r in range(N):
        for c in range(N):
            my_num = visit[r][c]
            for k in (1,3):
                nr, nc = r+dr[k], c+dc[k]

                if not in_range(nr,nc):
                    continue

                if visit[nr][nc] == my_num:
                    continue
                other_num = visit[nr][nc]
                neighbor_info[(min(my_num, other_num), max(my_num, other_num))] \
                    = neighbor_info.get((min(my_num, other_num), max(my_num, other_num)), 0) + 1
    for group, cnts in neighbor_info.items():
        g1, g2 = group
        art_sum += ((group_info[g1][0] + group_info[g2][0])*(group_info[g1][1])*
                    (group_info[g2][1]))*(neighbor_info[(min(g1,g2), max(g1,g2))])
    return art_sum


# [2] 회전
def rotation():
    global arr
    imsi = [row[:] for row in arr]

    # 정중앙 십자가 회전
    for row in range(N):
        imsi[N//2][row] = arr[row][N//2]
    for col in range(N):
        imsi[N-1-col][N//2] = arr[N//2][col]

    # 십자가 제외 시계 90도 회전
    for sr in (0, N//2+1):
        for sc in (0, N//2+1):

            for r in range(N//2):
                for c in range(N//2):
                    imsi[sr+c][sc+N//2-1-r] = arr[sr+r][sc+c]
    arr = imsi


def debug_print(word):
    if DEBUG:
        print(word)
        for row in arr:
            print(row)
        print()

DEBUG = False
###################
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 실행부
ans = 0
for _ in range(4):
    # [1] 예술 점수 구하기
    # 1-1. BFS로 그룹 나누기
    visit, group_info = find_group()
    debug_print('그룹 나누기 완료')

    # 1-2. 조화로움 계산하기
    art_sum = calculate()
    ans += art_sum
    debug_print('조화로움 계산 완료')


    # [2] 회전
    rotation()
    debug_print('회전 완료')

print(ans)