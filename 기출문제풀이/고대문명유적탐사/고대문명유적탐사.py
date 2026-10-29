
''' 고대 문명 유적 탐사 / 20260917 / 체감 난이도 : 골드 5
소요 시간: 2h 40m / 시도: 2회 / 실행 시간: 146ms (코드트리) / 메모리: 21MB

[타임라인]
09:00 - 09:22(22분) 문제 읽기 / 입력 받기 / 구상
09:22 - 11:13(100분) 구현, 1차 제출
11:13 - 11:44(31분) 디버깅으로 실수 확인 후 2차 제출

[구상]
- 일단 처리해야 할 정보가 그리 많지 않아서 자료 구조 선택은 쉽게 했다
- 그리고 그냥 지금까지 공부해온 내용 짬뽕한 느낌을 받아서.. 쉬운 문제구나?? 하지만 절대 방심하지마 라고 생각함
- 이 문제는 탐색하는 시간(?)이 굉장히 길다고 생각했다. 일단 돌릴 위치 선정해야 되고, 그 위치에서 어느 방향으로 돌릴지
정해야 되고.. 그걸 정하고 나서야 실제로 배열을 바꿔야 하므로..
- 그리고 마지막에 턴 별 점수 출력하는걸 빼먹고 안봐서 마지막에 구현하다 바꿈 ㅡㅡ 끝까지 문제 다 읽으라고

[구현]
- 나 요즘 왜이렇게 오타가 늘었을까르??
중간에 bfs 구현하면서 확인하는데 이상하게 돌아가서 한참 헤맸다. (20분 정도)
알고보니 nr, nc 거꾸로 씀 ㅡㅡ 아 진짜 뭐하냐고 진짜 뭐하냐고 뭐하냐고 뭐하냐고
ㄴ> 영상 다시 돌려보니까 내가 원래 visit[x][y]라고 썼다가 nr, nc로 수정하는데 y부터 바꿔서 그리 되었나봄
bfs 템플릿 이제 익숙해서 내가 너무 뇌에 힘 빼고 구현하나본데 진짜 오늘을 계기로 그러지좀 마라

- 멘헤라
1차 제출 때 틀려서 멘붕이 좀 왔다. 왜냐면 누가 제출했는지 의도치 않게 봤는데 이미 다들 너무 많이 성공함!!
일부러 안보려고 의식적으로 피하는데 정답 제출할 때만큼은 볼 수 밖에 없으니.. 아무튼
난 진짜 다 맞았다고 생각했고, 구상 때부터 왤케 쉽지? 라고 생각도 했었고.. 근데 3번을 틀려서 진짜
어디서부터 다시 봐야할지에 대해 너무 막막했음. 그리고 오늘 이거 못 푸는건가? 이런 것 마저 못 풀면 어카지?
등등 멘헤라 옴.

- 사실 본좌는 제출한 코드가 맘에 들지 않음. 너무 깔끔하지 않다.
배열 부분 회전해서 원래 arr에 집어넣는거 예전에 했는데 왜 상대좌표를 쓰질 못하니? 응 다시 공부해~~ 오늘이라도 알아서 다행이야
리팩토링에서 싹 다 갈아엎고 배열 회전도 마스터 하도록 하자
그리고 후보 정할 때 쓰는 임시 배열, 실제로 정한 배열 구분해서 변수를 굉장히 많이 사용했는데 이게 맞는건지..
ex: imsi, real_imsi 이런 식으로 임시의 임시를 만듦;; 반드시 리팩토링 할 것


[디버깅]
- 첫 제출 틀리고 아직 2시간 정도 남았으니 침착하자 마인드로 그냥 맨 처음부터 다 print 찍어서 들여다봄.
혹시나 회전에서 틀렸나 싶어서 270도 회전도 그냥 90도 3번으로 바꿈. 왜냐면 난 90도 회전만은 완벽하게
공부했으니까. 모든 과정을 지켜본 결과.. 진짜 뒤에선 틀린거 전혀 없고 뭔가 사각형 선택 자체를 잘못하고 있다는
생각이 들었음.
그래서 보니까???? 아니 내가 range를 잘못썼네.... 진짜 뭐하냐고 곱하기 백억
이 사소한 오타 찾는데만 30분이 걸림 ㅡㅡ 진짜 오타 그냥 내지 마


[후기]
- 첫인상: 쉽다
- 끝인상: 처리하는 범위가 길어지다 보니 쉽지만은 않았다.

---------------------------------------------------------
[개선]
코드 다듬기, 배열 회전 다시 공부

'''

