def duhagi(n):
    if n > N:
        return 0
    return n + duhagi(n+1)

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T}', end=' ')
    print(duhagi(1))


# 또다른 방법
ans = 0
def acc(n):
    global ans
    if n == N+1:
        return
    ans += n
    acc(n+1)