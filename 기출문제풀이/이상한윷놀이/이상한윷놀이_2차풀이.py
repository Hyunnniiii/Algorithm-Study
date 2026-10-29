
""" 이상한 윷놀이 / 20260926 지디의 디스러브를 들으며 / 체감 난이도: 골드
소요 시간 70분 / 시도 2회 / 실행 시간 86ms (코드트리) / 메모리 18MB (코드트리)

아 되게 잘 풀고 있었는데 최근 헷갈리던거 때문에 좀 헤맸음
최근에 문제 풀면서 리스트나 배열 순회 중 수정하면 오류나길래 아예 건드리는걸 지 양 하고 있었는데
오늘 제대로 공부함: 리스트/배열/딕셔너리 순회 중 값 변경은 가능, 삭제나 삽입은 절대 지양

1차 풀이 때 코드리뷰에서 내가 아쉽다고 했던 부분: 문제에서 알려준 순서대로 흰>빨>파 순서대로 구현하다
꼬이셨다고 함. 오늘은 파랑/범위 밖 처리하고 나서 흰/빨 한번에 처리 잘해서 과거의 나를 비웃어줌
그리고 extend 몰라서 일일히 추가하셨다고 함. 응 난 extend 바로 생각해서 썼어
배열도 얕은 복사 하셨다고 함. 이건 좀..

전체적으로 종료 처리 확실히 하기 (time 써서 처리하기 쉽게), 빨강/흰색 합쳐서 처리한 점 등에서 맘에 들지만
파랑/범위 밖 케이스에 대해 엣지를 충분히 생각하지 못했다.
경계에서 앞으로 갔는데 파랑이라 후진했는데 경계 밖인 상황이라던가
조건 분기를 정신차리고 해야하는 문제인 것 같다. 또 풀어야지

"""

# 15:40 시작 ~ 15:55 손구상 ~ 16:07 주석 설계 완료
# 16:07 좀 쉴래
# 16:13 재개 ~ 16:39 1차 제출 ~ 16:52 2차 제출

# 구할 것: 게임이 종료되는 순간의 턴의 번호 (1000보다 크면 -1)
# =====================
import sys
sys.stdin = open('../input.txt', 'r')

# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N

# 색깔 처리
def yap(nr, nc, idx, color):
    sr, sc, sd = yoot[idx]
    k = arr[sr][sc].index(idx)
    move = arr[sr][sc][k:]
    arr[sr][sc] = arr[sr][sc][:k]
    if color == 'red':
        move.reverse()
    arr[nr][nc].extend(move)
    for y in move:
        _, _, d = yoot[y]
        yoot[y] = (nr, nc, d)


def debug_print(word, time):
    if DEBUG:
        print(word, '======')
        print(time, '초')
        print('윷 위치 확인')
        for row in arr:
            print(row)
        print()
        print('윷 정보 확인')
        print(yoot)
        print()
DEBUG = False
##########################
N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]    # 색깔 표시
arr = [[[] for _ in range(N)] for _ in range(N)]    # 윷 표시
yoot = {}   # {idx: (행, 열, 방향)}

change = [None, 1,3,0,2]
for idx in range(1, K+1):
    x, y, d = map(int, input().split())
    d = change[d]
    arr[x-1][y-1].append(idx)
    yoot[idx] = (x-1, y-1, d)


# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

status = True
for time in range(1, 1002):
    # 1001 되면 바로 종료
    if time == 1001:
        print(-1)
        break

    # 1번부터 순서대로
    for idx, info in yoot.items():
        sr, sc, sd = info

        # 다음 칸을 구했을 때 색깔이 뭔지에 따라 분기
        nr, nc = sr+dr[sd], sc+dc[sd]

        # 범위 밖/파랑
        if not in_range(nr, nc) or color[nr][nc] == 2:
            sd = (sd+2)%4
            yoot[idx] = (sr, sc, sd)
            nr, nc = sr + dr[sd], sc + dc[sd]

            if not in_range(nr, nc) or color[nr][nc] == 2:
                continue

        # 흰색이면
        if color[nr][nc] == 0:
            yap(nr, nc, idx, 'white')

        # 빨간색이면
        elif color[nr][nc] == 1:
            yap(nr, nc, idx, 'red')

        # 하나의 윷에 대해 처리 완료했으면, 윷을 옮긴 칸에 윷 개수 확인
        if len(arr[nr][nc]) >= 4:
            status = False
            print(time)
            break

    debug_print('윷 이동 완료', time)
    # 종료면 종료
    if not status:
        break