# [1] 탐사 진행
# 3x3 크기의 격자를 선택해서 회전시킨다.
# 회전은 90도, 180도, 270도 중 하나 가능
# 회전은 항상 진행
# 목표: 유물 1차 획득 가치 최대화 > 회전 각도 가장 작게 > 회전 중심 좌표 열 작게 > 행 작게

# [2] 유물 획득
# 1차 획득: 상하좌우로 인접한 같은 종류의 우물 조각이 3개 이상 연결된 경우
# 총 모인 조각의 개수가 유물의 가치
# 유물은 획득하면 사라진다

# 사라진 다음에, 유적의 벽면에 있는 숫자들을 순서대로 집어넣는다
# 작은 열 > 큰 행
# 벽면의 숫자는 충분하다
# 사용한 벽면의 숫자는 다시 사용 불가. 남은 숫자부터 순서대로

# [3] 유물 연쇄 획득
# 벽면 숫자로 채운 뒤에도 조각이 또 연결될 수 있다.
# 따라서 벽면 숫자로 채우고, 연결된거 지우는 과정을 연결된게 없을 때까지 반복

# [4] 종료
# 탐사 진행 과정에서 유물을 획득할 수 없으면 바로 종료
# 또는 K번의 턴이 모두 진행되면 종료

# 구할 것: 각 턴마다 획득한 유물의 가치의 총합
# ========================================

# 일단 의심
# 첫 턴에 끝나는 경우 > 없다고 해줌
# 벽면이 부족하면? > 그런 경우 없다고 해줌
# 종료 조건 어디서 확인? > 회전 직후에만. 1차 획득하고 더 없으면 바로 회전하면 됨
# ============================================
from collections import deque

# 범위
def in_range(nr,nc):
    return 0<=nr<5 and 0<=nc<5

# 회전 3가지 (순서대로 90, 180, 270도)
def rotate_arr(idx):
    global imsi
    if idx == 1:
        imsi = [row[:] for row in zip(*imsi[::-1])]
    elif idx == 2:
        imsi = [row[:] for row in zip(*imsi[::-1])]
        imsi = [row[:] for row in zip(*imsi[::-1])]
    elif idx == 3:
        imsi = [row[:] for row in zip(*imsi[::-1])]
        imsi = [row[:] for row in zip(*imsi[::-1])]
        imsi = [row[:] for row in zip(*imsi[::-1])]


# 유물 획득 bfs
def bfs():
    global tot_yumul_cnt, tot_trace
    visit = [[0]*5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            if visit[x][y] == 0:    # 이미 카운팅 된 곳은 제외
                Q = deque([(x,y)])
                visit[x][y] = 1
                my_yumul = imsi_arr[x][y]    # 현재 내가 찾는 유물 번호
                yumul_cnt = 1           # 현재 내가 찾는 유물의 인접한 개수
                trace = [(x,y)]              # 지나온 경로 저장

                while Q:
                    sr, sc = Q.popleft()
                    for k in range(4):
                        nr, nc = sr+dr[k], sc+dc[k]

                        # 범위내, 미방문, 같은숫자
                        if in_range(nr,nc) and visit[nr][nc] == 0 and imsi_arr[nr][nc] == my_yumul:
                            visit[nr][nc] = 1
                            yumul_cnt += 1
                            trace.append((nr, nc))
                            Q.append((nr,nc))

                # 탐색완료 했을 때 카운트 3 이상이면 반영
                if yumul_cnt >= 3:
                    tot_yumul_cnt += yumul_cnt
                    tot_trace = tot_trace + trace


###############################
K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))
res = [0]*K

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

