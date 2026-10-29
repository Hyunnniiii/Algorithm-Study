M = int(input())
lst = list(map(int, input().split()))

coin = [500, 100, 50, 10, 5, 1]
cnt = 0
coin_sum = 0

for i in range(6):
    for _ in range(lst[i]):
        if coin_sum + coin[i] <= M:
            coin_sum += coin[i]
            cnt += 1
        else:
            break

if coin_sum == M:
    print(cnt)
else:
    print(-1)
