N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
nums = [1,2,3,4,5,6]


# 1. 1번 주사위에서 차례대로 하나씩 바닥으로 해보기
# 1번만 하면 나머지는 다 정해지긴 함
# 마주보는 변의 인덱스 찾기 함수
def find(idx):
    if idx == 0:
        return 5
    if idx == 1:
        return 3
    if idx == 2:
        return 4
    if idx == 3:
        return 1
    if idx == 4:
        return 2
    if idx == 5:
        return 0

# 마주보는 주사위 면 인덱스: 0-5, 2-4, 1-3
lst = []
for i in range(6):  # i: 첫 번째 주사위에서 바닥으로 선택할 면의 인덱스
    max_sum = 0
    bottom = dice[0][i]
    bottom_idx = i

    for j in range(N):  # N번째 주사위까지
        # j번째 주사위의 i번째 면 고르기
        top_idx = find(bottom_idx)   # 윗면의 인덱스
        top = dice[j][top_idx]      # 윗면의 숫자

        # 주사위에서 위/아래 두 숫자 제외하고 max값 선택
        for k in range(6, 1, -1):
            if k != bottom and k != top:
                max_num = k
                break
        max_sum += max_num

        if j < N-1:
            # 그 다음 주사위에서 밑면이 될 면의 인덱스 찾기
            bottom_idx = dice[j+1].index(top)
            bottom = dice[j+1][bottom_idx]
        else:
            break

    lst.append(max_sum)
print(max(lst))