## 실행
for turn in range(K):
    # 하나의 턴에서 얻는 유물 총 개수
    ans = 0

    # 하나의 턴에서 내가 선택할 진짜 조합
    final_info = (0, 200, 200, 200)
    final_route = []

    # 1. 격자 내에서 3x3 격자의 중심을 선택
    for middle_r in range(1,4):
        for middle_c in range(1,4):

            # 회전할 임시 배열
            real_imsi = [row[middle_c-1:middle_c+2] for row in arr[middle_r-1:middle_r+2]]

            # 3가지 옵션 중 하나로 회전
            for gakdo in range(1, 4):
                imsi = real_imsi
                imsi_arr = [row[:] for row in arr]

                rotate_arr(gakdo)

                # 회전한 임시 배열을 그 자리에 다시 느
                i = 0
                for rr in range(middle_r-1,middle_r+2):
                    j = 0
                    for cc in range(middle_c-1, middle_c+2):
                        imsi_arr[rr][cc] = imsi[i][j]
                        j += 1
                    i += 1

                # 그러면 이제 회전 완료. 유물 획득 ㄱㄱ
                tot_yumul_cnt = 0  # 총 유물 개수
                tot_trace = []  # 지울 곳들 좌표 모두 모음
                bfs()

                # 정산해봅시다
                info = (tot_yumul_cnt, -gakdo, -middle_c, -middle_r)
                if info > final_info:
                    final_info = info
                    final_route = tot_trace

    # 그럼 이제 회전 3개에 대한 제일 좋은 선택지가 나옴
    # > 근데 여기서 아무것도 없으면 끝
    # 종료 처리 나중에 와서 여기서 해라
    if final_info[0] == 0:
        break

    # 그러면 정답에 유물 추가, 진짜 선택지로 회전
    ans += final_info[0]
    imsi = [row[-final_info[2]-1:-final_info[2]+2] for row in arr[-final_info[3]-1:-final_info[3]+2]]
    rotate_arr(-final_info[1])

    print('배열에 반영하기 전 확인, 정보', final_info)
    print(imsi)
    for row in arr:
        print(row)
    print()

    # 회전한 임시 배열을 그 자리에 다시 느
    i = 0
    for rr in range(-final_info[3] - 1, -final_info[3] + 2):
        j = 0
        for cc in range(-final_info[2] - 1, -final_info[2] + 2):
            arr[rr][cc] = imsi[i][j]
            j += 1
        i += 1
    print('배열에 넣어줌')
    for row in arr:
        print(row)
    print()

    # final route를 행 큰, 열 작은 순서대로 sort
    # 비운 다음에 벽면 숫자 넣기
    final_route.sort(key = lambda x : (x[1], -x[0]))
    for x, y in final_route:
        arr[x][y] = wall.pop(0)



    print('1차 완료')
    print('파이널 정보', final_info)
    for row in arr:
        print(row)
    print('일단 한 번 해서 획득한 양: ', ans)
    print()

    # 유물 연쇄 획득 가능한지 확인
    while True:
        imsi_arr = [row[:] for row in arr]
        tot_yumul_cnt = 0
        tot_trace = []
        bfs()

        # 만약 더이상 없다면 > 끝
        if tot_yumul_cnt == 0:
            break

        # 또 있다면 > final route 정렬, 숫자 넣기, bfs 실행
        ans += tot_yumul_cnt
        print('추가로', tot_yumul_cnt, '점 얻음')
        tot_trace.sort(key=lambda x: (x[1], -x[0]))
        for x, y in tot_trace:
            arr[x][y] = wall.pop(0)

    print('추가까지 완료 후 상황')
    for row in arr:
        print(row)
    print('=====')

    res[turn] += ans

res = [x for x in res if x != 0]
print(*res)




