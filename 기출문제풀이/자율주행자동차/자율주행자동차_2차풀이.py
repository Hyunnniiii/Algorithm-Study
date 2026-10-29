''' 자율주행 자동차 / 20260915 빨래를 기다리며 / 체감 난이도: 브론즈
소요 시간: 38분 / 시도: 1회 / 실행 시간: 57ms (코드트리) / 메모리: 17MB

음.. 1차 코드리뷰를 보니 과거의 나와 지금의 나는 완전히 다른 사람이다
과거의 나: cnt, fail_cnt, back_x, back_y, x, y, .... 쓸모없는 변수 너무 많음, 복잡함.
그리고 1차 풀이에선 함수화는 어림도 없고 애초에 절차대로 코드를 짤 생각이 없어보임.
문제에서 말한 대로 하려고는 하는데, 단계를 구분 안하고 한 번에 while문으로 돌리려고 하다 보니
내가 짰던 코드인데도 오늘 보니 이해하기 어렵ㄷㅏ
BUT 오늘 나의 코드? 이뻐죽겠다

문제를 처음 봤을 때는 설명에 나온 대로 일단 좌회전하고, 그 다음에 좌회전 추가로 4번 하는 코드를 구현하고 있었는데
생각해보니까 그냥 그 자리에서 좌회전 4번 해서 안되면 후진하는거나 다름이 없었다.
그래서 중간에 수정했다.

'''

# ==============
# [1] 현재 방향 기준으로 왼쪽으로 한 칸 가기
# 미방문 / 범위 내 / 도로여야 함
# [2] 1번이 불가한 경우: 인도거나, 이미 방문한 경우
# 좌회전해서 1번 다시 시도
# [3] 좌회전 4번 해서 확인했는데 모두 안되는 경우
# 바라보는 방향 유지한 채로 한 칸 후진, 1번 다시 시도
# [4] 종료: 후진 시도했으나 뒷 공간이 인도여서 못 가는 경우

# 구할 것: 종료되었을 때 자동차가 거쳐간 도로의 총 면적
# 처음 위치도 포함이다
# 근데 이거 그냥 1번 과정에서 좌회전했을 때 4방향 다 안되면 후진 하는거 아님?

# ===========
import sys
sys.stdin = open('input.txt', 'r')

# 1. 현재 방향 기준으로 왼쪽 간 적 없다면, 좌회전해서 1칸 전진하기
def go_left():
    global car_r, car_c, car_d

    for _ in range(4):
        nr, nc = car_r + dr[(car_d-1)%4], car_c + dc[(car_d-1)%4]

        # 미방문, 도로면 갈 수 있음 > 방문 처리, 차의 좌표와 방향 업데이트
        if visit[nr][nc] == 0 and arr[nr][nc] == 0:
            visit[nr][nc] = 1
            car_r, car_c, car_d = nr, nc, (car_d-1)%4
            return True

        # 못 간다면 > 다시 좌회전
        car_d = (car_d-1)%4

    # 만약 여기로 온다면 > 4번 좌회전 했는데 다 실패한거임
    return False


# 2. 좌회전해서는 못가. 후진하자
def go_back():
    global car_r, car_c, car_d

    # 현재 방향을 유지한 채로 후진한 다음, 1번 시도
    nr, nc = car_r + dr[(car_d+2)%4], car_c + dc[(car_d+2)%4]

    # 만약 후진을 못한다면 > 바로 종료
    if arr[nr][nc] == 1:
        return False

    # 후진 가능하면 > 좌표 갱신, 방문 처리, 다시 1번 시도하세요
    car_r, car_c = nr, nc
    visit[nr][nc] = 1
    return True


# ====================================
R, C = map(int, input().split())
car_r, car_c, car_d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
visit = [[0]*C for _ in range(R)]
visit[car_r][car_c] = 1

# 북동남서 (시계니까 좌회전할 때 -1로 처리)
dr = [-1,0,1,0]
dc = [0,1,0,-1]

while True:
    # [1] 왼쪽 갈 수 있는감?
    ok = go_left()

    # [2] 1이 안되면 > 후진혀
    if not ok:
        final_ok = go_back()

        # [3] 2도 안되면 > 그냥 끝
        if not final_ok:
            print(sum(map(sum, visit)))
            break