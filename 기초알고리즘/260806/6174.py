N = int(input())
L = [0]*4

for i in range(4):
    count = 0
    while N >= 0:
        N = N - 10 ** (3 - i)
        count += 1
    N = N + 10 ** (3 - i)
    L[i] = count - 1

cnt = 0

kaprekar = True
while kaprekar:
    max_lst = sorted(L, reverse=True)
    min_lst = sorted(L)

    max_number = 0
    min_number = 0

    for i in range(4):
        max_number += max_lst[i] * (10**(3-i))
        min_number += min_lst[i] * (10**(3-i))

    ans = max_number - min_number
    cnt += 1

    if ans == 6174:
        kaprekar = False
        break

    else:
        for i in range(4):
            count = 0
            while ans >= 0:
                ans = ans - 10 ** (3 - i)
                count += 1
            ans = ans + 10 ** (3 - i)
            L[i] = count - 1
print(cnt)
