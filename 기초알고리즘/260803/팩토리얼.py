def factorial(n):
    if n > N:
        return 1
    return n * factorial(n+1)

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T} {factorial(1)}')