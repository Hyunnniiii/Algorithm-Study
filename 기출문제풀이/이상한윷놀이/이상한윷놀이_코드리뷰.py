
''' 이상한 윷놀이 / 20260902 / 체감 난이도 : 측정 불가
소요 시간: 3시간+ / 시도: 1회 / 실행 시간: 86ms (코드트리) / 메모리: 18MB

[타임라인]
# 15:46 - 16:00(14분) 문제 읽기 / 입력 받기 / 구상
# 16:00 ~ 구현하다 끝남;;

[구상]
- (bad)
    - 다 갈아엎고 다시 풀고나서 나의 실패한 풀이를 보니 내가 구상을 제대로 한건가? 라는 생각이
    든다. 요즘 시뮬레이션 문제들은 단계를 명확하게 나눠서 풀려고 시도 중인데, 
    구상 중에 그 단계들의 순서가 논리에 맞는지, 어떤 순서로 진행해야 오류가 발생하지 않는지에 대해 
    생각해봐야 하는데 너무 문제에서 제시한 순서대로만 구현하려고 한건 아닌지..
    (문제에서 흰색 > 빨간색 > 파란색 순서로 안내해줘서 나도 그 순서대로 단계를 나눠서 구현했음.
    근데 다시 풀어보니까 애초에 처음에 파란색이거나, 못 가는 경우를 처리해두고 빨강/흰색을 
    한번에 처리하는게 단계상 훨씬 구현하기 쉬운데, 그냥 문제에서 그렇게 알려줬으니까-라는
    생각으로 단계를 정해버렸다)

[구현]
- (bad)
    - 나 자신도 이해하기 어려운 논리로 코드를 구성해서.. 점점 갈 수록 구현하기도 힘들고
    나도 내가 뭘 하고 있는지 이해 못하는 대참사 발생.

    - 전반적으로 배열 안에 리스트 넣어서 활용해본 적이 없던 터라 구현에서 심각한 버벅임을 경험했다.
    배열 안에 리스트를 집어넣고, 거기에 리스트를 append하는 과정에서 아주 많은 시간을 헤맸음.
    (1) 리스트 append하면 [1, 2]로 들어가는데 나는 1, 2를 넣고 싶었다.
    그래서 append(*lst)를 했더니 안된대.
    >> extend를 했어야 함. extend는 lst 안의 원소들을 풀어서 추가해준다..

    (2) 배열 생성할 때 [[[]]*N for _ in range(N)]을 해서 같은 행 안의 리스트들이
    전부 같은 객체가 됨. 그래서 난 분명 arr[1][2]에 append를 했는데 arr[1]에 모두 추가되는
    사고 발생. 나중에 알아채고 바꾸긴 했지만 여기서도 시간 엄청 잡아먹음

---------------------------------------------------------
[개선할 사항]
- 나의 정신머리

'''
# =======================================================

# 0. 번호 찾고 그 번호의 방향으로 이동
# 1. 이동한 칸이 범위 밖/파란색이면 > 방향 바꿔주고 반대편 확인
# 2. 반대편도 범위 밖이거나 파란색이면 > 그 숫자는 그냥 그 자리 그대로
# 3. 이동하기: 빨/흰/반대편인 경우
# 4. 이동 후 쌓인 말 4개인 곳 있는지 확인

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
yoot = {}
arr = [[[] for _ in range(N)] for _ in range(N)]

# 우좌상하
di = [0,0,-1,1]
dj = [1,-1,0,0]

# 방향 바꾸기 (인덱스 > 값으로 변경)
change = [1,0,3,2]

for i in range(1, K+1):
    x, y, d = map(int, input().split())
    yoot[i] = [x-1, y-1, d-1]
    arr[x-1][y-1].append(i)

ans = 0
status = True
while status:
    ans += 1

    # 1000번 시도해도 안되면 그만해라
    if ans > 1000:
        ans = -1
        status = False
        break

    for idx in range(1, K+1):
        # [0] 번호 찾고 해당 방향대로 이동한 칸 살펴보기
        cur_r, cur_c, cur_d = yoot[idx][0], yoot[idx][1], yoot[idx][2]
        nxt_r, nxt_c = cur_r + di[cur_d], cur_c + dj[cur_d]

        # [1] 못 가는 칸이면 방향 바꿔주기: 파란색, 범위 밖
        if not (0 <= nxt_r < N and 0 <= nxt_c < N) or color[nxt_r][nxt_c] == 2:
            yoot[idx][2] = change[cur_d]

        # [2] 방향 바꾼 뒤에 이동 가능한지 확인, 못 가면 break
        cur_d = yoot[idx][2]
        nxt_r, nxt_c = cur_r + di[cur_d], cur_c + dj[cur_d]

        if not (0 <= nxt_r < N and 0 <= nxt_c < N) or color[nxt_r][nxt_c] == 2:
            continue

        # [3] 여기까지 온거면 이동은 할 수 있는 거임. 빨강/흰색 이동
        if color[nxt_r][nxt_c] == 0:    # 흰색이면
            # 원래 배열에서 이동할 숫자의 인덱스를 찾아서
            to_see = arr[cur_r][cur_c]
            move_idx = to_see.index(idx)
            move = to_see[move_idx:]    # 그 인덱스 이후의 말 모두 이동
            arr[cur_r][cur_c] = to_see[:move_idx]   # 원래 배열에 인덱스까지만 남긴다

            # 말 옮기기, yoot에도 좌표 반영
            for x in move:
                arr[nxt_r][nxt_c].append(x)
                yoot[x][0], yoot[x][1] = nxt_r, nxt_c

        elif color[nxt_r][nxt_c] == 1:    # 빨간색이면
            # 이동할 말의 순서를 뒤집은 다음에 동일한 과정 수행
            to_see = arr[cur_r][cur_c]
            move_idx = to_see.index(idx)
            move = to_see[move_idx:]
            move.reverse()
            arr[cur_r][cur_c] = to_see[:move_idx]
            for x in move:
                arr[nxt_r][nxt_c].append(x)
                yoot[x][0], yoot[x][1] = nxt_r, nxt_c

        # [4] 옮긴 뒤에 말이 4개 이상 쌓였는지 확인하기
        if len(arr[nxt_r][nxt_c]) >= 4:
            status = False
            break

print(ans)