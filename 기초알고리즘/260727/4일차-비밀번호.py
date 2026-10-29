for T in range(1,11):
    N, pswd = input().split()
    N = int(N)

    stk = []
    for x in pswd:
        if stk and x == stk[-1]:
            stk.pop()
        else:
            stk.append(x)
    print(f'#{T}', ''.join(stk))