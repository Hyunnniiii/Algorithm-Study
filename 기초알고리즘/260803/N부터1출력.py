def Ntoone(n):
    if n <= 0:  # 종료조건
        return
    print(n, end=' ')
    Ntoone(n-1)

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T}', end=' ')
    Ntoone(N)
    print()