

## 입력 받기
# 고객수 N / 유실선 개수 M / 취약지점 개수 H
N, M, H = map(int, input().split())
arr = [[0]*N for _ in range(H+2)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b-1] = 1

## 함수 만들기
# 기능: 입력된 열에 대해 유실선 확인하면서 한 행씩 내려간다. 마지막 행에 도달했을 때 본인의
# 열 인덱스와 같은 곳에 도달하면 그 다음 진행, 아니라면 즉시 종료 후 False 반환
# 반환할 것: 도달 가능 여부
def game(sj, n_arr):
    r_sj = sj
    si = 0
    for _ in range(H+1):
        # 확인
        ni_1, nj_1 = si+1, sj       # 아래
        ni_2, nj_2 = si+1, sj-1     # 좌측 아래

        if (0 <= ni_1 < H+2 and 0 <= nj_1 < N) and n_arr[ni_1][nj_1] == 1:
                si, sj = si+1, sj+1

        elif (0 <= ni_2 < H+2 and 0 <= nj_2 < N) and n_arr[ni_2][nj_2] == 1:
                si, sj = si+1, sj-1

        # 둘 다 없으면 > 그냥 밑으로
        else:
            si, sj = si+1, sj

    # 다 내려갔으면 확인
    if r_sj == sj:
        return True
    else:
        return False


## 유실선 넣을 수 있는 경우 모두 찾아두기
lst = []
for x in range(1, H+1):
    for y in range(N):
        if arr[x][y] == 0:
            # 양 끝 따로 처리
            if y == 0:
                if arr[x][y+1] == 0:
                    lst.append((x, y))
            elif y == N-1:
                if arr[x][y-1] == 0:
                    lst.append((x, y))
            else:
                if arr[x][y+1] == 0 and arr[x][y-1] == 0:
                    lst.append((x,y))

# 함수: M명이 모두 사다리 일직선으로 가는지 확인
def sido(hubo):
    # 일치하는지 확인하기
    # 1. 유실선 집어넣기
    for llst in hubo:
        rx, ry = llst[0], llst[1]
        arr[rx][ry] = 1

    # 2. 집어넣은 배열로 게임 돌리기
    cnt = 0
    for k in range(N):
        res = game(k, arr)
        if not res:
            cnt = 0
            break
        else:
            cnt += 1

    # 되돌리기
    for llst in hubo:
        rx, ry = llst[0], llst[1]
        arr[rx][ry] = 0

    # 3. 게임 결과 내보내기
    if cnt == N:
        return len(hubo), True
    else:
        return  -1, False

## 백트래킹
ans = False
ans_cnt = -1
def btrk(idx, cnt, hubo):
    global ans, ans_cnt, target_cnt
    if ans == True:
        return

    # 조기 종료: T개까지 선택 완료
    if cnt == target_cnt:
        # 여기에서 바로 계산하기
        ans_cnt, ans = sido(hubo)
        return

    # 종료: 모두 선택
    if idx == len(lst):
        return

    # 고르기: 인접한 곳에 선이 없는 경우
    x, y = lst[idx][0], lst[idx][1]
    btrk(idx + 1, cnt, hubo)
    if [x, y-1] not in hubo and [x, y+1] not in hubo:
        btrk(idx+1, cnt+1, hubo + [[x, y]])

for target_cnt in range(0,4):
    btrk(0,0,[])
print(ans_cnt)

