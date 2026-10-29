
''' 아기 바다거북의 대모험: 해저 화산 지대 / 20261001 / 체감 난이도 : 골드 5
소요 시간: 2h / 시도: 2회 / 실행 시간: 84ms (코드트리) / 메모리: 18MB

[타임라인]
09:00 - 09:53 (53분) 문제 읽기, 손구상, 주석구상
09:53 - 10:43 (50분) 구현 완, 제출 > fail
10:43 - 11:00 (17분) 드디어 테케 이해, 일부 수정, 제출 > 성공

[구상]
-일단 단어가 너무.. 혼란스러웠다.
마그마 압력 vs 열기 vs 분출 임계치 그냥 다 똑같아 보이고.. 진짜 이유는 잘 모르겠는데 구분이 잘 안됐다
>> 그 결과. 문제를 잘못 읽었고 애초에 테케를 이해하지 못했다.

열기 전파 단계에서 화산이 위치한 칸에 '해당 화산의 분출 임계치'만큼의 열기 발생하는건데,
나는 그냥 마그마 압력 + 추가로 들어온 열기 라고 해석을 해버렸고
구상하는 내내 그게 안보여서 대체 좌하단 칸의 열기가 60인 이유를 모른 채로 시간을 꽤 오래 소요했다.
근데 구상 시간이 너무 길어져서 일단 주석 설계로 진행했다.

- 주석 구상을 점점 더 상세하게 할 수 있게 됐다.
이유는 이제 머릿속으로 어느 정도 상상(?)할 수 있게 됐다. 예전에는 먼 그림이 안그려졌는데, 요즘은 주석으로 흐름을
쓰다보면 완성이 어떻게 된다..?
그리고 주석 구상에서 정말 도움을 많이 받는게, 구현하다보면 내가 빼먹는게 무조건 있는데 (오늘도 많았음)
내가 주석에 써둔거 보면서 아맞다!! 하면서 추가할 수 있다 (오늘 4번 정도 그랬음)

- 관리해야할 정보가 많았다고 생각이 든다.
근데 마침 내가 어제 밤에 색깔 폭탄을 풀었다 (이 문제도 관리할 정보가 많았음)
N차 풀이를 열심히 합시다


[구현]
- 어제 들은 얘기들 바로 써먹음. 딕셔너리 value 순회하지 말고 set으로 바꿔서 값 찾기,
함수에서 바뀌는 값은 리턴으로 받아서 함수 밖에서 따로 처리하기. ㅎㅎ 나 진짜 팀장 잘 만남
강사님 감사합니다

- 열기 전파 부분 이해 못해서 구현하면서도 테케 계속 들여다봤는데도 결국 이해 못했다.
그래서 일단 그냥 구현했다.. 근데 찜찜해서 구현 중간에 계속 테케 들여다보느라 늦었다.


[디버깅]
- 일단 틀리자마자 무조건 내가 문제 잘못 이해한거 맞다고 생각했다. 왜냐면 그림이 틀렸을리 없으니까 내가 틀린거임
그래서 문제를 다시 읽었는데.. 처음에는 심지어 맞는 부분 틀린줄 알고 고쳤다.
그랬더니 1번 테케가 틀리길래 진심 뭐지?? 하고 다시 1번 테케 돌리다가.. 원래 내가 맞았다는걸 알았고

그러면 진짜 뭐가 틀린거지?? 하다가.. 그냥 문제 다시 읽었다
그랬더니 그제야 보였다 >> 분출 임계치 이상인 화산은 ''뜨거운 열기''를 분출합니다..
본인도 뿜는거였음. 난 그 자리는 안하는줄. 마그마 압력이랑 열기랑 다른거였는데 구분을 안함


[후기]
문제를 제대로 잘 읽자
증신을 차리라
나 수능 지구과학 봤는데 왜이러지

---------------------------------------------------------
[개선]
화산 터지는거랑 연쇄반응 하나로 합치면 좋을듯
변수명이 좀 맘에 안듦. 좀 더 직관적인거 없나

'''

# 구할 것: 각 바다거북이 안식처에 도착한 턴 번호

# 저거 칸 왜 60이지? 진짜 왜 60이지? > 문제 처 읽어라
# 100턴 내 > 100턴까지만 인정해주는건ㄱ ㅏ..?
# ======================
from collections import deque

# 범위
def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


