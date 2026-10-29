# 말판이 이상하게 생김;
# 어떤 이동 칸 수가 나올지 예상할 수 있다
# 10번만 던질 수 있고, 각 회차마다 나오는 칸 수도 정해져 있다
# 목표: 정해진 칸 수에 따라 말을 잘 조합했을 때 가장 큰 점수 얻기

# 초기: 시작 칸에 말 4개
# 파란색 칸에서 멈추면 빨간색 방향으로 가야 한다/파란색에서 멈추지 않으면 검정색으로 가야 한다
# 도착칸에 도달하면 남은 횟수 상관없이 이동 끝
# 10개 턴 이후 도착칸에 도달하지 않은 말은 골라서 원하는 횟수만큼 이동할 수 있다 >> 뭔소리임?
# 말은 겹칠 수 없다. 그래서 이동헀을 때 그 자리에 다른 말이 있으면 그건 안되는 것
# 도착 != 40

# 뭔소리지?? 일단 무조건 완탐임
# 일단 정리하자면. 4개 말 중에 하나를 골라서 그 회차에 맞는 이동 횟수만큼 이동을 한다.
# 도착한 곳의 점수를 더한다.
# 총 10회 반복이고
# 도착칸에 말이 도달하면 그 말은 더이상 이동 불가
# 도착칸에 도착하지 않은 말을 골라 원하는 이동횟수만큼 이동 > 나 이게 이해가 안됨.
# 원하는 이동 횟수라는게 뭔데? 정해져있는거 아니야? 그렇게 치면 하나만 계속 이동하다가 나머지 전부 40 보내는게
# 이득 아닌가? 근데 계산해보니까 테케 답이 그게 아님. >> 아 이거 턴이 돌아가고 있을 때 얘기구나

# 아니 이거 테케 계산도 어려움. 지능 이슈로 직접 해볼 수가 없음

# ㅎㅎ.. 또 원복에서 막힘
# 딕셔너리 카피해서 원복하는거 왜 안됨?
# 무언가 한끗 차이로 내가 잘못한게 있는데 뭔지 죽어도 모르겠음 >> 미친!! 말이 겹치면 안됨 ㅅㅂ
# 그리고 생각해보니까 그냥 path 상관없이 현재 칸 숫자 같으면 겹치는거임 >> 고쳤더니 인덱스 에러가 계속 나네..
# 뭐야?? 다 고쳤는데 또 틀림 >> 와 미친 같은 숫자여도 칸이 2개인 곳이 있어 심지어 많음
# 진짜 알아냈다. 다른 경로여도 겹치는 지점은 처리 따로 해야됨: 25, 40 이새키들
# 아니 30이랑 35도 겹치네.. 그냥 겹침 판정 함수 만들자

# ==========================
# 칸 입력받기
K = list(map(int, input().split()))

# 길 정보
# 칸수 편하게 하기 위해 앞에 0
path = [i for i in range(0, 42, 2)]
path1 = [0, 13, 16, 19, 25, 30, 35, 40]
path2 = [0, 22, 24, 25, 30, 35, 40]
path3 = [0, 28, 27, 26, 25, 30, 35, 40]

horse = {0: [path, 0],
         1: [path, 0],
         2: [path, 0],
         3: [path, 0]}  # 인덱스: 말 번호 / 값: (현재 길 이름, 현재 길에서의 인덱스)

# 함수: 겹침 판정
# 같은 경로, 같은 인덱스거나 / 다른 경로여도 25,30,35,40이면 겹침
def naga(mal, nxt_path, nxt_idx):
    for idx in horse:
        # 나 자신은 검사 X
        if idx == mal:
            continue

        # 이미 도착했으면 검사 X
        if horse[idx] == [0]:
            continue

        my_path, my_idx = horse[idx]    # 검사하는 말
        # 1. 같은 경로, 같은 인덱스
        if nxt_path == my_path and nxt_idx == my_idx:
            return False

        # 2. 다른 경로, 같은 숫자 (안쪽 경로에서 겹치는 경우)
        if nxt_path[nxt_idx] in (25,30,35):
            if nxt_path[nxt_idx] == my_path[my_idx]:    # 같은 숫자인데
                if nxt_path != path and my_path != path:     # 30 때문에.. 어렵다 내가 하는거지만
                    return False

        # 3. 40은 모든 경로에서 겹친다
        if nxt_path[nxt_idx] == 40 and my_path[my_idx] == 40:
            return False

    return True


# 함수: 파란 칸에서 출발할 때 말 옮기기
def change_path(kan, mal):  # 몇 칸 옮길지, 몇 번 말인지
    status = True
    cur_path, cur_idx = horse[mal]
    # 분기에서 딱 출발하는 경우
    if cur_idx == 5:
        nxt_path, nxt_idx = path1, kan
        status = naga(mal, nxt_path, nxt_idx)

        if status:
            horse[mal][0] = path1
            horse[mal][1] = kan
        return status, path1[kan]

    elif cur_idx == 10:
        nxt_path, nxt_idx = path2, kan
        status = naga(mal, nxt_path, nxt_idx)

        if status:
            horse[mal][0] = path2
            horse[mal][1] = kan
        return status, path2[kan]

    elif cur_idx == 15:
        nxt_path, nxt_idx = path3, kan
        status = naga(mal, nxt_path, nxt_idx)

        if status:
            horse[mal][0] = path3
            horse[mal][1] = kan
        return status, path3[kan]


# 함수: 파란칸 아닐 때 말 옮기기
def move(kan, mal):
    status = True
    cur_path, cur_idx = horse[mal]
    if cur_idx + kan > len(cur_path) - 1:  # 현재 길의 인덱스 넘어갈 때
        horse[mal][0] = [0]
        horse[mal][1] = 0
        return status, 0
    else:
        nxt_path, nxt_idx = cur_path, cur_idx + kan
        status = naga(mal, nxt_path, nxt_idx)

        if status:
            horse[mal][1] += kan
        return status, cur_path[horse[mal][1]]


# 백트래킹..
# 모두 5칸 나왔을 때 조기 종료 가능한가? > no
max_score = -float('inf')
def btrk(cnt, score):
    global max_score, horse
    ## 종료 조건: 10번 다 채웠을 때
    if cnt == 10:
        max_score = max(max_score, score)
        return

    ## 실행
    # [1] horse에 들어있는 말 중 하나를 골라서
    # [2] 주어진 input만큼의 칸 수를 옮기고
    # [3] 점수를 더한다
    kan = K[cnt]

    for h in horse:
        # 저장
        prev_path = horse[h][0]
        prev_idx = horse[h][1]

        new_horse = horse.copy()

        # 도착한 말 제외
        if horse[h][0] == [0]:
            continue

        # 분기점의 인덱스: 5, 10, 15
        if horse[h][0] == path and horse[h][1] in (5, 10, 15):
            status, plus = change_path(kan)
        else:
            status, plus = move(kan, h)

        # 겹치면 이거 진행하지마
        if not status:
            continue

        btrk(cnt + 1, score + plus)
        horse[h][0] = prev_path
        horse[h][1] = prev_idx

        horse = new_horse


btrk(0, 0)
print(max_score)