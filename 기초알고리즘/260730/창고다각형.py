# 최고 높이인 기둥을 기준으로 좌/우
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

max_idx = 0
max_height = 0
for x in lst:
    if max_height < x[1]:
        max_height = x[1]
        max_idx = x[0]

# 좌: 나보다 높은 기둥이 나올 때까진 현재 길이를 더한다
size = 0
cur_h = lst[0][1]
for i in range(0, lst.index([max_idx, max_height])):
    # 나보다 뒤가 더 크면 바꾸고
    if cur_h < lst[i+1][1]:
        size += cur_h * (lst[i+1][0] - lst[i][0])
        cur_h = lst[i+1][1]
    # 아니면 유지
    else:
        size += cur_h * (lst[i+1][0] - lst[i][0])

# 우: 뒤에서부터 나보다 높은 기둥이 나올 때까지 현재 길이 더한다
for i in range(lst.index([max_idx, max_height])):
    lst.pop(0)

# 최고 높이 더해주기
size += max_height

# 뒤에서부터 구하기
cur_h = lst[-1][1]
for j in range(len(lst)-1, 0, -1):
    # 나보다 앞이 더 크면 바꾸고
    if lst[j-1][1] > cur_h:
        size += cur_h * (lst[j][0] - lst[j-1][0])
        cur_h = lst[j-1][1]
    # 아니면 유지
    else:
        size += cur_h * (lst[j][0] - lst[j-1][0])
print(size)

