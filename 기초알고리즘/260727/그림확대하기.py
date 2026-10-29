R, C, ZR, ZC = map(int, input().split())

arr = [list(input()) for _ in range(R)]

lst = []
# ZR: 열마다 ZR번씩 반복해서 출력
for cols in arr:
    lst.append(list(x * ZC for x in cols))

# ZC: 행마다 ZC번씩 반복해서 출력
nlst = []
for rows in lst:
    for i in range(ZR):
        nlst.append(rows)


for x in nlst:
    print(*x, sep='')

# ===========
R, C, ZR, ZC = map(int, input().split())

arr = [list(input().split()) for _ in range(R)]

# 열을 ZR배 해서 출력
lst = []
for rows in arr:
    for _ in range(ZR):
        lst.append(rows)
print(lst)

# 행을 ZC배 해서 출력
for cols in lst:
    for

lst = ['A', 'B', 'C']
for x in lst:
    for _ in range(2):
        nlst.append(x)