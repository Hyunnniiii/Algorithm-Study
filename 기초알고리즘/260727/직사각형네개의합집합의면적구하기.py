arr = [[0]*10 for _ in range(10)]

for _ in range(4):
    start_x, start_y, end_x, end_y = map(int, input().split())

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            arr[i][j] += 1

num = 0
for i in range(10):
    for j in range(10):
        if arr[i][j] != 0:
            num += 1
print(num)