# 거북이 이동 bfs
def turtle_move(idx):
    r, c  = turtle[idx]

    Q = deque()
    Q.append((r,c))
    visit = [[-2]*N for _ in range(N)]
    visit[r][c] = -1
    turtle_pos = {tuple(pos) for pos in turtle.values()}

    while Q:
        sr, sc = Q.popleft()

        for k in range(4):
            nr, nc = sr+dr[k], sc+dc[k]

            if not in_range(nr,nc) or visit[nr][nc] != -2:
                continue
            if arr[nr][nc] == 1 or arr[nr][nc] == -1:
                continue
            if (nr,nc) in turtle_pos:
                continue

            # 도착했다면
            if nr==N-1 and nc==N-1:
                if visit[sr][sc] == -1:
                    return k
                else:
                    return visit[sr][sc]

            # 첫 방향이라면
            if visit[sr][sc] == -1:
                Q.append((nr,nc))
                visit[nr][nc] = k

            # 첫 방향 아니면
            else:
                Q.append((nr,nc))
                visit[nr][nc] = visit[sr][sc]
    # 경로가 없다면
    return None


# 화산 분출
def explode():
    explode_lst = set()
    for r, c, threshold in fire_info:
        if fire_stat[r][c] < threshold:
            continue

        imsi[r][c] += threshold
        explode_lst.add((r,c))
        for k in range(4):
            sr, sc = r, c
            fire = threshold
            while True:
                fire = fire//2
                # 0 되면 종료
                if fire == 0:
                    break

                # 다음 칸 확인
                nr, nc = sr + dr[k], sc + dc[k]

                # 범위 밖, 산호초
                if not in_range(nr,nc) or arr[nr][nc] == 1 :
                    break

                # 열기 더해주기
                imsi[nr][nc] += fire
                sr, sc = nr, nc

    return explode_lst


# 연쇄반응
def plus_explode():
    while True:
        plus_lst = set()
        for r, c, threshold in fire_info:
            if (r,c) in explode_lst:
                continue
            if fire_stat[r][c] + imsi[r][c] < threshold:
                continue

            imsi[r][c] += threshold
            plus_lst.add((r,c))
            explode_lst.add((r, c))
            for k in range(4):
                sr, sc = r, c
                fire = threshold
                while True:
                    fire = fire // 2
                    # 0 되면 종료
                    if fire == 0:
                        break

                    # 다음 칸 확인
                    nr, nc = sr + dr[k], sc + dc[k]

                    # 범위 밖, 산호초
                    if not in_range(nr, nc) or arr[nr][nc] == 1:
                        break

                    # 열기 더해주기
                    imsi[nr][nc] += fire
                    sr, sc = nr, nc

        if len(plus_lst)==0:
            break


def debug_print(word):
    if DEBUG:
        print(f'==={word}===')
        print()
        print('거북이 현재 상황')
        print(turtle)
        print()
        print('현재 화산 상항')
        print(fire_info)
        print()
        print('현재 마그마 상황')
        for row in fire_stat:
            print(row)
        print()

def debug_print_imsi():
    if DEBUG:
        print('외부 열기 상황')
        for row in imsi:
            print(row)
        print()

###################
DEBUG = False
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turtle = {}
for idx in range(1, M+1):
    r, c = map(int, input().split())
    turtle[idx] = [r,c]
fire_info = []  # [행,열,임계치]
fire_stat = [[0]*N for _ in range(N)]  # 현재 압력 표시
for _ in range(K):
    r, c, p = map(int, input().split())
    fire_info.append([r,c,p])

# debug_print('입력확인')

# 우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 정답 저장
ans = [-1]*(M+1)    # idx에 집어넣기

## 실행부
for time in range(1, 102):
    # 100턴 넘으면 X
    if time == 101:
        break

    # [1] 바다거북 이동
    for idx in range(1, M+1):
        if idx in turtle.keys():
            nxt_dir = turtle_move(idx)

            if nxt_dir is None:
                continue
            nxt_r, nxt_c = turtle[idx][0]+dr[nxt_dir], turtle[idx][1]+dc[nxt_dir]

            if nxt_r==N-1 and nxt_c==N-1:
                ans[idx] = time
                turtle.pop(idx)
            else:
                turtle[idx] = [nxt_r, nxt_c]

    debug_print('거북이 이동 완료')

    # [2] 화산 압력 증가
    for r, c, _ in fire_info:
        fire_stat[r][c] += 10

    debug_print('화산 압력 증가')

    # [3] 화산 분출
    imsi = [[0]*N for _ in range(N)]    # 외부 열기 표시
    explode_lst = explode()

    debug_print('화산 분출 완료')
    debug_print_imsi()

    # [4] 연쇄 반응
    plus_explode()

    debug_print('연쇄 반응 완료')
    debug_print_imsi()

    # [4] 화석화
    for idx in range(1,M+1):
        if idx in turtle.keys():
            r, c = turtle[idx]

            if imsi[r][c] >= 20:
                arr[r][c] = -1
                turtle.pop(idx)

    # [5] 환경 초기화
    for r, c in explode_lst:
        fire_stat[r][c] = 0

for x in ans[1:]:
    print(x)