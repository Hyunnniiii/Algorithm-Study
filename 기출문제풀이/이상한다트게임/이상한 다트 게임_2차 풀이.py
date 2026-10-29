
""" 이상한 다트 게임 / 20260925 심장 아프다 / 체감 난이도: 실버
소요 시간 INF분 / 시도 1회 / 실행 시간 166ms (코드트리) / 메모리 22MB (코드트리)

ㅇ ㅏ.......... ....  .... . ....... . . ....
이거 푸는 동안 대 정 회수 프로님께서 옆에서 루틴 지키는지 감시(?) 해주셨는데
너무 신경쓰여서 혼자 멸망했다. 진심 나 멘탈 왤케 약함??

일단 문제를 잘못(?) 읽음. 행은 아니고 열만 지구별인데 지구별 자체를 안하고 시작함
그리고 자잘한 실수도 많이 함. row%x인데 x%row라고 하고 정규화도 반대로 함
기억나는 피드백: 구상을 더 구체적으로 하자. 인덱싱 헷갈리는건 손으로 하고 들어가기. 문제 똑바로 읽기.
        구상 종이에 조금 더 상세하게 주의할 점 다 적기. (ex: 지구별이다)

침착하자 진짜 ... 루틴 제 0원칙 흥분 금지 실패로 인한 대참사 기록 완.

"""

# 3:10 ~ 3:26 손구상 ~
# 구할 것: q개 회전 처리 후 게임판에 남은 수의 총합
# ====================
import sys
sys.stdin = open('../input.txt', 'r')


# 범위
def in_range(nr, nc):
    return 0 <= nr < N + 1 and 0 <= nc < M


# [1] 회전
def rotation(x, d, k):
    for row in range(x, N+1, x):
        # 시계 방향
        if d == 0:
            if row%x == 0:
                arr[row] = arr[row][-k:] + arr[row][:-k]
        # 반시계 방향
        elif d == 1:
            if row%x == 0:
                arr[row] = arr[row][k:] + arr[row][:k]


# [2] 지우기
def erase():
    to_remove = set()   # 지울 곳 좌표 모을 곳
    flag = False  # 지웠는지 체크
    for r in range(N + 1):
        for c in range(M):
            if arr[r][c] == 0:
                continue

            my_num = arr[r][c]
            for k in range(4):
                nr, nc = r + dr[k], (c + dc[k])%M

                if not in_range(nr, nc):
                    continue

                if arr[nr][nc] == my_num:
                    to_remove.add((nr,nc))
                    to_remove.add((r,c))
                    flag = True

    for x, y in to_remove:
        arr[x][y] = 0
    return flag


# [3] 정규화
def normalize():
    cnt, arr_sum = 0, 0
    for r in range(N + 1):
        for c in range(M):
            if arr[r][c] != 0:
                cnt += 1
                arr_sum += arr[r][c]

    arr_mean = arr_sum // cnt
    for r in range(N + 1):
        for c in range(M):
            if arr[r][c] == 0:
                continue
            elif arr[r][c] < arr_mean:
                arr[r][c] += 1
            elif arr[r][c] > arr_mean:
                arr[r][c] -= 1


def debug_print(word):
    if DEBUG:
        print(word)
        for row in arr:
            print(row)
        print()


##############################
DEBUG = False

N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0] * M)

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 실행
for _ in range(Q):
    x, d, k = map(int, input().split())

    # [1] 회전
    rotation(x, d, k)
    debug_print('===회전===')

    # [2] 지우기
    flag = erase()
    debug_print('지우기')

    # [3] 정규화
    if not flag:
        normalize()
        debug_print('정규화 완료')

print(sum(map(sum, arr)))