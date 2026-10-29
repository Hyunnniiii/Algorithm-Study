def printonetoN(n):
    if n > N:
        return
    print(n, end=' ')
    printonetoN(n+1)

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T}', end=' ')
    printonetoN(1)
    print()