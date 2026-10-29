N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# print(lst)

score = [1] * N

rank = 1
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        # 둘 다 작으면 -> 등수 내려감
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            score[i] += 1

        # 그 외에는 등수 유지

print(*score)

