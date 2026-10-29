for T in range(1, int(input())+1):
    N = int(input())

    ans = -1
    s, e = 0, N

    while s <= e:
        mid = (s + e) // 2

        if mid**3 < N:
            s = mid + 1
        elif mid**3 > N:
            e = mid - 1
        elif mid**3 == N:
            ans = mid
            break

    print(f'#{T} {ans}')