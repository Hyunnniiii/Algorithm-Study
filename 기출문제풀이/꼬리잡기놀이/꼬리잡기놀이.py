
''' 꼬리잡기놀이 / 20260910 / 체감 난이도 : 골드 1
소요 시간: 4시간+ / 시도: 5회 / 실행 시간: 147ms (코드트리) / 메모리: 20MB

[타임라인]
09:00 - 09:23(23분) 문제 읽기 / 구상
09:43 - 11:05 (82분) 구현, 1차 제출
11:05 - 11:18 (13분) 휴식
11:18 - 디버깅


[구상]
- 내가 의도했던 구상 자체는 나쁘지 않았던 것 같다. 배열에 group 내 사람 정보만 저장하고, 이동선은 따로 관리, 공 던지기도
N에 따라 미리 다 작성해놓고 턴 수에 따라 자동으로 시작 행/열 출력하기..
- 다만 구체적이지 않았다. 며칠 지나서 내 구상 종이를 들여다보니까 구현 과정 중에라도 조금 더 명확하게 내가 구현하고자 하는
함수의 역할, 자료구조, 입출력 구조에 대해 생각했다면 어땠을까 아쉽다
- 그룹이  꽉 차있는 경우에 대해 전혀 생각하지 못했다 ^^.. 생각하기 귀찮아 하지 말라고
- 내가 꼬인건지는 모르겠는데 팀끼리 이동선 안겹친다는 얘기를 문제에서 해줬는데, 처음에 그 문장을 보자마자 그렇게 해석이 안됐음.
다만 그런 조건이 있어야 문제를 줄 수 있겠다..라는 믿음으로 풀긴 했다..

[구현]
- 가장 큰 패착은 이동선 내에 사람이 꽉 차있는 경우를 전혀 생각하지 못해서, 그룹 찾는 함수 구현할 때 분기점을 4번 이동선으로
잡았다는 것임. 수정하느라 너무 오래걸림..
- 오랜만에 옛날에 하던 실수를 함. 문제에서 보여준 테케에 맞는 정답으로 구현하기 ㅡㅡ
ex: 문제에서 N=7 예시 보여줬는데, 공 던지기 인덱스 7 기준으로 함..

[디버깅]
- 내가 틀린 테케에 엣지 케이스 (이동선 모두 사람으로 차있는 경우)가 나와있어서 뭐가 잘못됐는지 파악하긴 쉬웠다.
- 과연 그 테케를 내가 안봤다면 알아낼 수 있었을까? ㅠㅠ

---------------------------------------------------------
[코드 개선]
- 배열에 이동선 전부 넣고 처리하는거랑, 턴수에 따라 공 시작점 바로 반환하게 미리 만들어두는거 좋아보임

'''


# ========================================
# 첫인상: 뭔가? 최근 문제들보다는 할 일이 적어보인다
# 풀고 돌이옴: ㅋㅋ 응 아니야

# 꼬리잡기의 각 팀은 주어진 이동 선을 따라서만 이동
# 이동선은 각 팀끼리 안겹침. 머리/꼬리사람
# [1] 각 팀마다 머리사람을 따라 한 칸 이동
# - 맨 뒷 사람만 pop해서 맨 앞에 넣으면? 이라고 일단 생각
# [2] 공 던지기
# - 라운드마다 던져지는 행 or 열이 정해져있음
# [3] 공과 최초로 만나는 사람만 점수를 얻는다.
# 팀 내 몇 번째인지의 제곱
# 공을 얻은 팀은 방향을 바꾼다

# 구할 것: 각 팀이 획득한 점수의 총합
# 팀 최대 5개, 최대 1,000라운드
# [주의]
# 최초로 만나는 사람만. 또 있나?
# 그룹별 이동선이 맞닿아있는 경우는 주지 않는다는건가?
# > 이동선의 각 칸은 반드시 2개의 인접한 칸만이 존재? 로 일단 간주해볼게


# 일단 지금 모두 사람으로 차있는 경우를 생각 안해서
# 끝점을 다 4 기준으로 계산하게 처리를 해서 대박 수정이 필요함
# 방향 바꿀 때 그룹 배열도 거꾸로 바꿔줘야 되네ㅣ 순서니까
# 라운드 숫자 커질 때 생각 안함, 머리꼬리 바꿀 때 배열에 적용 안했음
# M개 그룹 찾는거 한번에 처리하게 구현해놓고 for문 또 돌림
# =====================================

