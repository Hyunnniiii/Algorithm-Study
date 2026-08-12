for T in range(1, int(input())+1):
    N, D = map(int, input().split())
    lst = list(map(int, input().split()))

    s, e = 0, N-1
    ans = 0

    while s <= e:
        mid = (s + e) // 2

        if lst[mid] > D:
            e = mid - 1
        elif lst[mid] < D:
            s = mid + 1
        else:
            ans = mid + 1
            break

    print(f'#{T} {ans}')