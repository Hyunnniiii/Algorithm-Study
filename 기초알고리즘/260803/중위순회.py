def in_order(n):
    if 1 <= n <= N:
        # 중위순회: 좌->중->우로 진행
        in_order(2*n)
        print(lst[n], end='')
        in_order(2*n + 1)
    return

for T in range(1, 11):
    N = int(input())
    lst = ['' for _ in range(N+1)]
    for x in range(1, N+1):
        lst[x] = list(input().split())[1]
    print(f'#{T}', end= ' ')
    in_order(1)
    print()