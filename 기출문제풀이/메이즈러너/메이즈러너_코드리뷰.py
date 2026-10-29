
''' 메이즈러너 / 20260907 / 체감 난이도 : 골드 2
소요 시간: 4H+ / 시도: 4회 / 실행 시간: 65ms (코드트리) / 메모리: 17MB

[타임라인]
14:00 - 14:25(25분) 문제 읽기 / 입력 받기 / 구상
14:25 - 17:30 (190분) 구현
17:30 - 디버깅하다 끝


[구상]
- 일단 문제를 보자마자 당황했음.
가장 작은 정사각형 선택, 배열에서 일정 부분만 선택해서 회전 >> 이 두 부분이 아예 어떻게 풀어야겠다-라는
생각이 떠오르는게 없었음. 회전은 어떻게 그래도 복사해서라도 하겠는데, 정사각형 선택이 정말 당황스러웠음.
- 구상할 떄도 마찬가지로 전혀 방법이 떠오르지 않았음. 그래서 이럴 땐 그냥 하드코딩이다!!는 마음가짐으로
이번 문제는 거의 모든 과정을 세세하게 케이스 나눠서 구현하기로 했다.

[구현]
- 사실 하드코딩은 나쁘지 않았다. 오히려 다른 문제에서 구현할 때보다 앞부분은 실수가 아예 나오지 않았다.
- 문제는 역시 정사각형 선택하는 부분이었는데,
나의 생각: 출구를 기준으로 가장 가까운 참가자를 BFS로 찾고, 같은 거리가 여러명이면 행과 열이 작은
참가자 고르기 >> 잘못됨

* 나의 생각을 반박할 수 있는 엣지
. . . . . .
. . . . . .
. . E . . A
. . . . . .
. . . . B .
. . . . . .

A는 맨해튼 거리 3, 정사각형 한 변 길이 4
B는 맨해튼 거리 4, 정사각형 한 변 길이 3

- 이걸 생각해냈더라면. 구현할 때 정사각형 찾는 부분에서 제일 오래걸렸는데, 시간낭비를 덜 할 수 있지 않았을까..
그 시간에 구상을 더 해서 제대로 된 답을 냈을 수도 있는거고.
그리고 이 로직 생각해내서 구현 들어갈 때 나 스스로도 이게 정말 맞나? 라는 질문에 YES라고 할 수 없는 상태였음
나도 확신 없으니까 구현하다 계속 바꾸고.. 구현도 역대급으로 오래 걸림!!
진짜 크게 혼나야 할 짓을 했다고 본다.

- 그리고 배열 회전하는거 순간 헷갈려서 멍떄리기 10분 함.. 공부한거 확실히 복습합시다

[디버깅]
- 하드코딩을 해놔서 디버깅 너무 어려웠음 ㅜ


[후기]
- 진짜 이러지 말자. 좋은 경험 한 것 같다 이 문제로.
절대로!!!!!!!!!!!! 나조차 의심가는 로직으로 구현 시작하지 말 것. 의심가면 귀찮아도 엣지 꼭 생각해낼 것.
모르겠으면 차라리 다른 부분 구현하고 나서 다시 구상해.

---------------------------------------------------------
# [개선] 83ms > 65ms
정사각형 선택하기 > size 지정해서 배열 돌리면 됨!! 하.. 진짜 똑똑한 사람 많아서 힘듦
회전하는 부분도 굳이 배열에서 떼어와서 새로운 배열을 회전하고 다시 넣을 필요가 없음.
그냥 바로 좌표 공식 써서 해주면 됨.
출구 좌표도 마찬가지. 상대좌표로 해결하면 됨

# ======================='''

# 빈칸: 이동 가능
# 벽: 이동 불가, 회전할 때 내구도 -1
# 출구

# [1] 참가자 움직임
# 동시에!! 벽이 없는 곳으로
# 출구와 가까워지는 곳으로만 이동할 수 있다. 상하 > 좌우 우선
# 움직일 수 없으면 제자리
# 한 칸에 여러 사람 가능

# [2] 미로 회전
# 1명 이상의 참가자와 출구를 포함하는 가장 작은 정사각형
# 이때 좌상단 행 작은 것 > 열 작은 것 우선으로
# 해당 정사각형을 시계방향 90도 회전, 그 안의 벽 내구도 -1