# 범위 체크
def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 그룹 내 사람의 좌표를 찾아서 리턴한다.
def find_group():
    team_idx = 0
    for r in range(N):
        for c in range(N):

            # 1부터 차례대로 넣어주겠음
            if arr[r][c] == 1 and visit[r][c] == 0:
                visit[r][c] = 1
                group_info[team_idx].append((r, c))

                status = True
                while status:
                    for k in range(4):
                        nr, nc = r + di[k], c + dj[k]

                        if in_range(nr, nc):
                            # 빈칸 > 그냥 무시해
                            if arr[nr][nc] == 0:
                                continue

                            # 2부터 계속 넣어주다가
                            elif arr[nr][nc] == 2 and visit[nr][nc] == 0:
                                visit[nr][nc] = 1
                                group_info[team_idx].append((nr, nc))
                                r, c = nr, nc
                                break

                            # 3 나오면 끝
                            elif arr[nr][nc]==3:
                                visit[nr][nc] = 1
                                group_info[team_idx].append((nr, nc))
                                team_idx += 1
                                status = False
                                break


# 머리사람을 따라 한 칸씩 이동하기
# 각 배열의 가장 맨 앞의 좌표가 머리사람이다.
# 따라서 나는 각 배열의 맨 뒤 좌표를 삭제하고, arr에서 그 자리 4로 처리해준 다음에
# 맨 앞에 좌표를 추가할건데, 추가할 좌표는 arr에서 인접 4방향 중 4 또는 3이 표시되어 있는 곳
def move():
    global group_info

    new_group_info = [[] for _ in range(len(group_info))]
    for idx in range(len(group_info)):
        # 맨 앞 사람 좌표부터 찾자
        first_r, first_c = group_info[idx][0]

        for k in range(4):
            nr, nc = first_r + di[k], first_c + dj[k]

            # 전진할 곳 어케 찾지
            # 어차피 3명 이상이 한 팀이니까 2도 무조건 있어. 1-3이 붙어있는 경우는 꽉 찬 경우 말고는 읍따
            if in_range(nr, nc) and (arr[nr][nc] == 3 or arr[nr][nc] == 4):
                new_group_info[idx].append((nr, nc))
                break

        # arr 초기화
        for p in group_info[idx]:
            arr[p[0]][p[1]] = 4

        # 맨 뒷사람 제외하고 넣어주자
        group_num = len(group_info[idx])
        for p in range(0, group_num - 1):
            new_group_info[idx].append(group_info[idx][p])

        # 새로운 정보 arr에 반영
        for iidx, put in enumerate(new_group_info[idx]):
            if iidx == 0:
                arr[put[0]][put[1]] = 1
            elif iidx == len(new_group_info[idx]) - 1:
                arr[put[0]][put[1]] = 3
            else:
                arr[put[0]][put[1]] = 2

    group_info = new_group_info


# 공 던지고 싶은데..
# 일단 몇 라운드인지 입력을 받으면 그거에 따라 시작하는 지점을 리턴하자
# 나 이거 왜 계산하다 말았니
def find_throw_and_people(round):
    round = (round - 1) % (4 * N) + 1
    if 0 < round <= N:
        for col in range(N):
            if 0 < arr[round - 1][col] < 4:
                return round - 1, col

    elif N < round <= 2 * N:
        for row in range(N - 1, -1, -1):
            if 0 < arr[row][round - N - 1] < 4:
                return row, round - N - 1

    elif 2 * N < round <= 3 * N:
        for col in range(N - 1, -1, -1):
            if 0 < arr[3 * N - round][col] < 4:
                return 3 * N - round, col

    elif 3 * N < round <= 4 * N:
        for row in range(N):
            if 0 < arr[row][4 * N - round] < 4:
                return row, 4 * N - round
    if True:
        return -1, -1


# 만약 사람을 만났다면, 그룹 배열에서 얘가 어디있는지 찾아
# 방향 바꿔야지!! >> 순서도 바뀌잖아????
# 방향 바꾸면: 순서 바꾸고, arr 숫자도 바꿔 임마
# 찾으면 몇 번째인지에 따라 점수 더해
def score(sr, sc):
    global ans, group_info

    change = []
    for row in group_info:
        if (sr, sc) not in row:
            change.append(row)
        else:
            ans += (row.index((sr, sc)) + 1) ** 2
            # 방향 바꾸기: 그룹 인포에서 해당 행의 순서 바꿔줘야 함
            row.reverse()
            change.append(row)

            # 배열에도 시작이랑 끝 번호 바꿔줘...
            first_r, first_c = row[0][0], row[0][1]
            last_r, last_c = row[-1][0], row[-1][1]

            arr[first_r][first_c] = 1
            arr[last_r][last_c] = 3

    group_info = change


###########################################################
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 그룹별 좌표 리스트 만들기
group_info = [[] for _ in range(M)]
visit = [[0] * N for _ in range(N)]

# M개의 그룹을 찾을게
find_group()

# K개 라운드 동안 진짜 게임 시작
ans = 0
for round in range(1, K + 1):
    # 이동
    move()

    # 공 던져서 사람 만나는지 확인
    people_r, people_c = find_throw_and_people(round)

    # 사람을 만났다면 점수 계산해
    if not (people_r == -1 and people_c == -1):
        score(people_r, people_c)

print(ans)