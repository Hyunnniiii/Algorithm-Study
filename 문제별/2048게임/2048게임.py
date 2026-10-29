# 09:02 시작
# 09:12 구상완
# 09:55 구현 완 근데 1번 테케가 틀림
# 10:11 중간에 0이 있을 때 틀림을 알아냄
# 10:41 그냥 엎기로 결정


# 1. 상하좌우 중 한 방향을 정한다
# 2. 중력 작용하기
# 해당 방향으로 숫자가 갈 수 있는 만큼 이동.
# 갈 수 있는 만큼 == 벽에 닿거나, 나와 같지 않은 숫자가 다음 칸에 있을 때
# 같은 숫자가 있으면 숫자를 합쳐서 다음칸에 적용.
# 단, 한번만 합침 & 두개씩만 합침

# 구할 것: 격자를 5번 이동해서 얻을 수 있는 가장 큰 블록의 수
# 가능한 모든 경우를 돌려보고 최댓값 구하기? 그러면 4^5 = 3만정도니까 일단 충분함
# N : 격자 크기
N = int(input().strip())
ans_arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]


import pprint
## 함수: 입력된 방향에 따라 2048게임을 1회 수행한다
# 반환할 것: 게임 수행 이후의 arr
def game(direction, arr):
    if direction == 0:  # 상
        for col in range(N):
            lst = []

            # 0이 아닌 수들을 리스트에 담는다
            for row in range(N):
                if arr[row][col] != 0:
                    lst.append(arr[row][col])

            # 리스트 순회하면서 하나씩 계산: 같은 수 더해서 하나로, 다른 수 그냥 그대로
            nlst = []
            i = 0
            while i < len(lst)-1:
                if lst[i] != lst[i+1]:
                    nlst.append(lst[i])
                    i += 1

                elif lst[i] == lst[i+1]:
                    nlst.append(lst[i]*2)
                    i += 2

            if i == len(lst)-1:
                if lst[i] != 0:
                    nlst.append(lst[i])

            # 해당 열 초기화
            for r in range(N):
                arr[r][col] = 0

            # nlst를 순차적으로 다시 배열에 넣어준다
            for idx in range(len(nlst)):
                arr[idx][col] = nlst[idx]

        return arr


    if direction == 1:  # 상
        for col in range(N):
            lst = []

            # 0이 아닌 수들을 리스트에 담는다
            for row in range(N):
                if arr[row][col] != 0:
                    lst.insert(0, arr[row][col])

            # 리스트 순회하면서 하나씩 계산: 같은 수 더해서 하나로, 다른 수 그냥 그대로
            nlst = []
            i = 0
            while i < len(lst)-1:
                if lst[i] != lst[i+1]:
                    nlst.append(lst[i])
                    i += 1

                elif lst[i] == lst[i+1]:
                    nlst.append(lst[i]*2)
                    i += 2

            if i == len(lst)-1:
                if lst[i] != 0:
                    nlst.append(lst[i])

            # 해당 열 초기화
            for r in range(N):
                arr[r][col] = 0

            # nlst를 순차적으로 다시 배열에 넣어준다
            for idx in range(len(nlst)):
                arr[N-1-idx][col] = nlst[idx]

        return arr

    if direction == 2:  # 좌
        for row in range(N):
            lst = []

            # 0이 아닌 수들을 리스트에 담는다
            for col in range(N):
                if arr[row][col] != 0:
                    lst.append(arr[row][col])

            # 리스트 순회하면서 하나씩 계산: 같은 수 더해서 하나로, 다른 수 그냥 그대로
            nlst = []
            i = 0
            while i < len(lst)-1:
                if lst[i] != lst[i+1]:
                    nlst.append(lst[i])
                    i += 1

                elif lst[i] == lst[i+1]:
                    nlst.append(lst[i]*2)
                    i += 2

            if i == len(lst)-1:
                if lst[i] != 0:
                    nlst.append(lst[i])

            # 해당 열 초기화
            for c in range(N):
                arr[row][c] = 0

            # nlst를 순차적으로 다시 배열에 넣어준다
            for idx in range(len(nlst)):
                arr[row][idx] = nlst[idx]

        return arr

    if direction == 3:  # 우
        for row in range(N):
            lst = []

            # 0이 아닌 수들을 리스트에 담는다
            for col in range(N):
                if arr[row][col] != 0:
                    lst.insert(0, arr[row][col])

            # 리스트 순회하면서 하나씩 계산: 같은 수 더해서 하나로, 다른 수 그냥 그대로
            nlst = []
            i = 0
            while i < len(lst)-1:
                if lst[i] != lst[i+1]:
                    nlst.append(lst[i])
                    i += 1

                elif lst[i] == lst[i+1]:
                    nlst.append(lst[i]*2)
                    i += 2

            if i == len(lst)-1:
                if lst[i] != 0:
                    nlst.append(lst[i])

            # 해당 열 초기화
            for c in range(N):
                arr[row][c] = 0

            # nlst를 순차적으로 다시 배열에 넣어준다
            for idx in range(len(nlst)):
                arr[row][N-1-idx] = nlst[idx]

        return arr


from copy import deepcopy
max_ans = 0
## 백트래킹: 5번 수행 후 배열 내 최댓값 구하기
def btrk(idx, b_arr):
    global max_ans
    # 종료: 5번 수행
    if idx == 5:
        ans = 0
        for r in range(N):
            for c in range(N):
                ans = max(ans, b_arr[r][c])
        max_ans = max(max_ans, ans)
        return

    # 4개 방향 중 하나를 선택해서 게임 수행
    for k in range(4):
        new_arr = game(k, deepcopy(b_arr))
        btrk(idx+1, new_arr)

btrk(0, ans_arr)
print(max_ans)