# 구할 것: 게임이 모두 끝났을 때 모든 참가자의 이동거리 합과 출구의 좌표
# [주의]
# 마지막에 출구의 좌표 다시 +1 해줘야 함
# =======================================
# 잊어버리기 전에 쓰는 후기
# 너 정사각형 정하는 로직 정말 확신을 갖고 구현 시작한거 맞아? 아니지 
# 로직 검증 똑바로 해 새끼야..는 너무 심했고 잘 해보자 ^^..
# 오히려 하드코딩한거는 다 맞았잖아. 로직이 확실한지 정말 확신이 있을 때만 진입하자..
# 솔직히 문제는 못 풀었지만. 나 이 문제 풀면서 성장함을 느꼈어.
# 공부한거 다 써먹게 되잖아 ex 배열 회전, 거리제한 bfs 등등 이 문제 또한 흡수하자
# 정사각형 탐색하는거 진짜 생각도 못했는데.. 레전드다 해보자

# ======================================
from collections import deque

# 상하좌우(0123)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 범위
def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N


# 참가자마다 이동할 방향 정하기
def go():
    global ans, player

    imsi = [[0] * N for _ in range(N)]  # 동시에 이동하니까 이거 덮어쓸거임

    for r in range(N):
        for c in range(N):

            # 사람 있으면 계산 시작
            if player[r][c] == 0:
                continue

            player_cnt = player[r][c]  # 몇 명인지
            cur_dist = abs(r - exit_r) + abs(c - exit_c)  # 현재 출구와의 거리
            moved = False  # 움직일거야?

            for k in range(4):
                nr, nc = r + di[k], c + dj[k]

                # 범위 확인, 벽이면 못 가
                if not in_range(nr, nc) or arr[nr][nc] > 0:
                    continue

                # 이동 후의 거리가 더 작아야해
                new_dist = abs(nr - exit_r) + abs(nc - exit_c)

                if new_dist >= cur_dist:
                    continue

                # 거리가 더 작다면 > 그곳 사람 수만큼 이동, 이동했다고 표시
                ans += player_cnt
                moved = True

                # 근데 그곳이 출구라면 > 바로 탈출이니까 표시할 필요 없음
                if (nr, nc) != (exit_r, exit_c):
                    imsi[nr][nc] += player_cnt

                # 여기까지 왔다면 더 탐색할 필요 없음
                break

            # 이동 못한다면 > 그대로 정보 저장
            if not moved:
                imsi[r][c] += player_cnt

    # 덮어쓰기
    player = imsi


# 가장 작은 정사각형 찾자
# 정사각형 한 변 길이 늘려가면서 배열 탐색하면 됨..
def find_square():
    # 한 변의 길이 늘려가면서
    for size in range(2, N + 1):
        # 배열 탐색
        for sr in range(0, N - size + 1):
            for sc in range(0, N - size + 1):
                er, ec = sr + size - 1, sc + size - 1

                # 출구가 있나요
                if not (sr <= exit_r <= er and sc <= exit_c <= ec):
                    continue

                # 사람이 있나요
                find = False
                for r in range(sr, er + 1):
                    for c in range(sc, ec + 1):
                        if player[r][c] > 0:
                            find = True
                            break

                    if find:
                        break

                if find:
                    return sr, sc, size


# 정사각형 부분만 따로 회전시키기
def clock(sr, sc, size):
    global exit_r, exit_c

    # 임시 배열 (덮어쓸 예정)
    new_arr = [[0] * size for _ in range(size)]
    new_people = [[0] * size for _ in range(size)]

    # 시계 방향 회전 공식 써
    for r in range(size):
        for c in range(size):
            nr = c
            nc = size - 1 - r

            new_arr[nr][nc] = arr[sr + r][sc + c]
            new_people[nr][nc] = player[sr + r][sc + c]

    # 벽 1씩 빼주고
    for r in range(size):
        for c in range(size):
            if new_arr[r][c] > 0:
                new_arr[r][c] -= 1

            arr[sr + r][sc + c] = new_arr[r][c]
            player[sr + r][sc + c] = new_people[r][c]

    # 출구 회전
    # 출구 좌표 정사각형 내에서의 상대좌표로 바꾼 다음에 회전 공식 쓰기.. 왜 이제 생각나니
    imsi_exit_r, imsi_exit_c = exit_r - sr, exit_c - sc
    exit_r, exit_c = imsi_exit_c + sr, size - imsi_exit_r - 1 + sc

    return


##########################
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [[0] * N for _ in range(N)]
for _ in range(M):
    r, c = map(int, input().split())
    player[r - 1][c - 1] += 1
exit_r, exit_c = map(lambda x: int(x) - 1, input().split())
arr[exit_r][exit_c] = -100

ans = 0
for _ in range(K):

    # 이동하고 배열에 처리
    go()

    # 모두 탈출했는지 확인
    if sum(map(sum, player)) == 0:
        break

    # 사각형 찾기
    start_r, start_c, size = find_square()

    # 회전하기
    clock(start_r, start_c, size)

print(ans)
print(exit_r + 1, exit_c + 1)